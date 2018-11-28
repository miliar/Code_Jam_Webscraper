#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

double c,f,x;
int t;

int main(){
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);

	scanf("%d",&t);
	for ( int i = 1; i <= t; ++ i){
		printf("Case #%d: ",i);
		scanf("%lf%lf%lf",&c,&f,&x);
		double min = x / 2;
		double cur = 2.0;
		double curtime = 0.0;
		while (x / cur > c / cur + x / (cur+f)){
			curtime += c / cur;
			cur += f;
		}
		curtime += x / cur;
		printf("%.7lf\n",curtime);
	}
}