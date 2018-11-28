#include<iostream>
#include<stdio.h>
using namespace std;
int min(int a,int b)
{
if(a<b)
return a;
else
return b;
}
int max(int a,int b)
{
if(a>b)
return a;
else
return b;
}
int main()
{
int T,i,x,r,c,mint,maxt;
FILE *ifp,*ofp;
ifp=fopen("D-small-attempt0.in","r");
ofp=fopen("outputCJ2","w");
fscanf(ifp,"%d",&T);
for(i=0;i<T;i++)
{
fscanf(ifp,"%d%d%d",&x,&r,&c);
fprintf(ofp,"Case #%d: ",(i+1));
if(x==1)
fprintf(ofp,"GABRIEL\n");
else if(x==2)
{
 if((r*c)%2==1)
	fprintf(ofp,"RICHARD\n");
else 
fprintf(ofp,"GABRIEL\n");
}
else if(x==3)
{
mint=min(r,c);
maxt=max(r,c);
if((mint==2 && maxt==3)||(mint==3 && maxt==3)||(mint==3 && maxt==4))
fprintf(ofp,"GABRIEL\n");
else
fprintf(ofp,"RICHARD\n");
}
else if(x==4)
{
mint=min(r,c);
maxt=max(r,c);
if((mint==3 && maxt==4)||(mint==4 && maxt==4))
fprintf(ofp,"GABRIEL\n");
else
fprintf(ofp,"RICHARD\n");
}
}
}

