#include<iostream>

using namespace std;

int n;
double T[20];
double f(int a, int b)
{
	double x = 1;
	for (int i = 0; i < n; i++)
	{
		if (a & (1 << i)) x *= T[i];
		else if (b & (1 << i)) x *= 1 - T[i];
	}
	return x;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int tt;
    cin >> tt;
    for (int t = 1; t <= tt; t++)
    {
    	cerr << t << "\n";
    	int k;
    	cin >> n >> k;
    	for (int i = 0; i < n; i++) cin >> T[i];
    	double ans = 0;
    	for (int i = 0; i < (1 << n); i++)
    	{
    		int cnt = __builtin_popcount(i);
    		if (cnt != k) continue;
    		int m = i;
    		double s = 0;
    		while(m)
    		{
    			m = i & (m - 1);
    			if (2 * __builtin_popcount(m) != cnt) continue;
    			s += f(m, i);
    		}
    		ans = max(ans, s);
    	}
    	cout.setf(ios::floatfield, ios::fixed);
    	cout.precision(7);
    	cout << "Case #" << t << ": " << ans << "\n";
	}
	
	
	return 0;
}
