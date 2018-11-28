#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

#define nln        puts("")                         /// print newline
#define Max(a,b,c) max(a,max(b,c))                  ///3 ta theke max
#define Min(a,b,c) min(a,min(b,c))                  ///3 ta theke min

#define FOR1(i,n)  for(i=1;i<=n;i++)
#define FOR0(i,n)  for(i=0;i<n;i++)                 ///looping
#define FORR(i,n)  for(i=n-1;i>=0;i--)
#define ALL(p)     p.begin(),p.end()

#define SET(p)     memset(p, -1, sizeof(p))
#define CLR(p)     memset(p, 0, sizeof(p))          ///memset
#define MEM(p,v)   memset(p, v, sizeof(p))

#define READ(f)    freopen(f, "r", stdin)           /// file
#define WRITE(f)   freopen(f, "w", stdout)

#define SZ(c)      (int)c.size()
#define PB(x)      push_back(x)                     ///STL defines
#define MP(x,y)    make_pair(x,y)
#define ff         first
#define ss         second

#define i64        long long int
#define f64        long double
#define PI         acos(-1.0)                        ///PI er value

const double EPS = 1e-9;                        ///constatnts
const int INF = 0x7f7f7f7f;

int dr8[8]= {1,-1,0,0,1,-1,-1,1};            ///8 direction move
int dc8[8]= {0,0,-1,1,1,1,-1,-1};
int dr4[4]= {0,0,1,-1};                      ///4 direction move
int dc4[4]= {-1,1,0,0};                      ///or adjacent dir.
int board[105][105];
bool board2[105][105];
int main()
{
	READ("input.txt");
	WRITE("output.txt");
	int kase,i,j,t=1,r,c,n,m;
	cin>>kase;
	while(kase--)
    {
        cin>>n>>m;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
                scanf("%d",&board[i][j]);
        }

        MEM(board2,false);

        for(i=1;i<=n;i++)
        {
            int mx=1;
            for(j=1;j<=m;j++)
            {
                if(mx<board[i][j])
                    mx=board[i][j];
            }

            for(j=1;j<=m;j++)
            {
                if(mx==board[i][j])
                    board2[i][j]=true;
            }
        }

        for(i=1;i<=m;i++)
        {
            int mx=0;
            for(j=1;j<=n;j++)
                if(mx<board[j][i])
                mx=board[j][i];

            for(j=1;j<=n;j++)
                if(mx==board[j][i])
                board2[j][i]=true;
        }

        bool ok=true;;

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++){
                //cout<<board2[i][j];
                //nln;
                if(board2[i][j])
                {
                    ok=true;
                    continue;
                }
                else
                {
                    ok=false;
                    break;
                }
            }
            if(!ok)break;
        }
        cout<<"Case #"<<t++<<": ";
        if(ok)puts("YES");
        else puts("NO");
    }
	return 0;
}



//knapsack Item print http://codepad.org/CDN8Aum3



