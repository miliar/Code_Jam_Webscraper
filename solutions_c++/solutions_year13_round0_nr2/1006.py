#include<iostream>
#include<stdio.h>
using namespace std;
int n,m;
int arr[110][110];
void findmin(int *x,int *y)
{
     int mini,i,j;
     mini=arr[0][0]; *x=0; *y=0;
     for(i=0;i<n;i++)
       for(j=0;j<m;j++)
       {
          if(arr[i][j]<mini)
          {
             mini=arr[i][j];
             *x=i; *y=j;
          }
       }
}
int row(int x,int y)
{
    int i,v=arr[x][y];
    for(i=0;i<m;i++)
    {
       if(arr[x][i]!=150 && arr[x][i]>v)
          return 0;
    }
    for(i=0;i<m;i++)
       arr[x][i]=150;
    return 1;
}
int col(int x,int y)
{
    int i,v=arr[x][y];
    for(i=0;i<n;i++)
    {
       if(arr[i][y]!=150 && arr[i][y]>v)
          return 0;
    }
    for(i=0;i<n;i++)
       arr[i][y]=150;
    return 1;
}
int final()
{
    int i,j;
    for(i=0;i<n;i++)
      for(j=0;j<m;j++)
        if(arr[i][j]!=150) return 0;
    return 1;
}
int main()
{
    freopen("inplawn.txt","r",stdin);
    freopen("outlawn.txt","w",stdout);
    int tc,t,i,j,x,y,flag;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
          for(j=0;j<m;j++)
             scanf("%d",&arr[i][j]);
        int done=0;
  //      printf("%d %d\n",n,m);
        while(!done)
        {
            findmin(&x,&y);
    //        printf("Min = %d %d\n",x,y);
            flag=0;
            if(row(x,y))
            { flag=1; } //printf("Row\n"); }
            else if(col(x,y))
            { flag=1; } //printf("Col\n"); }
            if(flag==0)
               break;
      /*      printf("st:\n");
            for(i=0;i<n;i++)
            {
              for(j=0;j<m;j++)
                printf("%d ",arr[i][j]);
              printf("\n");
            }*/
            done=final();
        }
       // printf("%d\n",done);
        if(done==0)
          printf("Case #%d: NO\n",tc);
        else
          printf("Case #%d: YES\n",tc);
    }
    return 0;
}
