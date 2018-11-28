#include<stdio.h>
#include<math.h>
int a[10000000];
int hu(int x)
{int r=0,t=1;
    if(x<10)return 1;
    else {for(int i=1;;i++)
    {a[r++]=x%10;
    x=x/10;
    if(x==0)break;
    }for(int i=0;i<=r/2&&r-1-i>=r/2;i++)
          if(a[i]!=a[r-1-i]){t=-1;break;}
          return t;}
}
int main()
{int i,n,h1,k=0,a,b;//double h;
    scanf("%d",&n);
    while(n--)
    {int q=0;k++;
       scanf("%d%d",&a,&b);
        for(i=a;i<=b;i++)
              {if(hu(i)==-1)continue;
              h1=sqrt(i);
              //h1=(int)h;
              if(h1*h1==i&&hu(h1)==1)q++;}

          printf("Case #%d: %d\n",k,q);



    }return 0;
}
