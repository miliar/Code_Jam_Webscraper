#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,I;
	cin>>t;
	for(I=1;I<=t;I++)
	{
		double c,f,x,rate = 2.0,t = 0.0;
		cin>>c>>f>>x;
		while((t+(x/rate)) > (t+(c/rate) + x/(rate+f)))
		{
			t = t+(c/rate);
			rate = rate + f;
		}
		printf("Case #%d: %0.7lf\n",I,(t+x/(rate)));
	}
	return 0;
}