#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

#define PI acos(-1.0)

int main(){

	int tt,casos=1;
	scanf("%d",&tt);
	while(tt-- > 0){
		double r,t;
		int cont =0;
		scanf("%lf %lf",&r,&t);
		double a1,a2,pintado=0,maxPint = t*PI;
		a1 = PI*r*r;
		r+=1.0;
		a2 = PI*(r)*(r);
		r+=1.0;
		pintado = a2-a1;
		//cout<<pintado<<endl;
		while(pintado <= maxPint+0.1){
			a1 = PI*r*r;
			r+=1.0;
			a2 = PI*((r)*(r));
			pintado += a2-a1;
			r+=1.0;
			//cout<<a1<<" "<<a2<<" "<<pintado<<endl;
			cont++;
		}
		cout<<"Case #"<<casos<<": "<<cont<<endl;
		casos++;
	}

	return 0;
}
