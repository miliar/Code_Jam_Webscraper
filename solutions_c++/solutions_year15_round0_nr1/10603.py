#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<time.h>
#define MAX 1001
int main()
{
int x,y=0,i,j,d,count=0;
int a[MAX],t,n;
char b[MAX];
freopen("in.in","r",stdin);
freopen("out","w",stdout);
scanf("%d",&t);
for(int tt=1;tt<=t;tt++)
{ y=0;
 scanf("%d%s",&n,&b);
 a[0]=b[0]-'0';
 if(a[0]==-48)
	a[0]=0; 
 count=a[0];
 for(i=1;i<=n;i++){
 a[i]=b[i]-'0';
  if(count>=i)
   count=count+a[i];
  else if(a[i]>0)
  {x=i-count;
  y+=x;
   count=count+a[i]+x;
  }
  else
	 continue;
  
}
printf("Case #%d: %d\n",tt,y);
}
getch();
}