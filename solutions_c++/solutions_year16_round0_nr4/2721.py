#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    long long int t,sv;
    long long int k,c,s,t1,num;
    scanf("%lld",&t);
    sv=t;

    while(t--)
    {
        num=1;
        scanf("%lld%lld%lld",&k,&c,&s);

        t1=pow(k,c-1);

        printf("Case #%lld: 1",sv-t);
        for(long long int i=2;i<=k;i++)
        {
            num+=t1;
            printf(" %lld",num);
        }
        printf("\n");
    }

    return 0;
}
