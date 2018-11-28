#include<stdio.h>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>

#define msn(x) (memset((x),0,sizeof((x))))
#define msx(x,y) (memset((x),0x7f,sizeof((x[0]))*(y+3)))
#define fuck(x) cerr << #x << " <- " << x << endl
#define acer cout<<"sb"<<endl
typedef long long ll;
using namespace std;
char mp[111][111];
bool np[111][111][4];
int n,m;
int T;
int cal()
{
    int ans=0;
    for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                bool flag=0;
                for(int k=0;k<4;k++)if(np[i][j][k]==0)flag=1;
                if(flag==0)return -1;
                if(mp[i][j]=='^'&&np[i][j][0]==1)ans++;
                else if(mp[i][j]=='v'&&np[i][j][1]==1)ans++;
                else if(mp[i][j]=='<'&&np[i][j][2]==1)ans++;
                else if(mp[i][j]=='>'&&np[i][j][3]==1)ans++;
            }
        }
        return ans;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        msn(np);
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)scanf("%s",mp[i]);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(mp[i][j]!='.')
                {np[i][j][2]=1;
                break;
                }
            }
            for(int j=m-1;j>=0;j--)
            {
                if(mp[i][j]!='.')
                {
                    np[i][j][3]=1;
                    break;
                }
            }
        }
        for(int j=0;j<m;j++)
        {
            for(int i=0;i<n;i++)
            {
                if(mp[i][j]!='.')
                {
                    np[i][j][0]=1;
                    break;
                }
            }
            for(int i=n-1;i>=0;i--)
            {
                if(mp[i][j]!='.')
                   {
                       np[i][j][1]=1;
                        break;
                   }
            }
        }
int ans=cal();
printf("Case #%d: ",cas);
if(ans==-1)
{
    printf("IMPOSSIBLE\n");
}
else printf("%d\n",ans);
    }
    return 0;
}
