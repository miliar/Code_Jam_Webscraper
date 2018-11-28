#include<stdio.h>
#include<conio.h>
void main()
{ clrscr();  float sec;int z; float tsec1,tsec2,sec2;
int t; float c,f,x; float r=2.0;
scanf("%d",&t);

for(z=1;z<=t;z++)
{   r=2.0;
  sec=0.0;
scanf("%f%f%f",&c,&f,&x);
 tsec1=x/r;
sec=sec+(c/r);
  r=r+f;



sec2=x/r;
tsec2=sec+sec2;
if(tsec2<tsec1)
{
while(tsec2<tsec1)
{


tsec1=tsec2;



sec=sec+(c/r);
r=r+f;
sec2=x/r;
tsec2=sec+sec2;
}
 printf("Case #");
printf("%d",z);
printf(": ");
printf("%f",tsec1);
printf("\n");
}
else
{
 printf("Case #");
printf("%d",z);
printf(": ");
printf("%f",tsec1);
printf("\n");
}
}getch();
}
