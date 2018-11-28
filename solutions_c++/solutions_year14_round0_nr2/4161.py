#include <bits/stdc++.h>
using namespace std;
vector <double> cummSum(200010);
int main()
{
      int testCases;
      cin >> testCases;
      for (int testNumber = 1; testNumber <= testCases; ++testNumber)
      {
	    cout << "Case #" << testNumber << ": ";
	    double C, F, X;
	    scanf ("%lf%lf%lf", &C, &F, &X);

	    cummSum[0] = 0;
	    double currRate = 2;
	    for (int i = 1; i <= 200000; ++i) {
		  cummSum[i] = C / currRate;
		  currRate += F;
	    }
	    for (int i = 1; i <= 200000; ++i)
		  cummSum[i] += cummSum[i - 1];

	    double ans;
	    int lo = 0, hi = 100000, mid;
	    while (lo < hi) {
		  mid = (lo + hi) / 2;
		  if (cummSum[mid] + X / (2 + mid * F) <= cummSum[mid + 1] + X / (2 + (mid + 1) * F)) {
			hi = mid;
			ans = cummSum[mid] + X / (2 + mid * F);
		  }
		  else
			lo = mid + 1;
	    }
	    printf ("%.7lf\n", ans);
      }
      return 0;
}

