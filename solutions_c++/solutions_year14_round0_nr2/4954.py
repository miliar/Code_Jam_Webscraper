#include<iostream>
using namespace std;

int main(){
	double c,f,x;
	double time;
	double temp,flag;
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>c>>f>>x;
		time=0;
		temp=2;
		flag=f*x/c-f;
		while(flag>temp){
			time+=c/temp;
			temp+=f;
		}
		time+=x/temp;
		printf("Case #%d: %.7lf\n",i,time);
	}
	return 0;
}