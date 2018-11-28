// Cookie Clicker Alpha.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int t;
	double c, f, x;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	double ans;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> c >> f >> x;
		int count = 0;
		ans = -1;
		int cc = 0;
		double temp=0;
		double temp2 = 0;
		double curr=0;
		while (true)
		{
			temp = x / (2 + cc*f) + curr;
			
			if (ans == -1 || temp < ans){
				ans = temp;
				curr += c / (2 + cc*f);
				cc++;
			}
			else
			{
				break;
			}
		}
		cout << "Case #" << i + 1 << ": " << setiosflags(ios::fixed) << setprecision(7) << ans << endl;
	}
}
