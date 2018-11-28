#include <iostream>
#include <stdio.h>
#include <string.h>
#include <cmath>
#include <iomanip> 

using namespace std;

int main()
{
	freopen ("B-large.in","r",stdin);
	freopen ("b-l.out","w",stdout);
	int n;
	cin >> n;
	for(int s = 0; s < n; s++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double seg = 0;
		double rA = 2;
		while(true)
		{
			double t = X/rA;
			double nt = C/rA + X/(rA + F);
			if(nt < t)
			{
				seg += C/rA;
				rA += F;
			} else {
				seg += X/rA;
				break;
			}
		}
		cout << "Case #" << s + 1 << ": " << fixed << setprecision(7) << seg << endl;
	}
	return 0;
}
