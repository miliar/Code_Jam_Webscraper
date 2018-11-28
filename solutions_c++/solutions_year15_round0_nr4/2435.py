#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fore(i,n) for(int i = 0; i< n ; i++ )
#define lop(i,n) for(int i = 1 ; i<=n ; i++ )
#define ops(i,n) for(int  i = n-1 ; i>=0 ; i-- )
#define	forall( it,g )	for( typeof(g.begin()) it=g.begin();it!=g.end();it++ )
#define PI  3.141592653589793
#define mod  1000000007
#define inf 1000000000000
#define INF -1000000000
#define modulo 1073741824
#define MH 1234533333333337
//ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);
using namespace std;
typedef vector <int > vi;
typedef vector <vector <int> > vv;
typedef vector <pair <int,int > >vp;
typedef vector <vector <pair <int ,int > > > vvp;
typedef vector <pair <int ,pair <int ,int > > > vpp;
typedef pair<int,int> pp;
typedef long long ll;
int grid[4][16] = {{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1} ,
{0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1},
{0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0},
{0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1}};
int main()
{
  ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);
  freopen("out.txt","w",stdout);
  freopen("D-small-attempt1.in","r",stdin);
  int test,g = 0;
  cin >> test ;
  while(test--){
    g++;
    int x,r,c;
    cin >> x >> r >> c ;
    string s ;
    if(grid[x-1][r*c-1])s = "GABRIEL";
    else s = "RICHARD";
    cout <<"Case #"<< g <<": "<< s <<endl;
  }
  return 0;
}

