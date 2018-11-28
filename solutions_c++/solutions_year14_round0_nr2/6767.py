#include <iostream>
using namespace std;

int main() {
	int T;
	cin>>T;
	for( int i = 1; i <= T; i++ ){
		double c,f,x,time,farmtime,baserate=2,min = 9999999;
		cin>> c >> f >> x;
		min = x/baserate;
		farmtime = 0;
		while(1){
			farmtime += c/baserate;
			baserate += f;
			time = x/baserate;
			if(min>farmtime+time)
			min = farmtime+time;
			else
			break;
		}
		printf("Case #%d: %0.7lf\n",i,min);
	}
	return 0;
}