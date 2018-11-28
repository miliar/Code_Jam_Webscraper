#include <bits/stdc++.h>

#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif

#define all(v)          v.begin(),v.end()
#define allr(v)         v.rbegin(),v.rend()
#define rep(i,m)        for(int i=0;i<(int)m;i++)
#define REP(i,k,m)      for(int i=k;i<(int)m;i++)
#define mem(a,b)        memset(a,b,sizeof(a))
#define mp              make_pair
#define pb              push_back
#define X real()
#define Y imag()

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef complex<long double> point;

int diri[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
int dirj[] = { 0, 1, 0, -1, 1, 1, -1, -1 };

int compare(double d1, double d2) {
	if (fabs(d1 - d2) < 1e-9)
		return 0;
	if (d1 < d2)
		return -1;
	return 1;
}
#define OO ((int)1e9)
#define MAX 1000001
#define MOD 1000000009

int main() {
	std::ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("1.in", "r", stdin);
//	freopen("A.in", "r", stdin);
	freopen("ans.txt", "w", stdout);
#endif
	int t, r, k, ii = 1;
	cin >> t;
	while (t--) {
		cerr << ii << endl;
		printf("Case #%d: ", ii++);
		map<int, int> cnt;
		rep(l,2)
		{
			cin >> r;
			r--;
			rep(i,4)
			{
				rep(j,4)
				{
					cin >> k;
					if (i == r) {
						cnt[k]++;
					}
				}
			}
		}
		vector<pair<int, int> > v(all(cnt));
		vector<int> a;
		rep(i,v.size())
		{
			if (v[i].second == 2)
				a.push_back(v[i].first);
		}
		if (a.size() == 0) {
			printf("Volunteer cheated!\n");
		} else if (a.size() == 1) {
			printf("%d\n", a[0]);
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}
//end

