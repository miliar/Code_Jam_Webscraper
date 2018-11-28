#include<stdio.h>
#include<iostream>
#include<vector>
#include<iomanip>
#include<algorithm>

using namespace std;

int main()
{

	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int t;
	cin>>t;
	for (int p=0;p<t;p++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double t1 = (x-0.f)/2.0;
		double t2 = t1;
		double tf=0;
		double rate=2.0;
		while(true)
		{
			tf=tf + c/rate;
			rate=rate+f;
			t2=tf+x/rate;
			if (t2>t1)
				break;
			else
				t1=t2;			
		}

		cout<<fixed<<setprecision(7)<<"Case #"<<p+1<<": "<<t1<<endl;
	}

	return 0;
}
