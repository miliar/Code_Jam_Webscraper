#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <fstream>

using namespace std;

#define fst first
#define snd second
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double

template<typename T>
T abs(T x) {
	return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
	return x * x;
}

template<typename T>
ostream& operator << (ostream &s, const vector<T> &x) {
	s << "[";
	for (auto it : x) {
		s << it << ", ";
	}
	s << "]";
	return s;
}

template<typename T>
ostream& operator << (ostream &s, const set<T> &x) {
	s << "{";
	for (auto it : x) {
		s << it << ", ";
	}
	s << "}";
	return s;
}


template<typename U, typename V>
ostream& operator << (ostream &s, const pair<U, V> &x) {
	s << "(" << x.fst << ", " << x.snd << ")";
	return s;
}

template<typename T>
bool chmax(T &x, const T &y) {
	if (x < y) {
		x = y;
		return true;
	}
	return false;
}

template<typename T>
bool chmin(T &x, const T &y) {
	if (x > y) {
		x = y;
		return true;
	}
	return false;
}

//---------------------------------------------------------------------

const int maxn = 203;
ld dp[maxn][maxn], dp2[maxn][maxn];
ld a[maxn];

int main() {
	srand(time(NULL));
	#ifdef LOCAL
		//gen();
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
	#else
		//freopen("springs.in", "r", stdin);
		//freopen("springs.out", "w", stdout);
	#endif
	//check();
	
	int T;
	cin >> T;
	
	for (int iter = 1; iter <= T; iter++)
	{
		cout << "Case #" << iter << ": ";
		
		int n, k;
		cin >> n >> k;
		for (int i = 1; i <= n; i++)
			cin >> a[i];
		sort(a + 1, a + n + 1);
		for (int i = 0; i <= n + 1; i++)
			for (int j = 0; j <= n; j++)
				dp[i][j] = 0;
		dp[0][0] = 1;
		for (int i = 1; i <= n; i++)
			for (int j = 0; j <= n; j++)
			{
				dp[i][j] = 0;
				if (j > 0)
					dp[i][j] += dp[i-1][j-1] * a[i];
				dp[i][j] += dp[i-1][j] * (1 - a[i]);
			}
		
		for (int i = 0; i <= n + 1; i++)
			for (int j = 0; j <= n; j++)
				dp2[i][j] = 0;
		
		dp2[n+1][0] = 1;
		for (int i = n; i >= 1; i--)
			for (int j = 0; j <= n; j++)
			{
				dp2[i][j] = 0;
				if (j > 0)
					dp2[i][j] += dp2[i+1][j-1] * a[i];
				dp2[i][j] += dp2[i+1][j] * (1 - a[i]);
			}
		
		//cout << dp[2][0] << " " << dp2[3][2] << "\n";
		
		ld ans = 0;
		for (int i = 0; i <= k; i++)
		{
			int ost = k - i;
			ld curans = 0;
			for (int j = 0; j <= i; j++)
			{
				if (j > k / 2)
					continue;
				//cout << n - ost + 1 << " " << j << " " << dp[i][j] << " " << dp2[n-ost+1][k/2-j] << "\n";
				curans += dp[i][j] * dp2[n - ost + 1][k / 2 - j];
			}
			ans = max(ans, curans);
		}
		
		cout.precision(9);
		cout << fixed << ans << "\n";
	}
	
	return 0;
}
