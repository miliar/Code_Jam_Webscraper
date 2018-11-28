#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main(){
long long int i,j,k,t,z=0;
double c,f,x,s=0.0,l=0.0,m=0.0,n=2.0;
scanf("%lld",&t);
while(t--){
    n=2.0;
    s=0.0;
    z++;
    scanf("%lf %lf %lf",&c,&f,&x);
    while(x/n>( c/n + x/(n+f) )){
    //cout<<'a';
    s+=c/n;
    n+=f;
    }
    s+=x/n;
printf("Case #%lld: %.7lf\n",z,s);
}
return 0;
}
