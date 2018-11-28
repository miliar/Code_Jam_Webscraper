#include<stdio.h>
#include<conio.h>
#include<iostream.h>
int main()
{
    freopen("B-large.in","r",stdin);
     freopen("outp.in","w",stdout);
     int T,i;
     cin>>T;
     double C,F,X,time,a,b,c,d;
     
     for(i=0;i<T;i++)
     {
     cin>>C;
     cin>>F;
     cin>>X;
     
     c=0;
    time=0.0;
     a=X/2;
     b=(C/2);
     d=(X/(2+F));
     while((b+d)<a)
     {
     time+=b;
     a=(a*(2+(c*F))/(2+((c+1)*F)));
     b=(b*(2+(c*F))/(2+((c+1)*F)));
     d=(d*(2+((c+1)*F))/(2+((c+2)*F)));
     c++;
     }
     time+=a;
     printf("Case #%d: %0.7lf\n",i+1,time);
     
     }
       
     getch();
     return 0;
     }
