#include<iostream>
#include<stdio.h>
#include<limits.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	int t2=0;
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(7);
	//freopen("out.txt","w",stdout);
	while(t--){
		++t2;
		double c,ff,x;
		cin>>c>>ff>>x;
		double f=2;
		double mini = 1000000000;
		double next = x/f;
		 double timee=0;
		while(next<mini){
			timee += c/f;
			mini= next;
			f += ff;
			next = x/f + timee;
	}	
	 cout<<"Case #"<<t2<<":"<<" "<<mini<<endl;
	// printf("%.6lf\n",mini);
}
}
