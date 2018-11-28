#include <bits/stdc++.h>
using namespace std;

#ifdef WIN32
    #define lld "%I64d"
#else
    #define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;

const int M = 1e6 + 15;
const int Q = 1e9 + 7;


string solve(int n) {
	bool used[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	for (int i = 1; i <= 1e6; i++) {
		ll x = i * n;
		while (x) {
			used[x % 10] = true;
			x /= 10;
		}
		bool ok = true;
		for (int j = 0; j < 10; j++)
			if (!used[j]) ok = false;
		if (ok) {
			char buf[100];
			itoa(i * n, buf, 10);
			return string(buf);
		}
		
	}
	return "INSOMNIA";
	
}

int main(){
    srand(time(NULL));
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int tq = 1; tq <= T; tq++) {
		int n;
		cin >> n;
		cout << "Case #" << tq << ": " << solve(n) << endl;
	}
		
    return 0;
}   