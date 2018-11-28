#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int ty=0;ty<t;ty++){
		double c,f,x;
		cin>>c>>f>>x;
		cout<<"Case #"<<ty+1	<<": ";
		double time1=0;
		if(x<c){
			time1=x/2;
			printf("%.8lf\n", time1);
		}
		else{
			double num=(x-c)*f;
			double hello=num/c;
			int cou=(hello-2.0)/f;
			double time2;
			double curr=2.0;
			for(int i=0;i<cou;i++){
				time1+=c/curr;
				curr+=f;
			}
			time2=c/curr + time1;
			time2 = min(time1 + x/(curr),time2 + x/(curr+f));
			//cout<<"\n"<<"cou is "<<endl;
			printf("%.8lf\n", time2);
			//cout<<time2<<endl;
		}
	}
}

