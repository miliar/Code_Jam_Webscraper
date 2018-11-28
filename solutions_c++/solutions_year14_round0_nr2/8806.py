#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

double solve()
{
	double	C, F, X;

	cin >> C >> F >> X;

	vector<double> ans;
	double t = 0.0;
	double cc = 2.0;
	int i = 0;

	do {
		ans.push_back(X / cc + t);
		t += C / cc;
		cc += F;
	} while(X / 2.0 + 2 > t && i++ < 10000000);

	return *min_element(ans.begin(), ans.end());
}

int main()
{
	int		T;

	cin >> T;
	for(int i = 1 ; i <= T ; ++i)
		cout << "Case #" << i << ": " << fixed << setprecision(7) << solve() << endl;
}

