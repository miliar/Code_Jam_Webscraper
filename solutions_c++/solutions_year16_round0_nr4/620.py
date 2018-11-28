#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<vector>

#define pii pair<int,int>
#define F first
#define S second
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

using namespace std;

int t;
LL k,c,s,v[105],n,id;

int main()
{
//    freopen("D-large.in","r",stdin);
//    freopen("D-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        scanf("%I64d%I64d%I64d",&k,&c,&s);
        if((double)k/c>s)
        {
            printf("Case #%d: IMPOSSIBLE\n",z);
            continue;
        }
        v[0]=1;
        for(int i=1;i<c;i++)    v[i]=v[i-1]*k;
        printf("Case #%d: ",z);
        for(n=1;n<=k;n+=c)
        {
            id=1;
            for(int i=0;i<c;i++)
            {
                id+=min(n+i-1,k-1)*v[i];
            }
            printf("%I64d ",id);
        }
        printf("\n");
    }
    return 0;
}
