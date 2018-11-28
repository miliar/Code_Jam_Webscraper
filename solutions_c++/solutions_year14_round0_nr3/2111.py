#include <bits/stdc++.h>

#define REP(i, a) for( int i = 0; i < a; i++ )
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define ITFOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define VE vector <int>
#define mset(A,x) memset(A, x, sizeof A)
#define PB push_back
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; REP(i,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; REP(i,m)REP(j,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define LSOne(S) (S&(-S))

using namespace std;

#define ll long long
#define lli long long int
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i 1<<30-1

int test,f,c,m,tot;
int grid[50][50];
int dx[]={-1,-1,-1,0,0,1,1,1};
int dy[]={-1,0,1,-1,1,-1,0,1};

bool check(int x,int y)
{
    if(x==-1 || x==f || y==-1 || y==c)
        return false;
    return true;
}

void dfs(int x,int y)
{
    if(grid[x][y])
        return ;
    grid[x][y]=-2;
    REP(i,8)
        if(check(x+dx[i],y+dy[i]) && grid[x+dx[i]][y+dy[i]]!=-1)
        {
            if(grid[x+dx[i]][y+dy[i]])
                grid[x+dx[i]][y+dy[i]]=-2;
            dfs(x+dx[i],y+dy[i]);
        }
}

int main(){
/*
   freopen("C-small-attempt4.in", "r", stdin);
   freopen("out.txt", "w", stdout);
*/
    scanf("%d",&test);
    REP(t,test)
    {
        scanf("%d %d %d",&f,&c,&m);
        printf("Case #%d:\n",t+1);
        tot=f*c;
        bool flag=false;
        REP(mask,(1<<tot))
        {
            int cnt=__builtin_popcount(mask);
            if(cnt==m)
            {
                //cout<<"entro: "<<mask<<endl;
                int x,y;
                mset(grid,0);
                REP(i,tot)
                {
                    if(mask&(1<<i))
                    {
                        x=i/c;
                        y=i%c;
                        grid[x][y]=-1;
                        REP(i,8)
                        {
                            if(check(x+dx[i],y+dy[i]) && grid[x+dx[i]][y+dy[i]]!=-1)
                                grid[x+dx[i]][y+dy[i]]++;
                        }
                    }
                }

                bool band=false;
                int xc,yc;
                REP(i,f)
                {
                    REP(j,c)
                    {
                        if(grid[i][j]==0)
                            dfs(i,j),band=true,xc=i,yc=j;
                        if(band)
                            break;
                    }
                    if(band)
                        break;
                }

                if(band)
                {
                    REP(i,f)
                    {
                        REP(j,c)
                        {
                            if(grid[i][j]==-1)
                                continue;
                            if(grid[i][j]!=-2)
                                band=false;
                            //cout<<grid[i][j];
                        }
                        //cout<<endl;
                    }
                    //cout<<mask<<endl;
                    if(band)
                    {
                        flag=true;
                        REP(i,f)
                        {
                            REP(j,c)
                            {
                                if(i==xc && j==yc)
                                    printf("c");
                                else if(grid[i][j]==-1)
                                    printf("*");
                                else
                                    printf(".");
                            }
                            printf("\n");
                        }
                    }
                }
                else
                {
                    REP(i,f)
                    {
                        REP(j,c)
                        {
                            if(grid[i][j])
                            {
                                int temp=grid[i][j];
                                grid[i][j]=-2;
                                xc=i,yc=j;
                                band=true;
                                REP(k,f)
                                {
                                    REP(l,c)
                                    {
                                        if(grid[k][l]==-1)
                                            continue;
                                        if(grid[k][l]!=-2)
                                            band=false;
                                        //cout<<grid[i][j];
                                    }
                                    //cout<<endl;
                                }
                                if(band)
                                {
                                    REP(k,f)
                                    {
                                        REP(l,c)
                                        {
                                            if(k==xc && l==yc)
                                                printf("c");
                                            else if(grid[k][l]==-1)
                                                printf("*");
                                            else
                                                printf(".");
                                            //cout<<grid[i][j];
                                        }
                                        printf("\n");
                                        //cout<<endl;
                                    }
                                    flag=true;
                                }

                                grid[i][j]=temp;
                                if(flag)
                                    break;
                            }
                            if(flag)
                                break;
                        }
                        if(flag)
                            break;
                    }
                }
            }
            if(flag)
                break;

        }
        if(flag==false)
            printf("Impossible\n");
    }
/*
    fclose(stdin);
    fclose(stdout);
*/
    return 0;

}

