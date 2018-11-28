#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	freopen("b-large.in.txt","r",stdin);
	freopen("b-large.txt","w",stdout);
	int T;
	cin >> T;
	for (int tt = 0 ; tt < T ; tt++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double nown = X/C - 2/F - 1;
		int n = ceil(nown);
		//cout << "fuck " << n << endl;
		if (n < 0) n = 0;
		double ans = 0;
		for (int i = 0 ; i < n ; i++)
			ans += C / (2 + i*F);
		ans += X/(2 + n*F);
		printf("Case #%d: %.7lf\n", tt+1, ans);
	}
}