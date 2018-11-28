#include <bits/stdc++.h>
using namespace std;
#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define endl "\n"
#define sync ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define clean(a) memset((a),0,sizeof (a))
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)
typedef pair<int,int> pii;
typedef long long ll;
const int N = 200005;
const int MAX = 1000000007;
const double EPS = 0.000001;
//cout << fixed << setprecision(10);

int n;
int t;
string s;
map<char, int> ma;
vector<int> ans;
int main() {
	fin("A.in");
	fout("A.out");
	sync;
	cin >> t;
	int k;
	for(int q = 0;q<t;q++) {
		cin >> s;
		ma.clear();
		ans.clear();
		for(int i = 0;i<(int)s.length();i++)
			ma[s[i]]++;
		k = ma['Z'];
		for(int i = 0;i<k;i++)
			ans.pb(0);
		ma['Z'] = 0;
		ma['E'] -= k;
		ma['R'] -= k;
		ma['O'] -= k;
		k = ma['W'];
		for(int i = 0;i<k;i++)
			ans.pb(2);
		ma['T'] -= k;
		ma['W'] = 0;
		ma['O'] -= k;
		k = ma['U'];
		for(int i = 0;i<k;i++)
			ans.pb(4);
		ma['F'] -= k;
		ma['O'] -= k;
		ma['U'] = 0;
		ma['R'] -= k;
		k = ma['X'];
		for(int i = 0;i<k;i++)
			ans.pb(6);
		ma['S'] -= k;
		ma['I'] -= k;
		ma['X'] = 0;
		k = ma['G'];
		for(int i = 0;i<k;i++)
			ans.pb(8);
		ma['E'] -= k;
		ma['I'] -= k;
		ma['G'] = 0;
		ma['H'] -= k;
		ma['T'] -= k;
		k = ma['R'];
		for(int i = 0;i<k;i++)
			ans.pb(3);
		ma['T'] -= k;
		ma['H'] -= k;
		ma['R'] = 0;
		ma['E'] -= 2*k;
		k = ma['F'];
		for(int i = 0;i<k;i++)
			ans.pb(5);
		ma['F'] = 0;
		ma['I'] -= k;
		ma['V'] -= k;
		ma['E'] -= k;
		k = ma['V'];
		for(int i = 0;i<k;i++)
			ans.pb(7);
		ma['S'] -= k;
		ma['E'] -= k;
		ma['V'] = 0;
		ma['E'] -= k;
		ma['N'] -= k;
		k = ma['I'];
		for(int i = 0;i<k;i++)
			ans.pb(9);
		ma['N'] -= 2*k;
		ma['I'] = 0;
		ma['E'] -= k;
		k = ma['O'];
		for(int i = 0;i<k;i++)
			ans.pb(1);
		sort(ans.begin(),ans.end());
		cout << "Case #" << q + 1 << ": ";
		for(int i = 0;i<(int)ans.size();i++)
			cout << ans[i];
		cout << endl;
	}
	return 0;
}
