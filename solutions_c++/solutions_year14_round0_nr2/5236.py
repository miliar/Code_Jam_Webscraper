
/*
1 = C = 500.
1 = F = 4.
1 = X = 2000.
*/
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double rate=2.0;
	//	bool in=false;
		double tim=0;
		while((x-c)/rate>x/(rate+f))
		{
			tim+=c/rate;
			rate+=f;
			//in=true;
		}
		tim+=x/rate;
		cout.precision(7);
		cout<<"Case #"<<tc<<": "<<fixed<<tim<<endl;


	}
	return 0;
}
