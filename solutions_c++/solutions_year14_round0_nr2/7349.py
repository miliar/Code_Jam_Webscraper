// iHaala Madrid - A Gunner
#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

int main(){
	int t,a,b;
	double c,f,x,p,q,r,i,j;
	cin>>t;
	
	for(int tt=1;tt<=t;tt++){		
		cin>>c>>f>>x;
		
		p=0.00;r=2.000,q=0.0;
		while(1){
			i= (x*1.0)/r;
			j= (c*1.0)/r + (x*1.0)/(r+f);
			if(i<=j){
				p+=i;
				break;
			}			
			p+=((c*1.0)/r);
			r+=f;
		}
		
		cout<<"Case #"<<tt<<": ";				
		printf("%.7f",p);
		cout<<endl;
	}
	
	return 0;	
}