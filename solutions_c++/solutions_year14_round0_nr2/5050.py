#include <stdio.h>
#include<iostream>
using namespace std;
int main()
{
int N,i;
cin>>N;
for (i =1; i<=N; i++)
{
double F,X,C,rt=2.0,t=0.0;
scanf("%lf%lf%lf",&C,&F,&X);
while ((X/rt) >(C/rt) + (X/(rt+F)))
{
t+= (C/rt);
rt+= F;
}
t+=(X/rt);
printf("Case #%d: %0.7lf\n",i, t);
}
return 0;
}