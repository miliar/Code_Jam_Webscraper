#include<cstdio>

int a[1003],n;


int verify(int m)
{
int i,j,k=0;
for(i=0;i<n;i++)
    {
    k+= a[i]/m - (a[i]%m == 0);    
    }    
return k+m;    
}

int main()
{
int i,j,k,t,T,m;

scanf("%d",&T);    
for(t=1;t<=T;t++)
    {
    scanf("%d",&n); 
    m=0;
    for(i=0;i<n;i++)
        {
        scanf("%d",&a[i]);
        if(m<a[i]) m=a[i];
        }   
    k= m;
    for(i=1;i<=m;i++)
        {
        j=verify(i);
      //  printf("%d %d\n",i,j);
        if(k>j) k=j;
        }
    printf("Case #%d: %d\n",t,k);
    }
    
return 0;    
}
