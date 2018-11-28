#include <iostream>

using namespace std;

int main(void){

	freopen("B-large.in","r",stdin);
	freopen("a2.out","w",stdout);

	int t;
	cin>>t;

	for(int test=0;test<t;test++){
		double c,f,totalCookies;
		cin>>c>>f>>totalCookies;
		int totalFarms = 0;
		double rate = 2.0;
		double totalTime = 0;
		while(true){
			double t = c/rate;
			//cout<<totalTime<<" "<<totalCookies/rate<<" "<<totalTime+totalCookies/(rate+f)+t<<endl;
			if(totalTime+totalCookies/rate<=totalTime+totalCookies/(rate+f)+t){
				printf("Case #%d: %.7lf\n",test+1,totalTime+totalCookies/rate);
				break;
			}else {
				totalTime+=c/rate;
				rate+=f;
			}
		}
	}


}