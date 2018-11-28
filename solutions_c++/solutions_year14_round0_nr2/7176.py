#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
	int t,t1=0;
	cin>>t;
	while(t1++<t){
		double F,X,C,cur=2,time=0;
		cin>>C>>F>>X;
		while(X/cur>C/cur+X/(cur+F)){
			time+=C/cur;
			cur+=F;
		}
		time+=X/cur;
		cout<<"Case #"<<t1<<": ";
		printf("%f\n",time);
	}
}