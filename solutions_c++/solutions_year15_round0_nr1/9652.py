#include<bits/stdc++.h>
int main()
{
 
int T,Smax,j;
char a[10002];
int x=0;
scanf("%d",&T);
 
while(T>0)
{
int p=0;
int y=0;
x++;
 
scanf("%d",&Smax);
scanf("%s",a);
 
int z=a[0];
for(j=1;j<=Smax;j++)
{
 
if(z<j+48)
{
y++;
z++;
}
z+=a[j]-48;
 }
 
printf("Case #%d: %d\n",x,y);
T--;
}
return (0);
}