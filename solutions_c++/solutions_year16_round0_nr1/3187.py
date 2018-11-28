#include<stdio.h>
#include<set>
using namespace std;
set<int> s;
int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int t,l=0;
    scanf("%d",&t);
    long long n;
    while(l<t)
    {   l++;
        long long i,k,tmp;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",l);
            continue;
        }
        for(i=0;i<=9;i++) s.insert(i);
        i=1;
        while(!s.empty())
        {
            k=i*n;
            tmp=k;
            while(k)
            {
                s.erase(k%10);
                k/=10;
            }
            i++;
        }
        printf("Case #%d: %lld\n",l,tmp);
    }
    return 0;
}
