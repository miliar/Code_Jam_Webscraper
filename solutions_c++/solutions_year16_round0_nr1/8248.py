#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[20];
bool dfs(long long m)
{
    while(m)
    {
        a[m%10]=1;
        m/=10;
    }
    for(int j=0;j<=9;j++)
    {
        if(!a[j]) return false;
    }
    return true;
}
int main()
{
    int t,kk,sum;
    long long n,i;
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);

    scanf("%d",&t);
    kk=t;
    while(t--)
    {
        for(int j=0;j<=11;j++)a[j]=0;
        scanf("%lld",&n);
        if(n==0) {printf("Case #%d: INSOMNIA\n",kk-t);continue;}
        for(i=1;;i++)
        {
            if(dfs(n*i)) break;
        }
        printf("Case #%d: %lld\n",kk-t,n*i);
    }
    return 0;
}
/*


5
0
1
2
11
1692
*/
