#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fore(i,n) for(int i = 0; i< n ; i++ )
#define lop(i,n) for(int i = 1 ; i<=n ; i++ )
#define ops(i,n) for(int  i = n-1 ; i>=0 ; i-- )
#define	forall( it,g )	for( typeof(g.begin()) it=g.begin();it!=g.end();it++ )
#define PI  3.141592653589793
#define mod  1000000007
#define inf 10000000000
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
  freopen("out.txt","w",stdout);
  freopen("A-large (1).in","r" ,stdin);
  int test ,x = 0;
  cin >> test ;
  while(test--){
    x++;
    int n ;
    cin >> n ;
    int a[n+5];
    fore(i , n)
      cin >> a[i];
    int mi = 0,ma = 0;
    fore(i , n-1)
      if(a[i+1]<a[i])
        mi+=a[i]-a[i+1];
    int g = 0;
    fore(i ,n-1)
      if(a[i+1]<a[i])
        g = max(g ,a[i]-a[i+1] );
    fore(i , n-1)
      ma+=min(g,a[i]);
    cout << "Case #" << x << ": " << mi << " " << ma <<endl;
  }
  return 0;
}
