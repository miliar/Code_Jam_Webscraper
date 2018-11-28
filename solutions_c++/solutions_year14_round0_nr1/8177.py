#include <iostream>
#include<stdio.h>
#include<cstdio>
using namespace std;
int main (void)
{
   int T, a[16],b[16],i1,i2,k1,k2,j=0,i=0,l=0,p,count;
   
   
    freopen ("A-small-attempt2.in","r",stdin);
    freopen("A-output.txt","w",stdout);
    scanf("%d", &T);
    for(l=1;l<=T;l++)
    {
    count=0;
    scanf("%d",&i1);
    k1=4*(i1-1);
    for(i=0;i<16;i++)
     scanf("%d",&a[i]);
    
     scanf("%d",&i2);
     k2=4*(i2-1);
     for(i=0;i<16;i++)
     scanf("%d",&b[i]); 
   for(i=0;i<4;i++)
   {
   	for(j=0;j<4;j++)
   	{
   		if(a[k1+i]==b[k2+j])
   		{
   			count++;
   		    p= a[k1+i];
   		}
   		 
   	}
   }
   printf("Case #%d: ",l);
   if(count==1)
     printf("%d\n",p);
     else if(count==0)
     printf("Volunteer cheated!\n");
     else
      printf("Bad magician!\n");
  
}
return(0);
}
