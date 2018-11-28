#include<iostream>
using namespace std;


int main(){
	int n;
	double t,cps,C,F,X;
	cin>>n;

	for(int i=0;i<n;i++)
	{
		cps=2; 
		t=0;
		cin>>C>>F>>X;
		while((X/cps)>(C/cps+X/(cps+F)))
		{
			t+=C/cps;
			cps+=F;
		}
		t+=X/cps;
		printf("Case #%d: %.7f \n",i+1,t);
	}
	return 0;
}