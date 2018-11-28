#include<cstdio>
#include<cassert>

long long calc(int n)
{
long long ans=0,t;
int a[10]={0},c=10;    
while(c)
    {
    ans++;
    t= ans*n;
    
    while(t)
        {
        if(!a[t%10]) {a[t%10]=1;c--;}
        t/=10;    
        }
    if(ans>1000) return -1;
    }
return ans;
}

int main()
{
int i,j,k,l,n,t,T;
long long m;
scanf("%d",&T);
for(t=1;t<=T;t++)
    {
    scanf("%d",&n);
    m=calc(n);
    if(m!=-1)
    printf("Case #%d: %lld\n",t,m*n);    
    else
        printf("Case #%d: INSOMNIA\n",t);    
    }    

//long long ans;
//j=0;
//for(i=1;i<=1000000;i++)
 //   {
  //  m = calc(i);
  //  if(j<m) j=m;
  //  printf("%d: %d : %lld\n",i,m,i*m);    
  //  }
//printf("MAX = %d\n",j);
return 0;    
}
