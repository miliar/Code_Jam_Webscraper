#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
using namespace std;
int pie[1005];
int max(int i, int j)
{
	return i > j ? i : j;
}
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T = 0;
	int caseT = 1;
	cin >> T;
	while (T--)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> pie[i];
		}
		int sum1=0, sum2=0,maxx=0;
		for (int i = 0; i < n - 1; i++)
		{
			maxx = max(maxx, pie[i] - pie[i + 1]);
			if (pie[i + 1] < pie[i])
			{
				sum1 += pie[i] - pie[i + 1];
			}
		}
		for (int i = 0; i < n - 1; i++)
		{
			sum2 += maxx>pie[i] ? pie[i] : maxx;
		}
		cout << "Case #" << caseT++ << ": " << sum1 << " " << sum2 << endl;
	}
	return 0;
}
