/*
TASK: Enclosure
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T,K,X;
int tb[127][127];
int co,Mc,sum=0;
int dp[23][23][23];
void iSearch(int val)
{
    //printf("%d %d\n",val,sum++);
    int x,y,z,i,j;
    if(val==X)
    {
        int ok=0;
        for(i=1;i<=N;i++)
        {
            for(j=1;j<=M;j++)
            {
                if(tb[i][j]==1)
                    ok++;
                else if(tb[i][j]==0)
                {
                    queue<PII> Q;
                    tb[i][j]=2;
                    Q.push(mp(i,j));
                    bool chk=false;
                    int temp=1;
                    while(!Q.empty())
                    {
                        x=Q.front().X;
                        y=Q.front().Y;
                        Q.pop();
                        if(tb[x+1][y]==0)
                        {
                            if(x+1>N)
                            {
                                chk=true;
                                break;
                            }
                            tb[x+1][y]=2;
                            temp++;
                            Q.push(mp(x+1,y));
                        }

                        if(tb[x][y+1]==0)
                        {
                            if(y+1>M)
                            {
                                chk=true;
                                break;
                            }
                            tb[x][y+1]=2;
                            temp++;
                            Q.push(mp(x,y+1));
                        }
                        //------
                        if(tb[x-1][y]==0)
                        {
                            if(x-1<1)
                            {
                                chk=true;
                                break;
                            }
                            tb[x-1][y]=2;
                            temp++;
                            Q.push(mp(x-1,y));
                        }

                        if(tb[x][y-1]==0)
                        {
                            if(y-1<1)
                            {
                                chk=true;
                                break;
                            }
                            tb[x][y-1]=2;
                            temp++;
                            Q.push(mp(x,y-1));
                        }
                    }
                    if(!chk) {
                        ok+=temp;
                        for(int ii=1;ii<=N;ii++)
                        for(int jj=1;jj<=M;jj++)
                            if(tb[ii][jj]==2)
                                tb[ii][jj]=3;
                    }
                    else
                    {
                        for(int ii=1;ii<=N;ii++)
                        for(int jj=1;jj<=M;jj++)
                            if(tb[ii][jj]==2)
                                tb[ii][jj]=0;
                    }
                }
            }
        }
        for(i=1;i<=N;i++)
            for(j=1;j<=M;j++)
                if(tb[i][j]>1)
                    tb[i][j]=0;
//        if(ok>=K)
//            Mc=min(Mc,co);
        for(i=1;i<=ok;i++)
        {
            dp[N][M][i]=min(dp[N][M][i],co);
            dp[M][N][i]=min(dp[M][N][i],co);
        }
        return ;
    }
    x=val/M;    // row
    y=val%M;    // col
    x++;    y++;
    tb[x][y]=1; co++;
    iSearch(val+1);
    tb[x][y]=0; co--;
    iSearch(val+1);
}
int main()
{
    freopen("C-small-attempt3.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
	scanf("%d",&T);
	int tt=0;
	for(i=1;i<=20;i++)
        for(j=1;j<=20;j++)
            for(k=1;k<=20;k++)
                dp[i][j][k]=11111;
    while(T--)
    {
        sum=0;
        tt++;
        scanf("%d%d%d",&N,&M,&K);
        //memset(tb,0,sizeof tb);
        X=N*M;
        Mc=11111;
        co=0;
        if(dp[N][M][K]==11111)
            iSearch(0);
        printf("Case #%d: %d\n",tt,dp[N][M][K]);
    }
}
