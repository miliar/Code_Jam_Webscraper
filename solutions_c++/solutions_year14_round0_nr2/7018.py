#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int k=1;k<=t;k++){
		double c,f,x,t=0,y=2,m,n,s=0;
		int a=1;
		cin>>c>>f>>x;
		while(a){
		m=x/y;
		t=c/y;
		y=y+f;
		n=t+x/y;
		if(m>n){
			s=s+t;
		}
		else{
			s=s+m;
			a=0;
		}
	}
	cout<<"Case #"<<k<<": ";
	printf("%.7f\n",s);
}
return 0;
}
		
		
