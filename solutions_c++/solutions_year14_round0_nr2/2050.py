#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	for (int tt=1;tt<=t;tt++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double vm = f*(x-c)/c;
		double v = 2;
		double ans = 0;
		while (v<vm)
		{
			ans +=c/v;
			v += f;
		}
		ans += x/v;
		cout<<"Case #"<<tt<<": "<<fixed<<setprecision(7)<<ans<<"\n";
	}
	return 0;
}