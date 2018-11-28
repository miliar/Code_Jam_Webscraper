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

int n,ans;
string s;
char c;
int r;

int prove() {
	int i = s.length() - 1;
	while(i >= 0 && s[i] == '+')
		i--;
	return i;
}

void minu() {
	int i = r;
	
	for(int j = 0;j<=(i >> 1);j++) {
		c = s[i - j];
		if (s[j] == '+')
			s[i - j] = '-';
			else s[i - j] = '+';
		if (c == '+')
			s[j] = '-';
			else s[j] = '+';
	}
}

void plu() {
	int i = r;
	while(s[i] != '+')
		i--;
		
	for(int j = 0;j<=(i >> 1);j++) {
		c = s[i - j];
		if (s[j] == '+')
			s[i - j] = '-';
			else s[i - j] = '+';
		if (c == '+')
			s[j] = '-';
			else s[j] = '+';
	}
}

int main() {
//	fin("B-small.in");
	fin("B-large.in");
	fout("B-large.out");
	sync;
	int t;
	cin >> t;
	for(int q = 1;q<=t;q++) {
		cin >> s;
		ans = 0;
		while (true) {
			r = prove();
			if (r == -1)
				break;
				
			ans++;
			if (s[0] == '+')
				plu();
				else minu();
		}
		cout << "Case #" << q << ": " << ans << endl;
	}

	return 0;
}
