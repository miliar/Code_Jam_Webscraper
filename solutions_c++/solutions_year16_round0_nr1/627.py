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

int t,c,n,ans,m,g;
bool ch[10];

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        memset(ch,0,sizeof(ch));
        c=0;
        m=1;
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",z);
            continue;
        }
        while(c!=10)
        {
            ans=m*n;
            while(ans!=0)
            {
                g=ans%10;
                if(!ch[g])
                {
                    ch[g]=true;
                    c++;
                }
                ans/=10;
            }
            ans=m*n;
            m++;
        }
        printf("Case #%d: %d\n",z,ans);
    }
    return 0;
}
