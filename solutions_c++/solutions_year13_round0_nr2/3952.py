#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<double>vd;
typedef vector<string> vs;
typedef vector<vi>vvi;
typedef map<string,int> msi;
typedef map<int,int>mii;
typedef map<pii,int>mpi;

#define pb push_back
#define MP make_pair
#define popb pop_back
#define all(a) a.begin(), a.end()
#define Sort(x) sort(x.begin(),x.end())
#define Reverse(x) reverse(x.begin(),x.end())
#define SZ(a) ( (int)a.size() )
#define mem(a, b) memset(a, b, sizeof(a))

#define REP(i,n) for (i=0;i<n;i++)
#define REV(i,n) for (i=n;i>=0;i--)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define FOR(i,p,k) for (i=p; i<k;i++)

#define COPY(c,r)   memcpy(c,r,sizeof(r))
#define popcount(i) __builtin_popcount(i)
#define fs first
#define sc second

/// Moves ///
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[] = {-2, 2, -1, 1, -1, 1};int dy[] = {0, 0, 1, 1, -1, -1}; //Hexagonal Moves

/// Cycles ///
//#define cycl0 0
//#define cycl1 1
//#define cycl5 5
//#define cycl6 6
//int cycl2[] = {1, 2, 4, 8, 6};
//int cycl3[] = {1, 3, 9, 7, 1};
//int cycl4[] = {1, 4, 6};
//int cycl7[] = {1, 7, 9, 3, 1};
//int cycl8[] = {1, 8, 4, 2, 6};
//int cycl9[] = {1, 9, 1};

#define INF 1<<30

int arr[101][101];
int n, m;

bool check(void);
bool check_cell(int i, int j);

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;

    cin>>t;
    for (int cas=1; cas<=t; cas++)
    {
        cin>>n>>m;
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
            {
                cin>>arr[i][j];
            }
        }
        if (check()) printf ("Case #%d: YES\n", cas);
        else printf ("Case #%d: NO\n", cas);
    }
	return 0;
}

bool check(void)
{
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<m; j++)
        {
            if (check_cell(i, j)==false) return false;
        }
    }
    return true;
}

bool check_cell(int i, int j)
{
    bool r=true, c=true;
    for (int k=0; k<m; k++)
        if (arr[i][k]>arr[i][j]) { r = false; break; }
    for (int k=0; k<n; k++)
    if (arr[k][j]>arr[i][j]) { c = false; break; }
    return r|c;
}
