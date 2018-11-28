#include<iostream>
using namespace std;
#include<stdio.h>
//#include<fstream>

int main(){
int y,t,i,j;
double c,f,x;
cin>>t;
y=t;
while(t--){
double ans=0,tym=0,rate=2,a,b;
int chk=0;
cin >>c >>f >>x;
ans=x/2;
        a=c/2;
        b=0;
while(a+x/(rate+f)<ans){
//	if(2*f>x)
//	ans+=c/rate;
//if(2*f>x){
//tym=x/2;
//break;
  //}  
tym+=c/rate;
rate+=f;
//	if(chk>0){
b=a;
a=c/rate;
//	}
ans=x/rate;
      //      cout <<" ans " <<ans <<"\n";
chk++;
}
//if(chk==0)
//cout<<"Case #" << y-t <<": "<<x/2 <<"\n";
  // else
   printf("Case #%d: %.7lf\n", y-t,tym+x/rate);
}
return 0;
}
