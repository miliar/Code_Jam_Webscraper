#include<bits/stdc++.h>
#define scf scanf
#define ptf printf
#define forp(i,j,k) for(int i=j;i<k;i++)
#define form(i,j,k) for(int i=j;i>k;i--)
#define sz(x) (int)x.size()
#define pb push_back
#define fst first
#define scd second
using namespace std;

typedef long long LL;

const int N=1010,M=100000;

int coms[N][N],len[N],a[N],p[N][N],lis[M][100],tot,tmp[N],num[N],nnn,ans,cnt;
char str[N][110];



int check()
{
    int res=0,mx;
    forp(i,0,nnn)
    {
        forp(j,0,num[i])
        {
            mx=0;
            forp(k,0,j)
                mx=max(mx,coms[p[i][j]][p[i][k]]);
            res+=len[p[i][j]]-mx;
        }
    }
    return res;
}

void dfs(int x)
{
    int t0;
    if(!x)
    {
        forp(i,0,nnn)if(!num[i])return;
        t0=check();
        if(t0>ans){ans=t0;cnt=0;}
        if(t0==ans)cnt++;
        return;
    }
    forp(i,0,nnn)
    {
        p[i][num[i]++]=x-1;
        dfs(x-1);
        num[i]--;
    }

}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,n,m;
    scf("%d",&T);
    forp(tcnt,0,T)
    {
        scf("%d%d",&m,&n);
        nnn=n;
        forp(i,0,m)scf("%s",str[i]);
        forp(i,0,m)
        {
            a[i]=i+1;
            len[i]=strlen(str[i]);
        }
        int fg;
        forp(i,0,m)
            forp(j,0,m)
            {
                fg=0;
                forp(k,0,min(len[i],len[j]))
                    if(str[i][k]!=str[j][k])
                    {
                        coms[i][j]=k;
                        fg=1;
                        break;
                    }
                if(!fg)coms[i][j]=min(len[i],len[j]);
            }
        memset(num,0,sizeof(num));
        ans=cnt=0;
        dfs(m);
        int l,t0;
        ptf("Case #%d: %d %d\n",tcnt+1,ans+n,cnt);
    }
    return 0;
}
