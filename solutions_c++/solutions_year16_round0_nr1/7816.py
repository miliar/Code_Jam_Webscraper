#include<iostream>
#include<stdio.h>
using namespace std ;
int main()
{
    int t,d,i=1,i0=1,i1=1,i2=1,i3=1,i4=1,i5=1,i6=1,i7=1,i8=1,i9=1,temp=0;
    int n,j=1;
    FILE *fp;
    fp=fopen("lll.txt","w");
    cin>>t;
    while(t--)
    {
    cin>>n;
    i=1;i0=1;i1=1;i2=1;i3=1;i4=1;i5=1;i6=1;i7=1;i8=1;i9=1;
    if(n==0)
    {
        fprintf(fp,"Case #%d: INSOMNIA\n",j);
        j=j+1;
    }

    else
    {
        temp=n;
        while(temp>0)
        {
           d=temp%10;
           switch (d)
           {
           case 0:i0=0;break;
           case 1:i1=0;break;
           case 2:i2=0;break;
           case 3:i3=0;break;
           case 4:i4=0;break;
           case 5:i5=0;break;
           case 6:i6=0;break;
           case 7:i7=0;break;
           case 8:i8=0;break;
           case 9:i9=0;break;
           default:
               break;
                       }
           temp=temp/10;
           if((i0+i1+i2+i3+i4+i5+i6+i7+i8+i9)==0)
           {
               fprintf(fp,"Case #%d: %d\n",j,(n*i));

               j=j+1;
               break;
           }
           if(temp==0)
           {
               i++;
               temp=n*i;
           }
        }
    }
    }


    }
