#include<stdio.h>
#include<iostream>
using namespace std;

int a[105][105];
int r[105];//stores max of each row
int c[105];
int n,m;

inline int mi(int a,int b)
{
    return a>b?b:a;
}

bool func()
{
    int i,j;
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
          if(a[i][j]!=mi(r[i],c[j]))
              return 0;

    return 1;
}

int main()
{
    int i,j,d,xmin,ymin,t,w;
   scanf("%d",&t);
   for(w=1;w<=t;w++)
   {
        scanf("%d%d",&n,&m);
        for(i=0;i<102;i++) r[i]=c[i]=0;
    for(i=0;i<n;i++)
    {

          for(j=0;j<m;j++)
    {
        scanf("%d",&a[i][j]);
        if(a[i][j]>r[i]) r[i]=a[i][j];
        if(a[i][j]>c[j]) c[j]=a[i][j];

    }
    }


     if(func()) printf("Case #%d: YES\n",w);
     else  printf("Case #%d: NO\n",w);

   }



}
