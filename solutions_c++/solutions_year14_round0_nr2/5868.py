#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; ++tt)
	{
		long double c, f, x;
		cin >> c >> f >> x;
		long double frequency = 2, seconds = 0;
		while(c * frequency + c * f < x * f) seconds += c / frequency, frequency += f;
		seconds += x / frequency;
		cout << fixed << setprecision(7) << "Case #" << tt << ": "<< seconds << endl;
	}
	return 0;
}