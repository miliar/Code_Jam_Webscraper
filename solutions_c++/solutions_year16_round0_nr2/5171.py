#include <bits/stdc++.h>
#include <utility>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const ll BASE = 10007;
const int MAXN = 100005;

#define filla(a, x) memset(a, x, sizeof(a))
#define rep(i, n) for (int i = 0, sz = (n); i < sz; ++i)
#define foru(i, l, r) for (int i = (l); i <= (r); ++i)
#define ford(i, r, l) for (int i = (r); i >= (l); --i)
#define pb push_back
#define fs first
#define sc second


int read()
{
	int x;
	scanf("%d", &x);
	return x;
}

int main()
{
	#ifdef DEBUG
		freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);
	#endif
	int ntest = read();
	for (int i = 1; i <= ntest; ++i) {
		char s[1000];
		scanf("%s", s);
		int sz = strlen(s);
		// cout << s << " " << sz << " ";
		s[sz] = '+';
		int cnt = 0;
		for (int j = 0; j < sz; ++j)
			if (s[j] != s[j+1])
				cnt++;
		cout << "Case #"<< i <<": " << cnt;
		if (i < ntest)
			cout << "\n";
	}
	return 0;
}