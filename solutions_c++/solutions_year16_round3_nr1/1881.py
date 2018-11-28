#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <utility>
#include <functional>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <deque>
 
using namespace std;
 
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define mp make_pair
#define all(r) r.begin(),r.end()
#define rall(r) r.rbegin(),r.rend()
#define fi first
#define se second
#define println(X) cout<<X<<endl;
#define DBG(X) cout<<#X<<" : "<<X<<endl;
 
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<vl> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;


const int INF = 1e9;

double EPS = 1e-10;



int main(){
	int mCase;
	scanf("%d", &mCase);
	int n;
	
	for(int Case = 1; Case <= mCase; Case++){
		cin>>n;
		vi v(n);
		rep(i, n) cin>>v[i];
		vector<pii> p(n);
		rep(i, n){
			p[i].se = i;
			p[i].fi = v[i];
		}
		int sum = 0;
		rep(i, n) sum += v[i];
		sort(rall(p));

		vector<string> ans;
		if(sum%2==1){
			ans.pb(string());
			ans.back()+=('A'+p[0].se);
			p[0].fi--;
			sum--;
		}
		while(sum > 0){
			ans.pb(string());
			sort(rall(p));
			ans.back()+=('A'+p[0].se);
			p[0].fi--;
			sum--;
			sort(rall(p));
			ans.back()+=('A'+p[0].se);
			p[0].fi--;
			sum--;
		}

		printf("Case #%d:", Case);
		rep(i, ans.size()) printf(" %s", ans[i].c_str());
		printf("\n");
	}
}