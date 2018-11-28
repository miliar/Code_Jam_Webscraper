#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<conio.h>

int main()
{
    int aaa,y,i,j,n=1,count=0,k,flag;
    double c,f,x,a[10000][4],temp;
    freopen("B-small-attempt2.in","r",stdin);
    freopen("small.out","w",stdout);
    scanf("%d",&aaa);
    k=1;
    while(k<=aaa)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        temp=2.0000000;
        a[0][0]=(double)temp;
        a[0][1]=(double)c/(double)temp;
        a[0][2]=(double)c/(double)temp;
        a[0][3]=(double)x/(double)temp;
        i=1;
        flag=1;
        while(1)
        {
            temp=temp+f;
            a[i][0]=(double)temp;
            a[i][1]=(double)c/(double)temp;
            a[i][2]=((double)c/(double)temp)+a[i-1][2];
            a[i][3]=((double)x/(double)temp)+a[i-1][2];
            if(a[i-1][3]<=a[i][3])
                break;
            i++;

        }
        printf("Case #%d: ",k);
        printf("%0.7lf",a[i-1][3]);
        printf("\n");
        k++;
    }
    return 0;
}
