#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int t;
	cin>>t;
	double c,f,x;
	for(int cs=1;cs<=t;cs++){
		cin>>c>>f>>x;
		double total=0,rate=2.0;
		while(true){			
			if( c/rate + x/( rate + f ) >= x/rate ){
				total += x/rate;
				break;
			}
			total+=c/rate;
			rate+=f;
		}
		cout<<setprecision(10)<<"Case #"<<cs<<": "<<total<<endl;
	}
	return 0;
}

