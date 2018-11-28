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

int main()
{
  ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);
  freopen("A-small-attempt1.in","r",stdin);
  freopen("out.txt","w",stdout);
  int test,x = 0;
  cin >> test;
  while(test--){
    x++;
    int w,r,c,ans=0;
    cin >> r >> c >> w ;
    if(c%w!=0)ans = 1;
    cout <<"Case #"<<x << ": " <<c/w +ans+ w-1 <<endl;
  }
  return 0;
}
