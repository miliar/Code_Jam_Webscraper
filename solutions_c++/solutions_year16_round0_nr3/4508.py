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

llint get2toScale(llint num, int sc){
	llint ans = 0;
	llint deg = 1;
	while (num){
		ans += (num % 2)*deg;
		deg *= sc;
		num /= 2;
	}

	return ans;
}

int check_prime(llint num){
	for (llint i = 2; i*i <= num; ++i){
		if (num % i == 0)
			return i;
	}
	return 1;
}

vector<pair<int, vector<int>>> ans;

string get2scale(llint num){
	string s = "";
	while (num){
		s = (num % 2 ? "1" : "0") + s;
		num /= 2;
	}
	return s;
}

void task(){
	int t;
	cin >> t;
	for (int i = 1; i < t + 1; ++i){
		int n, j;
		cin >> n >> j;
		for (int mask = 0; mask < (1 << (n - 2)); ++mask){
			bool ok = 1;
			vector<int> tans ;
			llint num2 = (1 << (n - 1))| (mask << 1)| 1;
			for (int i = 2; i <= 10; ++i){
				int pr = check_prime(get2toScale(num2, i));
				if (pr == 1){
					ok = 0;
					break;
				}
				tans.push_back(pr);
			}
			if (ok){
				ans.push_back({num2, tans});
			}
			if (ans.size() == j)
				break;
		}
		cout << "Case #" << i << ":\n";
		for (auto x: ans){
			cout << get2scale(x.first) << ' ';
			for (auto y: x.second){
				cout << y << ' ';
			}
			cout << endl;
		}
	}
}
