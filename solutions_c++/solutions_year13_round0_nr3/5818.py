#include <iostream>
#include <cmath>
#include <stdio.h>
#define pi 4*atan(1.0)
using namespace std;
int main()
{
int k1,k2,n,i,t,j,a[10500],c[100],k;
int b[6]={1,4,9,121,484,10201};
for (i=0;i<=5;i++)
for (j=b[i];j<b[i+1];j++)
a[j]=i+1;
cin>>n;
for (i=0;i<n;i++)
{
cin>>k1>>k2;
t=a[k2]-a[k1];
if ((k1==1||k1==4||k1==9||k1==121||k1==484)&&(k2==1||k2==4||k2==9||k2==121||k2==484)) t++;
else if (k1==1||k1==4||k1==9||k1==121||k1==484) t++;
cout<<"Case #"<<i+1<<": "<<t<<endl;
}
return 0;
}
