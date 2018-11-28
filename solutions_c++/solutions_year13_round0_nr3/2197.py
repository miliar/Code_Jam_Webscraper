#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

bool palindrome(int n)
{
    int d[10];
    int m=0;
    while (n>0)
    {
        d[m++]=n%10;
        n/=10;
    }
    for (int i=0;i<m;i++)
    {
        if (d[i]!=d[m-1-i]) return false;
    }
    return true;
}
int main()
{
    vector<int> v;
    int T,A,B;
    v.push_back(1);
    for (int i=2;i<=31;i++)
    {
        if (palindrome(i) && palindrome(i*i))
        {
            v.push_back(i*i); 
            //printf("%d\n",i*i);
        }
    }
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C_output_small.txt","w",stdout);
    //printf("size=%d\n",v.size());
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        scanf("%d%d",&A,&B);
        int result=0;
        for (int i=0;i<v.size();i++)
        {
            if (v[i]>=A && v[i]<=B) result++;
        }
        printf("Case #%d: %d\n",cases,result);
    }
    return 0;
}
