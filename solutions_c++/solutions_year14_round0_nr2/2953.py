#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
using namespace std;
int main()
{freopen("B-large.in","r",stdin);
freopen("out.txt","w",stdout);
double c,f,x,s=0.0,k,l,d,m=2.0,n=2.0;
int t,j;
cin>>t;
for(j=0;j<t;j++)
{s=0.0;k=0.0;l=0.0;m=2.0;n=2.0;
cin>>c>>f>>x;
k=x/m;
l=k;
do{k=l;
n=c/m;
s=n+s;
m=m+f;
l=s+(x/m);
d=k-l;
}while(d>0.0);
printf("Case #%d: %.7f\n",j+1,k);
}
getch();
return 0;
}