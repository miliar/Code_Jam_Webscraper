#include<iostream>
using namespace std;

double getTime(int farmNum, double f, double curTime, double cookieNum, double x){
	double speed= 2+farmNum*f;
	return curTime+(x-cookieNum)/speed;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas= 1; cas <= t; cas++){
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		bool flag= false;
		double curTime= 0;
		int farmNum= 0;
		double ans= 0;
		while(flag == false){
			if(c > x){
				flag= true;
				ans= getTime(farmNum, f, curTime, 0, x);
				break;
			}
			curTime+= c/(2+farmNum*f);
			double t1= getTime(farmNum, f, curTime, c, x);
			double t2= getTime(farmNum+1, f, curTime, 0, x);
			if(t1 < t2){
				flag= true;
				ans= t1;
				break;
			}
			else{
				farmNum++;
			}
		}
		printf("Case #%d: %.7lf\n", cas, ans);
	}
	return 0;
}