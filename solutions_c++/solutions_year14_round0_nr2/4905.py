#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
    freopen("B-small.in","r",stdin);
    freopen("a.txt","w",stdout);
int T,t;
double C,F,X,time,cookies,x;
scanf("%d",&T);
t=1;
while(t<=T){
	cin>>C;
	cin>>F;
	cin>>X;
	time=0;
	cookies=0;
	x=2;
	while(cookies!=X){
	if((C/x)+(X/(x+F))>X/x){
	time=time+X/x;
	cookies=X;
	}
	else
	{
		time+=C/x;
		x+=F;
		cookies=0;
	}
	}

printf("Case #%d: %.7f\n",t,time);
t++;
}
return 0;
}
