#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define	For(i,a,b)				for(int i=(a);i<(b);++i)
#define	rep(i,n)				For(i,0,(n))
#define	all(v)					(v).begin(),(v).end()


int calc(vector<int> pi, int limpan)
{
	int special = 0;
	int maxpan = 0;

	rep(i, pi.size()) {
		int tmp = pi[i];
		while(tmp > limpan) {
			maxpan = max(maxpan, limpan);
			++special;
			tmp -= limpan;
		}
		maxpan = max(maxpan, tmp);
	}
	return special + maxpan;
}

int solve()
{
	int D;
	cin >> D;
	vector<int> Pi(D);

	rep(i, D)
		cin >> Pi[i];

	int maxpan = *max_element(all(Pi));
	int res = maxpan;
	For(i, 1, maxpan)
		res = min(res, calc(Pi, i));
	return res;
}

int main()
{
	int T;
	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}
