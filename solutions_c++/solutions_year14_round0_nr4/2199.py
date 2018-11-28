#include <iostream>
#include <algorithm>
using namespace std;

const int MAXn = 1000 + 10;
int n;
int ans1, ans2;
double ar1[MAXn], ar2[MAXn];

inline void solve()
{
	cin >> n;
	for(int i=0; i<n; ++i)
		cin >> ar1[i];
	for(int i=0; i<n; ++i)
		cin >> ar2[i];

	sort(ar1, ar1+n);
	sort(ar2, ar2+n);

	ans1 = 0;
	int p1 = n-1, p2 = 0;
	for(int i=n-1; i>=0; --i)
		if(ar1[i] < ar2[p1])
			--p1;
		else {
			++p2;
			++ans1;
		}

	ans2 = 0;
	p1 = n-1, p2 = 0;
	for(int i=0; i<n; ++i)
		if(ar1[i] > ar2[p2]) {
			++p2;
			++ans2;
		}
		else
			--p1;
}

int main()
{
	int nt;
	cin >> nt;
	for(int i=1; i<=nt; ++i) {
		solve();
		cout << "Case #" << i << ": " << ans2 << ' ' << ans1 << endl;
	}

	return 0;
}
