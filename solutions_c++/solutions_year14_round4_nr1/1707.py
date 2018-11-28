//#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <string>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

int main(){
	int T, n, x, a[10000];
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> n >> x;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a + n);
		int i = 0, j = n - 1, ans = 0;
		while (i <= j)
		{
			if (a[j] + a[i] > x)
			{
				ans++;
				j--;
			}
			else
			{
				ans++;
				i++;
				j--;
			}
		}
		if (i == j)
			ans++;
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}