#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <sstream>

using namespace std;

//(500/14)+(2000/18) > 2000/14 No continúo, de lo contrario sigo
//es decir si es menor sigo
int t;
int cookies = 0;
int main()
{
	ios_base::sync_with_stdio(false);
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		double c = 0.0, f= 0.0, x= 0.0;
		double cookiesNow = 2.0, z = 0.0;
		scanf("%lf %lf %lf", &c, &f, &x);
		double ans = 0, ans1 = 0;
		
		while(true)
		{
			char buffer[100];
			if(((c/cookiesNow)+(x/(cookiesNow+f))) >= (x/cookiesNow))
			{
				z = (x/cookiesNow);
				sprintf(buffer,"%.7f",z);
				stringstream ss(buffer);
				ss >> z;
				ans1 += z;
				break;
			}
			z = (c/cookiesNow);
			sprintf(buffer,"%.7f",z);
			stringstream ss(buffer);
			ss >> z;
			ans1 += z;
			if(((c/cookiesNow)+(x/(cookiesNow+f))) < (x/cookiesNow))
			{
				cookiesNow += f;
				continue;
			}			
		}
		printf("Case #%d: %.7f\n", i+1, ans1);
	}

	return 0;
}