/**À„∑®∑÷Œˆ£∫

*/
#include<bits/stdc++.h>
#define MAXN 55
#define PI acos(-1.0)
#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,s,t) for(int i=s; i<=t; i++)
#define mem(a,b)  memset(a,b,sizeof(a))
#define show(x) { cerr<<">>>"<<#x<<" = "<<x<<endl; }
#define show2(x,y) { cerr<<">>>"<<#x<<"="<<x<<"  "<<#y<<" = "<<y<<endl; }
using namespace std;

int main()
{
    freopen("E:\\acm\\input.txt","r",stdin);
    freopen("E:\\acm\\output.txt","w",stdout);

    int T; cin>>T;
    FOR(cas,1,T)
    {
        printf("Case #%d:\n",cas);
        char grid[MAXN][MAXN];
        int R,C,M,N; cin>>R>>C>>M;
        N = R*C - M;
        REP(i,R) REP(j,C) grid[i][j] = '*';

        bool isok = false;
        if(R == 1)
        {
            REP(i,N) grid[0][i] = '.';
            isok = true;
        }
        else if(C == 1)
        {
            REP(i,N) grid[i][0] = '.';
            isok = true;
        }
        else
        {
            // R > 2 && C > 2
            if(N == 1)
            {
                grid[0][0] = '*';
                isok = true;
            }
            else if(N >= 4)
            {
                FOR(k,2,R)
                {
                    if(k*C < N) continue;
                    int res = N - 2*k;
                    if(res < 0 || res == 1 || ( k==2 && res%k == 1)) continue;
                    REP(i,k) grid[i][0] = grid[i][1] = '.';

                    int j = res/k + 2;
                    if(res%k == 1)
                    {
                        REP(i,k) FOR(h,2,j-1) grid[i][h] = '.';
                        REP(i,res%k) grid[i][j] = '.';
                        grid[1][j] = '.';
                        grid[k-1][j-1] = '*';
                    }
                    else
                    {
                        REP(i,k) FOR(h,2,j-1) grid[i][h] = '.';
                        REP(i,res%k) grid[i][j] = '.';
                    }
                    isok = true;
                    break;
                }
            }
        }
        if(!isok) printf("Impossible\n");
        else
        {
            grid[0][0] = 'c';
            REP(i,R)
            {
                REP(j,C) printf("%c",grid[i][j]);
                printf("\n");
            }
        }
    }

}












