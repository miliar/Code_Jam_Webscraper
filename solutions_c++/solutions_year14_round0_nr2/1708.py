#include<stdio.h>
#include<iostream>
using namespace std;
double X,C,F;
void init(){
	double t=0,T,a=2;
	cin>>C>>F>>X;
	double minn=X/a;
	while(1){
        T=t+X/a;
        if(T<=minn) minn=T;
        else break;
        t=t+C/a;
        a=a+F;
	}
	printf("%.7lf\n",minn);
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("2.out","w",stdout);
    int T,C;
    cin>>T;
    for(C=1;C<=T;C++){
		cout<<"Case #"<<C<<": ";
		init();
    }
}
