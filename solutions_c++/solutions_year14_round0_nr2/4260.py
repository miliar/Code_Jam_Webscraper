#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <limits>
#include <cstring>

using namespace std;


double getMin(double  C,double F,double X)
{
	double t1 = X/2;
	// printf("t1 = %.7lf  ",t1 );
	double t2;
	double i = 2;
	while(1)
	{
		
		t2 = t1 - X/i + C/i + X/(i+F);

		// printf("t2 = %.7lf  i = %lf\n",t2,i );
		if(t2 < t1)
		{
			t1 = t2;
			// printf("t1 = %lf ",t1 );
			i = i+F;
		}
		else
			return t1;
	}
}
int main()
{
	int T;
	double C,F,X;
	scanf("%d",&T);
	for(int t = 1;t<=T;t++)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		double ans = getMin(C,F,X);
		printf("Case #%d: %.7lf\n",t,ans);
	}
	return 1;

}