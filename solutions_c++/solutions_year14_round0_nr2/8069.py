#include <cstdio>
#include <iostream> 

using namespace std; 

double c, f, x; 

void solve(int tnum)
{
	cerr << "test " << tnum << endl; 
	cin >> c >> f >> x; 
	double allTime = 0; 
	double v = 2; 
	double ans = 1e100; 
	for (int i = 0; i <= 20000000; i++)
	{
		ans = min(ans, allTime + x / v); 
		allTime += c / v; 
		v += f; 
	}
	cout << "Case #" << tnum << ": "; 
	cout << ans; 
	cout << endl; 
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout); 

	cout.precision(20); 
	cout.setf(ios::fixed); 
	int tc; 
	cin >> tc; 
	for (int t = 0; t < tc; t++)
	{
		solve(t + 1); 
	}

	return 0; 
}