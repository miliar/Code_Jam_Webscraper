#include<iostream>
#include <iomanip>
using namespace std;

int main()
{
	int T;
    long double C;
    long double F;
    long double X;
    long double increment;
    long double time;
	
	freopen("B-large.in","rt",stdin);
	freopen("output.in","wt",stdout);
	cin >> T;
	for(int loop = 1;loop<=T;loop++)
	{
		cin >> C;
		cin >> F;
		cin >> X;
		
		increment = 2.0;
		time = X/increment;
		long double farmTime = 0.0 ;
		
		while(true)
		{
		    long double oneFarm = farmTime + (C / increment) + (X / (increment + F));
			if (time < oneFarm)
			 {
          		break;
        	 }
			 else
			 {
		          farmTime += C / increment;
		          increment += F;
		          time = oneFarm;
        	 }
		}
		cout << fixed;
	    cout <<"Case #"<<setprecision(7)<<loop<<": "<<time<<endl;
		
	}
	return 0;
}
