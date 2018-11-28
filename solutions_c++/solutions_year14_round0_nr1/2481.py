#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <utility>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cstdlib>
#include <map>
using namespace std;
typedef long long int ll;
#define inf 1000000007
#define iit(n) scanf("%lld",&n)
#define oit(n) printf("%lld",n)
#define pb(n) push_back(n)
#define REP(i,j,n) for(i=j;i<n;i++)
#define READ(x) freopen(x, "r", stdin)
#define WRITE(x) freopen(x, "w", stdout)
#define mp make_pair
int main()
{
//  ios_base::sync_with_stdio(0);cin.tie(0);
	READ("input");
	WRITE("output.txt");
	int tc;
	cin>>tc;
	int cas=0;
	for(cas=1;cas<=tc;cas++) {
		ll n;
		cin>>n;
		ll i,j;
		set<ll> s;
		vector<vector<int> > v(4,vector<int> (4));
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				cin>>v[i][j];
				if(i==n-1) s.insert(v[i][j]);
			}
		}
		int m;
		cin>>m;
		ll ans=0,t;
		vector<vector<int> > a(4,vector<int> (4));
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				cin>>a[i][j];
				if(i==m-1) {
					if(s.find(a[i][j])!=s.end()) {
						ans++;
						t=(*s.find(a[i][j]));
					}
				}
			}
		}
		cout<<"Case #"<<cas<<": ";
		if(ans==1) {
			cout<<t<<"\n";
		} else if(ans>1) {
			cout<<"Bad magician!\n";
		} else if(ans==0) {
			cout<<"Volunteer cheated!\n";
		}
	}
	return 0;
}
		
