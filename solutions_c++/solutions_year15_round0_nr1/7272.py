#include <bits/stdc++.h>

#define sz(a) int((a).size())
#define tr(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(),(c).end()
#define uniq(c) sort(all((c))); (c).resize(unique(all((c))) - (c).begin())
#define lobo(c, x) (int) (lower_bound(all((c)), (x)) - (c).begin())
#define upbo(c, x) (int) (upper_bound(all((c)), (x)) - (c).begin())
#define R(i,a,b) for (int i=a; i<=b; i++)
#define stop getchar();
#define tess puts("===========");
#define tes(a) cerr<<#a << " = "<<a<<endl;
#define cincout ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);

#define INF 1000111222
#define EPS  1e-9
#define pb  push_back
#define mp  make_pair

#define fi  first
#define se  second
#define X   first
#define Y   second

using namespace std;

typedef pair<int,int> 	ii;
typedef long long 	 int64;

int T;
string s;

int main () {
	cincout;
	cin >> T;
	R(tc,1,T) {
		int ans = 0;
		int tmp = 0;
		cin >> s >> s;
		R(i,0,sz(s)-1) {
			if (tmp >= i) 
				tmp += s[i] - '0';
			else {
				ans += i-tmp;
				tmp  = i+s[i] - '0';
			}
		}
		cout << "Case #"<<tc<<": "<<ans<<"\n";
	}
}
