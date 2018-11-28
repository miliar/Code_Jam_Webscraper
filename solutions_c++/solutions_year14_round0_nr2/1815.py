#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	cout.setf(ios::fixed);
	cout.precision(7);
	
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		
		double limit = X / C - 2 / F;
		
		int k;
		if (limit < 0)
			k = 0;
		else
			k = (int)limit;
		
		double ans = 0;
		for (int i = 0; i < k; i++)
			ans += C / (2.0 + i * F);
		ans += X / (2.0 + k * F);
		
		cout << "Case #" << caseI << ": " << ans << endl;
	}
	
	return 0;
}
