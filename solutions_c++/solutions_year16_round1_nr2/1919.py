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

int t,n,x,cnt[2505],tmp[55],id;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        memset(cnt,0,sizeof(cnt));
        id=0;
        scanf("%d",&n);
        for(int i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                scanf("%d",&x);
                cnt[x]++;
            }
        }
        for(int i=1;i<=2500;i++)
        {
            if(cnt[i]%2==1)
            {
                tmp[id]=i;
                id++;
            }
        }
        sort(tmp,tmp+n);
        printf("Case #%d: ",z);
        for(int i=0;i<n;i++)    printf("%d ",tmp[i]);
        printf("\n");
    }
    return 0;
}
