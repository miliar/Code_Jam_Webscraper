#include <bits/stdc++.h>
using namespace std;

int n;
double wantAmount, wantT;
double amountNeg, amountPos, amountZero;
double sumNeg, sumPos;

void solve()
{
	amountNeg = amountPos = amountZero = 0;
	sumNeg = sumPos = 0;

	cin >> n;
	cin >> wantAmount >> wantT;

	for(int i = 1; i <= n; i++)
	{
		double amount, t;
		cin >> amount >> t;
		if(t < wantT)
		{
			amountNeg += amount;
			sumNeg += amount * (wantT - t);
		}
		if(t > wantT)
		{
			amountPos += amount;
			sumPos += amount * (t - wantT);
		}
		if(t == wantT)
		{
			amountZero += amount;
		}
	}

	if(sumPos > sumNeg)
		amountPos = amountPos * sumNeg / sumPos;
	if(sumPos < sumNeg)
		amountNeg = amountNeg * sumPos / sumNeg;

	double total = amountNeg + amountPos + amountZero;
	if(total == 0)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << wantAmount / total << endl;


	
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int ret = MAIN();
	#ifdef LOCAL_TEST
		cout << "[Finished in " << clock() - start << " ms]" << endl;
	#endif
	return ret;
}
