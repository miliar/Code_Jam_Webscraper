#include <bits/stdc++.h>
using namespace std;


#define Size(s) ((int)s.size())
#define rep(i, n) for(int i=0; i<n; ++i)
#define Foreach(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define F first
#define S second
#define X real()
#define Y imag()
#define MP make_pair

template<class P, class Q> inline bool mmin(P &a, Q b) { if (a > b){ a = b; return true;} return false;}
template<class P, class Q> inline bool mmax(P &a, Q b) { if (a < b){ a = b; return true;} return false;}

typedef long long LL;
typedef pair<int, int> pii;

const int MAXn = 100*1000;
int n, w;
int ar[MAXn];
bool mark[MAXn];

int main()
{
	ios_base::sync_with_stdio(false);

	int nq;
	cin >> nq;
	rep(ii, nq) {
		cin >> n >> w;
		rep(i, n)
			cin >> ar[i];
		sort(ar, ar+n);
		fill_n(mark, n, 0);

		int ans = 0;
		for(int i=n-1; i>=0; --i) {
			if(mark[i])
				continue;
			int cur = 0, kr=0;
			for(int j=i; j>=0 && kr<2; --j)
				if(!mark[j] && cur+ar[j]<=w) {
					mark[j] = true;
					cur += ar[j];
					++kr;
				}
			++ans;
		}

		cout << "Case #" << ii+1 << ": " << ans << endl;
	}

	return 0;
}
