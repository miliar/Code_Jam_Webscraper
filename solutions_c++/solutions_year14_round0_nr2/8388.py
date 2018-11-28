#include <iostream>
#include <cmath>
#include <string>
#include <queue>
using namespace std;

int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for (int i = 0; i  < t; i++)
    {
    	double c, f, x;
    	cin >> c >> f >> x;
    	double tec = 2;
    	double ans = 100000000000;
    	double time = 0;
    	double ost = 0;
    	do
    	{
    		ans = min(ans, time + x/tec);
    		time += c / tec;
    		tec = tec + f;
    	}
    	while (ans >= time + x/tec);
	printf("Case #%d: %.7lf\n",i + 1, ans);
}
    return 0;
}
