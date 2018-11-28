using namespace std;
#include<iostream>
#include<stdio.h>

double C,F,X;
int main()
{
freopen ("B-large.in","r",stdin);
freopen ("B-large.out","w",stdout);

long t;
cin>>t;
for(long k=1;k<=t;k++)
{
  cin >>C>>F>>X;

  double i=2;
  double time=0;
  
  while(C/i+X/(i+F) < X/i)
  { time+=C/i; i+=F;}

  time+=X/i;
  printf("Case #%d: %.7f\n",k,time);

}
}

