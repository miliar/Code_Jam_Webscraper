#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main()
{
	int T;
	double C,F,X;
	long long int i,j,k;
	double tc,tx,tt;
	double r;
	double v;

	int S;
	cin>>T;
	S=T;
	while(T--)
	{
		cin>>C>>F>>X;
		r=X-C;
		v=2.0;
		k=0;
		while(1)
		{
			tx=r/v;
			tc=X/(v+F);
			if(tx<tc)
				break;
			else
			{
				v=v+F;
				k++;
			}
		}
		tt=X/(2.0+k*F);
		for(i=0,v=2.0;i<k;i++,v=v+F)
		{
			tt=tt+C/v;
		}
		cout<<"Case #"<<S-T<<": ";
		cout<<fixed<<setprecision(7)<<tt<<endl;
	}


	return 0;
}
