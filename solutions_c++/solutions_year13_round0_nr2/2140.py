#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>

using namespace std;

#define Limit 100005
#define FRO freopen("in.txt","r",stdin);
#define FRU freopen("out.txt","w",stdout);

#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define i64 long long
//#deinfe i64 __int64
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define infinity 2147483647
#define pi acos(-1.0)
#define eps 1e-9



#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)


template< class T > T sqr(T n) { return n*n; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > T Max(T a, T b) { return a>b?a:b; }
template< class T > T Min(T a, T b) { return a<b?a:b; }
template< class T > T abs(T a) { return a>0?a:-a; }

//const int row[]={-1, -1, -1,  0,  0,  1,  1,  1};  // Kings Move
//const int col[]={-1,  0,  1, -1,  1, -1,  0,  1};  // Kings Move
//const int row[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int col[]={-1,  1, -2,  2, -2,  2, -1,  1};  // Knights Move
//const int row[]={-1,0,0,1,0};
//const int col[]={0,-1,1,0,0};

int n,m;
int grid[110][110];

bool check(int r,int c,int h)
{
    int i,j;
    i=r;
    while(i>0)
    {
        if(grid[i-1][c]<=h)i--;
        else break;
    }
    j=r;
    while(j<n+1)
    {
        if(grid[j+1][c]<=h)j++;
        else break;
    }
    if(i==0 && j==n+1)return true;


    i=c;
    while(i>0)
    {
        if(grid[r][i-1]<=h)i--;
        else break;
    }
    j=c;
    while(j<m+1)
    {
        if(grid[r][j+1]<=h)j++;
        else break;
    }
    if(i==0 && j==m+1)return true;

    return false;
}

int main()
{
   // FRO
   // FRU
    int tc,t,i,j,k,a,b,c,d;
    cin>>tc;
    for(t=1;t<=tc;t++)
    {
        cin>>n>>m;
        SET(grid);
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)cin>>grid[i][j];
        }
        int flg=0;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if(!check(i,j, grid[i][j] ))flg=1;
            }
        }
        if(flg)printf("Case #%d: NO\n",t);
        else printf("Case #%d: YES\n",t);
    }

    return 0;
}

