#include<bits/stdc++.h>
#define scf scanf
#define ptf printf
#define forp(i,j,k) for(int i=j;i<k;i++)
#define form(i,j,k) for(int i=j;i>k;i--)
#define sz(x) (int)x.size()
#define pb push_back
#define fst first
#define scd second
#define m_p make_pair
#define pct __builtin_popcount
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int dx[]={0,0,-1,1},dy[]={1,-1,0,0};
int n,m,can[10];
char mp[110][110];
map<char,int>H;

int in(int x,int y,int n,int m)
{
    return x>=0&&x<n&&y>=0&&y<m;
}

void doit()
{
    int ans=0,fg,cnt,x,y;
    forp(i,0,n)
        forp(j,0,m)
        {
            if(mp[i][j]=='.')continue;
            cnt=0;
            forp(k,0,4)
            {
                fg=0;
                x=i;y=j;
                for(;;)
                {
                    x+=dx[k];y+=dy[k];
                    if(!in(x,y,n,m))break;
                    if(mp[x][y]!='.')
                    {
                        fg=1;
                        break;
                    }
                }
                can[k]=fg;
                cnt+=fg;
            }
            if(cnt==0)
            {
                puts("IMPOSSIBLE");
                return;
            }
            if(!can[H[mp[i][j]]])ans++;
        }
    ptf("%d\n",ans);
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    scf("%d",&T);
    H['>']=0;H['<']=1;H['^']=2;H['v']=3;
    forp(tcnt,0,T)
    {
        scf("%d%d",&n,&m);
        forp(i,0,n)
            scf("%s",mp[i]);
        ptf("Case #%d: ",tcnt+1);
        doit();

    }
    return 0;
}
