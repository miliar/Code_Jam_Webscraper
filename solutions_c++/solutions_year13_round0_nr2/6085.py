#include<stdio.h>
#include<stdlib.h>
 
int arr[100][100];
 
int fun(int i,int j,int n,int m)
{
    int f1,f2,max,ind;
    f1 = 1;
    f2 = 1;
    max = arr[i][j];
    for(ind=0;ind<n;ind++)
    {
        if(arr[ind][j] > max) f1=0;
    }
    
    for(ind=0;ind<m;ind++)
    {
        if(arr[i][ind] > max) f2=0;
    }
    
    if((f1 ==0) && (f2==0)) return 0;
    else return 1;
}
 
int main()
{
    int t,n,m,i,j,k,flag1,flag2;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&n);
        scanf("%d",&m);
        // input the matrix
        for(j=0;j<n;j++)
        {
          for(k=0;k<m;k++)
          {
              scanf("%d",&arr[j][k]);  
              
          }
        }
        
        flag1 = 1;
        flag2 =1;
        for(j=0;j<n;j++)
        {
            for(k=0;k<m;k++)
            {
                flag1 = fun(j,k,n,m);
                if(flag1==0) {flag2 = 0;break;}
            }
            
            if(flag2 ==0)break;
        }
        
        if(flag1 ==0) printf("Case #%d: NO\n",i+1);
        else printf("Case #%d: YES\n",i+1);
    }
    
    return 0;
}
