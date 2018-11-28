#include <iostream>
#include<iomanip>
using namespace std;

int main() {
	double c,s,f,i,x,X,t;
//	cout.precision(7);
	int test;cin>>test;
	for( i=0;i<test;i++){
	x=c=s=f=X=t=0;s=2;
	cin>>c>>f>>X;
	while(1){
	 if(X/(s+f)>(X-c)/s){
	   t+=(X)/s;break;
	   }
	 t+=c/s;//cout<<t<<" ";
	 s+=f;
	
	 }
	 cout<<"Case #"<<i+1<<": "<<setprecision(15)<<t<<endl;}
	return 0;
}
