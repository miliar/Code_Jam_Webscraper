#include <stdio.h>
#include <math.h>
#include <string.h>
//const double eps = 1e-8;
int main(){
	//freopen("out.txt","w",stdout);
	int T;
	int ca = 1;
	scanf("%d",&T);
	while( T-- ){
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		double sum = 0.0;//当前产生的cookie总数
		double rateAdd = 2.0;//当前的产生速度
		double farm_num = 0;//当前的farm数目
		double ti = 0;//当前花费的时间
		while( 1 ){
			//printf("time = %lf\n",ti);
			if( sum>=x ) break;
			if( sum>=c ){
				if( c <= ( f*( x -( sum-c ) )/(rateAdd+f)) ){
					//buy
					sum -= c;
					farm_num += 1.0;
					rateAdd += f;
					//printf("buy farm = %d\n",farm_num);
				}
				else {
					double left = x - sum;
					sum = x;
					ti += (left/rateAdd);
					//printf("no buy & over\n");
				}
			}
			else{
				double left = c-sum;
				if( left>=x ) left = x;
				ti += (left/rateAdd);
				sum = c;
				//printf("produce time = %lf\n",ti);
			}
		}
		printf("Case #%d: ",ca++);
		printf("%.6lf\n",ti);
	}
	return 0;
}