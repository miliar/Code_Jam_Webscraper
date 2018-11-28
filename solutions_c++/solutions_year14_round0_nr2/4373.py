#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <iostream>
#include <istream>
#include <limits>
#include <ios>
#include <time.h>
#include <math.h>
using namespace std;

bool isp(int x,int a,int b){

for(int i  =1;i<=a;++i)
{
if(x%i==0 && x/i<=b){return false;}
}
return true;
}



int main(){
int a,b;
cin >> a;
b= a;
while(a>0){

double c,f,x;

scanf("%lf %lf %lf",&c,&f,&x);


double q1= f*(x/c);

q1-=2;

double n = q1/f;

long k = (long)n;

double ans = 0;
if(k<=0){k=0;}


for(double i = 0;i<k;++i){
ans+=(c/(2+i*f));
}



ans+=(x/(2+k*f));





printf("Case #%d: %lf\n", b-a+1,ans);


--a;
}


return 0;

}







