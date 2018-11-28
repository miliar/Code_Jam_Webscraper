#include <iostream>
using namespace std;


int main(){
	//freopen("B-large.in.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int i,c;
	double farmTime[100005];
	int t;
	double farmCost, farmSpeed, needed;
	cin>>t;
	for(c=1;c<=t;c++){
		cin>>farmCost>>farmSpeed>>needed;

		
		farmTime[0]=0.0;
		for(i=1;i<100005;i++){
			double speed = 2.0 + farmSpeed*(i-1);
			farmTime[i] = farmTime[i-1] + farmCost/speed;
		}

		double minn = 1e9;
		for(i=0;i<100005;i++){
			double speed = 2.0 + farmSpeed * i;
			minn = min(minn, farmTime[i] + needed/speed);	
		}

		printf("Case #%d: %.12lf\n",c,minn);

	}

	return 0;
}