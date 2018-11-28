#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define mk make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,int> ii;

int main(void) {
	int t; cin >> t;

	For(c,1,t+1) {
		string s; cin >> s;
		string ans;

		ans += s[0];
		for (int i = 1; i < s.size(); i++) {
			string aux;
			if (s[i] >= ans[0]) {
				aux += s[i];
				aux += ans;
				ans = aux;
			} else {
				ans += s[i];
			}	
		}
	
		printf("Case #%d: ", c);
		cout << ans << endl;
	}	



	return 0;
}
