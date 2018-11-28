#include<iostream>
using namespace std;
#include<stdio.h>

int main(){
	int tt,inc=1;
	double c,f,x,z,y,r,t;
	scanf("%d",&tt);
	while(tt--){
		//scanf("%f%f%f",&c,&f,&x);
		cin>>c>>f>>x;
		r=2.00000000;
		z=x/r;
		y=c/r+x/(r+f);
		t=0.0000000;
		while(z>y){
			t=t+c/r;
			r=r+f;
			z=x/r;
			y=c/r+x/(r+f);
		}
		t=t+z;
		printf("Case #%d: %0.7f\n",inc++,t);
		//cout<<t<<endl;
	}
	return 0;
}
