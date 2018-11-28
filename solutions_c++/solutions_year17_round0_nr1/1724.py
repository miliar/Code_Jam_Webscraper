#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back

mt19937 rnd;

inline int rndInt (int x) {
	return rnd () % x;
}

/*inline int R (int l, int r) {
	return l + rndInt (r - l + 1);
}*/

char Cur;

inline char getChar () {
	char t = Cur;
	Cur = getchar ();
	return t;
}

template<class telem> void readInt (telem &a) {
	a = 0;
	while (!isdigit (Cur)) getChar ();
	while (isdigit (Cur)) {
		a *= 10;
		a += getChar () - '0';
	}
}  	

int T = 1;
string s;
int k;
int tc;
int add[1111];

void pre () {
}

void load () {
	cin >> s >> k;
}

void solve () {
	tc++;
	cout << "Case #" << tc << ": ";
	int ans = 0;
	int n = (int) s.size ();
	fill (add, add + n, 0);
	for (int i = 0, j = 0; i < n; i++) {
		j += add[i];
		int t = (s[i] == '-') ? 1 : 0;
		t ^= (j & 1);
		if (t) {
			if (i + k > n) {
				cout << "IMPOSSIBLE\n";
				return;
			}
			ans++;
			j++;
			add[i + k]--;
		}
	}
	cout << ans << '\n';                     
}   	
   
int main () {
	ios_base::sync_with_stdio (false);
	cin.tie (0);
	pre ();
#ifdef LOCAL
	auto ___ = freopen ("file.in", "r", stdin);
	___ = freopen ("file.out", "w", stdout);
	assert (___);
#endif

	double st = clock ();

	cin >> T;
             
	while (T --> 0) {	
		load ();  
		solve ();
	}

	clog << (clock () - st) / CLOCKS_PER_SEC << endl;

	return 0;
}