#include <cstdio>
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
	int k, t;
	cin>>t;
	for(k=0;k<t;k++)
	{
		double c, f, x;
		cin>>c>>f>>x;
	//	cout<<c<<f<<x<<endl;
		double time=0;
		double v=2;
		while((c/v)+(x/(v+f))<x/v)
		{
			time+=c/v;
			v+=f;
	//		cout<<time<<endl;
		}
		time+=x/v;
		cout << setprecision(7) << fixed;
	//	printf("%7lf\n", time); 

		cout<<"Case #"<<k+1<<": "<<time<<endl;
	}
	return 0;
}
