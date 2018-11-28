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

const int M = 10;
const int Q = 1e9 + 7;


int a[M][M], b[M][M];
int aa[M][M];
bool used[M];
int ans;

bool gen2(int pos, int n) {
	if (pos == n)
		return true;
	bool ok = false;
	for (int i = 0; i < n; i++) {
		if (!b[pos][i]) continue;
		if (used[i]) continue;
		ok = true;
		used[i] = true;
		if (!gen2(pos + 1, n)) return false;
		used[i] = false;
	}
	if (!ok)
		return false;
	return true;
}

void pr(int n) {
	for (int i = 0; i < n ;i++)    {
		for (int j = 0; j < n; j++)
			cout << a[i][j];
		cout << endl;
	}	
}
void gen(int n, int mask) {
	int cost = 0;
	//cout << mask << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {	
			int tmp = mask & 1;
			if (tmp < a[i][j])
				return;
			cost += tmp - a[i][j];
			a[i][j] = tmp;
			mask >>= 1;
		}
	}
	int p[10];
	for (int i = 0; i < n; i++)
		p[i] = i;
	do{
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)
				b[i][j] = a[p[i]][j];
		}
		for (int i = 0; i < n; i++)
			used[i] = false;
		bool ok = gen2(0, n);
		if (!ok)
			return;
	}while (next_permutation(p, p + n));
//	if (cost == 3) {
//		pr(n);
//		cout << mask << endl;
//	}	
	ans = min(ans, cost);
		

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
	for (int it = 1; it <= T; it++) {
		int n;
		cin >> n;
		for(int i = 0; i < n; i++) {
			string s;
			cin >> s;
			for (int j = 0; j < n; j++)
				aa[i][j] = s[j] - '0';
		}
		ans = Q;
		for (int mask = 0; mask < (1 << (n * n)); mask++) {
			for (int i =0; i < n; i++)
				for (int j = 0;j < n; j++)
					a[i][j] = aa[i][j];
			gen(n, mask);
		}	
		printf("Case #%d: %d\n", it, ans);
	}
		
    return 0;
}   