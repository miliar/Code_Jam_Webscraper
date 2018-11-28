#include <iostream>
#include <stdio.h>
using namespace std;

double time(double c,double f,double x){
	double last = 2,sum1 = 0,sum2 = 0;
	sum1 = x / last; sum2 = c / last;
	while(sum1 > x / (last + f) + sum2){
		last += f;
		sum1 = sum2 + x / last;
		sum2 += c / last;
	//	if(sum1 < x / (last + f) + sum2)
	//		break;
	}
	return sum1;
}
void read(){
	int t;
	double c,f,x;

	scanf("%d",&t);
	for(int i = 0; i < t; i++){
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: %.7lf\n",i + 1,time(c,f,x));
	}

}
int main(){
	freopen("f.txt","r", stdin);
	freopen("fout.txt","w",stdout);
	read();

	return 0;
}
