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

int t,n,id;
LL m,mx;
bool a[55][55];

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        memset(a,0,sizeof(a));
        scanf("%I64d%I64d",&n,&m);
        mx=(LL)pow(2,n-2);
        printf("Case #%d: ",z);
        if(m>mx)    printf("IMPOSSIBLE\n");
        else
        {
            printf("POSSIBLE\n");
            for(int i=0;i<n;i++)
            {
                for(int j=i+1;j<n;j++)  a[i][j]=true;
            }
            if(m!=mx)
            {
                a[0][n-1]=false;
                id=1;
                while(m!=0)
                {
                    if(m%2==0)  a[id][n-1]=false;
                    m/=2;
                    id++;
                }
                while(id!=n)
                {
                    a[id][n-1]=false;
                    id++;
                }
            }

            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)    printf("%d",a[i][j]?1:0);
                printf("\n");
            }
        }
    }
    return 0;
}
