#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
double C,F,X;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("outputGoogleJam.txt","w",stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> C >> F >> X;
		double cur = 2;
		double ans = INT_MAX;
		double res = 0,s;
		while(1)
		{
			s = res + X / cur;
			if (s > ans)
				break;
			ans = s;
			res += C / cur;
			cur += F;
		}
		printf ("Case #%d: %.7lf\n",i + 1,ans);
	}
	return 0;
}