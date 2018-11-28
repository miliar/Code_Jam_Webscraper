#include <bits/stdc++.h>

using namespace std;

void task();

int main() {
#ifdef LUNAWYLL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	 //freopen("input.txt", "r", stdin);
	// freopen("output.txt", "w", stdout);
#endif
	task();
#ifdef LUNAWYLL
	//cout << "\n============\n" <<(double)clock()/CLOCKS_PER_SEC;
#endif
	return 0;
}

#ifdef LUNAWYLL
#define dbg(x) cout << #x << " = " << (x) << endl;
#define dbg2(a, b) cout << #a << " = " << (a) << "; "<<\
#b << " = " << (b) << endl;
#define dbg3(a, b, c) cout << #a << " = " << (a) << "; "<<\
		#b << " = " << (b) << "; "<<\
#c << " = " << (c) << endl;
#else
#define dbg(...) (void(1));
#define dbg2(...) (void(1));
#define dbg3(...) (void(1));
#endif

typedef long long int llint;
typedef vector<int> vi;
typedef pair<int, int> pii;
#define all(v) v.begin(), v.end()

const int N = (int)3e5 + 10;
const llint MOD = (llint)1e9 + 7;
const int INF = (int)1e9 + 10;
const llint LINF = (llint)8e18 + 100;
const int BUF_SIZE = (int)1e6 + 10;

string s;
int ans;

void rev(int ind){
	string ts = "";
	for (int i = ind - 1; i >= 0; --i){
		ts += s[i] == '+' ? '-' : '+';
	}
	s = ts + s.substr(ind);
	++ans;
}

void task(){
	int t;
	cin >> t;
	for (int i = 1; i < t + 1; ++i){
		cin >> s;
		ans = 0;
		while (true){
			int ind = s.find_last_of('-');
			if (ind == -1)
				break;
			if (s[0] == '+')
				rev(s.find_first_of('-'));
			if (s[ind] == '+')
				break;
			rev(ind + 1);
		}
		cout << "Case #" << i << ": " << ans << "\n";
	}
}
