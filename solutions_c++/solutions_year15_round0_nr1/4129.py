#include<stdio.h>
using namespace std;

int main()
{
   int t,c=1;
   int a[1005];
   int smx = 0;
   scanf("%d",&t);
   while(c<=t)
   {
	int ans=0,i = 0;
	scanf("%d",&smx);
	char h = ' ';
        int cc = 0;

	while(h ==' ') scanf("%c",&h);
        a[0] = h - '0';
	for(i=1;i<=smx;i++)
        {
	   scanf("%c",&h);
	   a[i] = h-'0';
          
           
	}
	cc  = a[0];
	for (i =1;i<=smx;i++)
	{
          
	   if(i > cc && a[i]!=0)
           {
	       ans+= (i-cc);
               cc = i;
	   }
	   cc = cc+a[i];
		
        }

     // Case #1: 0

     printf("Case #%d: %d\n",c,ans);
     c++;
   }
}
