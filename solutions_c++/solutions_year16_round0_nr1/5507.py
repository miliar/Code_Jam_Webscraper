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

bool a[10];

bool check(){
	for (int i = 0; i < 10; ++i)
		if (!a[i])
			return 0;
	return 1;
}

void mark(llint n){
	while (n){
		a[n % 10] = 1;
		n /= 10;
	}
}

void task(){
	int t;
	cin >> t;
	for (int i = 1; i < t + 1; ++i){
		int num;
		cin >> num;
		memset(a, 0, sizeof(a));
		if (num == 0){
			cout << "Case #" << i << ": INSOMNIA\n";
			continue;
		}
		int it = 0;
		for (int k = 0; k < (int)1e6 && !check(); ++k){
			++it;
			mark((llint)num*it);
		}
		cout << "Case #" << i << ": " << (llint)num*it << "\n";
	}
}
