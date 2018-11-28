#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

double time(int num, double costFarm, double cookiesIncrease, double winAmount){
	double curr = 2.0;
	double t = 0.0;
	for(int i=0;i<num;i++){
		t += (costFarm / curr);
		curr += cookiesIncrease;
	}
	t += (winAmount/curr);
	return t;
}

double timeTaken(double costFarm, double cookiesIncrease, double winAmount){
	double ans = 100000.0,last;
	int i=0;
	while(true){
		last = ans;
		ans = time(i,costFarm,cookiesIncrease,winAmount);
		if(ans>last){
			return last;
		}
		i++;
	}
	return last;
}

int main(){
	int t;
	double a,b,c;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		scanf("%lf %lf %lf",&a,&b,&c);
		printf("%.7lf\n",timeTaken(a,b,c));
	}
}
