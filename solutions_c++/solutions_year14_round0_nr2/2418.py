#include <iostream>
#include <iomanip>
using namespace std;

const int K = 1e7 + 5;

inline double solve()
{
	double c, f, x;
	cin >> c >> f >> x;

	double ret = x/2, cur = 2., elap = 0.;
	

	for(int i=0; ;++i) {
		elap += c/cur;
		cur += f;
		ret = min(ret, elap+x/cur);

		if(elap+c/(cur+f)+x/(cur+f) >= elap+x/cur)
			break;
	}

	return ret;
}

int main()
{
	int nt;
	cin >> nt;
	cout << fixed << setprecision(7);
	for(int i=1; i<=nt; ++i) {
		cout << "Case #" << i << ": " << solve() << endl;
	}

	return 0;
}
