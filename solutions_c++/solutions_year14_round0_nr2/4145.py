#include<iostream>
#include<cstring>
#include<fstream>
#include<iomanip>

using namespace std;


int main()
{
	int T;
	ifstream f;
	ofstream f2;
	int i,j,k;
  	f.open ("B-large.in");
	f2.open("B-large.out");
	f>>T;
	double C,F,X;
	double rate;
	double time;
	double exp_time1, exp_time2, rem_cookie;
	int done =0;
	for( i=0; i<T; i++ )
	{
		f>>C;
		f>>F;
		f>>X;
		rate = 2;
		time = 0;
		done =0;
		rem_cookie = X;
		while ( done ==0 )
		{
			exp_time1 = time + (rem_cookie/rate);
			exp_time2 = time + C/rate + (rem_cookie/(rate+F));
			//case when generate new farm
			if( exp_time2 < exp_time1 )
			{
				//create new farm 
				//update rate, time taken till now, remaining won't change
				time = time + C/rate;
				rate = rate + F;
			}
			else   // don't create farm
			{
				time = time + ( rem_cookie/rate );
				done = 1;
			}
		}
		
		f2<<"Case #"<<(i+1)<<": "<<setprecision(10)<<time<<endl;
				
		
	}
	f.close();
	f2.close();


	return 0;
}
