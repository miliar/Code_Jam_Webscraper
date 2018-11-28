#include<cstdio>
#include<cstring>
int a[15],t,n,cas,nu;
inline void get(int num)
{
  for(;num;num/=10)
    a[num%10]=1;
}
inline bool check(int ama)
{
  for(int i=0;i<10;i++)
    if(!a[i])
      return false;
  return true;
}
int main()
{
  //freopen("1.txt","w",stdout);
  scanf("%d",&t);
  while(t--)
  {
  	scanf("%d",&n);
  	printf("Case #%d: ",++cas);
  	if(n==0){puts("INSOMNIA");continue;}
  	memset(a,0,sizeof(a));
  	for(int j=1;;j++)
  	{
  	  nu=n*j;
  	  get(nu);
  	  if(check(nu))
	  {
	  	printf("%d\n",n*j);
	  	break;
	  }
    }
  }	
  return 0;
}
