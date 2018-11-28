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
	int n;//, p;
	ll ans, t;
	set<int> st;
	for(int Case = 1; Case <= mCase; Case++){
		scanf("%d", &n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n", Case);
			continue;
		}
		//p = 1;
		st.clear();
		ans = (ll)n;
		while(1){
			t = ans;
			while(t>0LL){
				st.insert(t%10LL);
				t/=10LL;
			}
			if(st.size()>=10){
				break;
			}
			ans += n;
		}
		printf("Case #%d: %lld\n", Case, ans);
	}
}