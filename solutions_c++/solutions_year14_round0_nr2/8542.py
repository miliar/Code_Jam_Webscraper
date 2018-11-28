#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
long double c,f,x;long double r=2;long double total=0;
cin>>c>>f>>x;
double time=0;
if(c<x){
	while(((x/r) >(c/r) + (x/(r+f)) ) >0)
		{
		time=time+c/r;
		r=r+f;
		total=total+c;
		}
	time=time+x/r;	
}
else {time=time+x/r;}

printf("Case #%d: %0.7f\n",i,time);
}





}