#include<iostream>
using namespace std;
#include"stdio.h"
 double timcal(double c, double f, double x,int n){
	int i;
	 double rate =2;
	 double time =0;
	for (i=0;i<n;){
		time += (c/rate);
		rate += f;
		i++;
	}
	time += (x/rate);
	return time;
}



int main(){
	int z1,z;
	double c,f,x;
	double rate;
	double tp,t;
	int i;
	cin>>z1;
	for(z=1;z<=z1;z++){
		cin>>c>>f>>x;
		rate = 2;
		tp = x/rate;
		t=tp;
		for(i=1;tp>=t;i++){
			tp =t;
			t = timcal(c,f,x,i);
		}
		cout<<"Case #"<<z<<": ";
		printf("%lf",tp);
		cout<<"\n";
	}
}
