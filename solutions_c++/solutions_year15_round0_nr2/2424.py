#include <bits/stdc++.h>
#include <limits>
using namespace std;

 
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef long double ld;
#define var(a,b) __typeof(b) a = b
#define rep(i,n) for(int i = 0;(i) < (n); ++i)
#define rept(i,a,b) for(var(i,a); i < (b); ++i)
#define tr(v,it) for(var(it,v.begin());it!=v.end();++it)
#define fill(a,val) memset(a,val,sizeof(a))
#define all(v) v.begin(),v.end()


int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int t;
	cin >>	t;
	rep(l,t){
		int D;
		cin >> D;
		vector<int > v(D);

		rep(i, D){
			cin >> v[i];
		}
		sort(v.begin(), v.end(), greater<int>());
		// cout << v[0] << endl;
		int val = 0;
		int ans = INFINITY;

		for(int i = 1; i <= v[0]; i++){
			val = 0;
			for(int j = 0; j < D; j++){
				if(v[j] <= i){
					break;
				}
				val += ceil(float(v[j])/float(i)) - 1;
			}
			if(val + i < ans)
				ans = val + i;
		}
		cout << "Case #" << l + 1  << ": " << ans << endl;
	}

	return 0;
}