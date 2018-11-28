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


int solve(string s) {
	int ans = 0;
	for (int i = (int)s.size() - 1; i >= 0; i--) {
		if (s[i] == '-') {
			ans++;
			for (int j = 0; j <= i; j++)
				s[j] = (s[j] == '-' ? '+' : '-');
		}
	}
	return ans;
	
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
		string s;
		cin >> s;
		cout << "Case #" << tq << ": " << solve(s) << endl;
	}
		
    return 0;
}   