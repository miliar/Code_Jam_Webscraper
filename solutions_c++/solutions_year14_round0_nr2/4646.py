#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;

#define EPS 1e-8

int main(){
	int tc;
	double c,f,x;
	cin>>tc;
	for(int i=1;i<=tc;i++){
		cin>>c>>f>>x;
		double cc = 0.0000000; //current cookies
		double speed = 2.0000000;
		double totalTime = 0.0000000;
		while(cc < x){
			//time to wait until finish without buying farm
			double timeEnd = (x-cc)/(speed);
			//time to wait until we get a farm
			double timeFarm = (c-cc)/(speed);
			//time to wait until finish with new farm and zero cookies
			double timeFarmEnd = x/(speed + f);
			
			//printf("timeEnd: %.7lf\ntimeFarm: %.7lf\ntimeFarmEnd: %.7lf\n", timeEnd,timeFarm,timeFarmEnd);
			
			//faster with buying farm
			if((timeFarm + timeFarmEnd) < timeEnd || (fabs((timeFarm + timeFarmEnd) - timeEnd) < EPS)){
				//buy the farm
				//printf("Buying the farm...\n");
				speed += f;
				totalTime += timeFarm;
			} else {
				//dont buy the farm
				//printf("Not buying the farm...\n");
				totalTime += timeEnd;
				cc += speed*timeEnd;
			}
			//printf("Current: %.7lf, Goal: %.7lf\n", cc,x);
			//printf("Current total time: %.7lf\n", totalTime);
		}
		printf("Case #%d: %.7lf\n", i, totalTime);
	}
	return 0;
}