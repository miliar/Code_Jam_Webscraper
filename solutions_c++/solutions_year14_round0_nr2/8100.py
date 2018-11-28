#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int t,i,tc;
	double c,f,x,min,rate,ans;
	cin>>t;
	tc = 0;
	while(t--) {
		tc++;
		cin>>c>>f>>x;
		min = 1000000000;
		i = 0;
		rate = 2;
		ans = x/2;
		while(true) {
			min = ans + (c/(i*f + 2)) - (x/(i*f + 2)) + (x/((i+1)*f + 2));
			i++;
			if(min > ans) break;
			ans = min;
		}
		printf("Case #%d: %.10lf\n",tc,ans);
	}
	return 0;
}