#include <stdio.h>

int main(void) {
   int t,n;float na[10],k[10];int ws,ds,flag,c;float k1[10],na1[10];int a,a1,b,y1,y2,y3,y4,x,z,x1,x2; float ck,ch;

scanf("%d",&t);
for(x=1;x<=t;x++)
{   ws=0;flag=0;ds=0;c=0;
 scanf("%d",&n);
 for(x1=0;x1<n;x1++)
 {scanf("%f",&na[x1]);}
 for(x2=0;x2<n;x2++)
 {scanf("%f",&k[x2]);}
 for(a=0;a<n;a++)
 {
  for(a1=0;a1<n-1;a1++)
  {
   if(na[a1]>na[a1+1])
   {
   ck=na[a1];
   na[a1]=na[a1+1];
   na[a1+1]=ck;
   }
    if(k[a1]>k[a1+1])
   {
   ch=k[a1];
   k[a1]=k[a1+1];
   k[a1+1]=ch;
   }
 } }
    for(z=0;z<n;z++)
    {
    na1[z]=na[z];
    k1[z]=k[z];}
  for(y1=0;y1<n;y1++)
  {
    for(y2=0;y2<n;y2++)
    {     flag=0;
      if(na[y1]<k[y2])
      {  flag=1;
	na[y1]=0.0;
	k[y2]=0.0;break;}}
       if(flag==0)
ws=ws+1;}

y4=n-1;
       while(na1[0]>0.0)
       {
	for(y2=y4;y2>=0;y2--)
	{
	if(na1[y2]>k1[y2])
	{ds=ds+1;
	na1[y2]=0.0;
	k1[y2]=0.0;  } }
c=0;
	for(y3=0;y3<n;y3++)
	{
	if(na1[y3]==0.0)
	continue;
	else
	{na1[c]=na1[y3];
	k1[c]=k1[y3];
	if(c!=y3)
	{na1[y3]=0.0;
	k1[y3]=0.0;}
	c++;
	}}
	na1[0]=0.0;k1[c-1]=0.0;
	for(y4=0;y4<c-1;y4++)
	{
	  na1[y4]=na1[y4+1];
na1[y4+1]=0;}  }
	  printf("%d%d",ws,ds);
printf("\n");
	  }








	
	return 0;
}