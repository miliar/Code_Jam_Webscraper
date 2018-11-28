#include<iostream>
#include<stdio.h>

using namespace std;
int main(){
double c,f,x,t,a;
int n,i;
//FILE *fp=fopen("attempt1.in","r");
//FILE *fpo=fopen("out.txt","w");
cin>>n;
//fscanf(fp,"%d",&n);
for(i=1;i<=n;i++)
{
//fscanf(fp,"%d",&a);
cin>>c>>f>>x;
a=2;
t=0;
while(1)
{
if(x/a < x/(a+f)+c/a)
{
t+=x/a;
break;
}
else
{
t+=c/a;
a+=f;
}
}
//fprintf(fpo,"Case #%d: Bad magician!\n",i+1);
printf("Case #%d: %lf\n",i,t);
}
}

