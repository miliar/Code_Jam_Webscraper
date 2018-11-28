#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 100000000000000000
ll seting(ll N,int pos)
{
     return N = N|(1LL<<pos);
}
ll reset(ll N,int pos)
{
      return N = N&~(1LL<<pos);
}	
bool chek(ll N,int pos)
{
     return (bool) (N&(1LL<<pos));
}
ll len;
ll base(ll num,ll b)
{
	int i,tmp;
	ll tt,ans;

	tmp = 0;
	tt= 1;
	ans = 0;
	for(i=0;i<len;i++)
	{
		 if(chek(num,i)==1)
		 {
		 	//tmp++;
		 	ans+=tt;
		 }
		 tt*=b;
	}
	
  return ans;
}
bool f;
ll cal(ll num)
{
	ll sqr,i;
	sqr = sqrt(num);
	for(i=2;i<=sqr;i++)
	{
		if(num%i==0)
		{
		
			return i;
		}
	}
	
	return 0;
}
vector<ll>res;
int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
	ll t,tcase,k,n,st,cn,i,num,j,div,l;
	scanf("%lld",&tcase);
	for(t=1;t<=tcase;t++)
	{
	   scanf("%lld %lld",&len,&k);
	   
	   st = 32769;
	   //st = 33;
	   cn = 0;
	   printf("Case #%lld:\n",t);
	   for(i=st;cn<k;i+=2)
	   {
	   	   f = 0;
	   	   res.clear();
	   	   for(j=2;j<=10;j++)
	   	   {
	   	       num = base(i,j);	
	   	       div = cal(num);
	   	       if(div==0)
	   	       {
	   	          f= 1;
					 break;	
			   }
			   else
			   {
			   	  res.push_back(div);
			   }
		   }
		  // cout<<i<<" "<<res.size()<<" "<<f<<endl;
		   if(f==0)
		   {
		   	  for(j=len-1;j>=0;j--)
		   	  {
		   	  	if(chek(i,j)==1)
		   	  	{
		   	  		printf("1");
				}
				else
				   printf("0");
			  }
			  printf(" ");
			  l = res.size();
			  for(j=0;j<l;j++)
			  printf("%lld ",res[j]);
			  cn++;
			  printf("\n");
		   }
		   
	   }
	   
	}
	
	return 0;
}

