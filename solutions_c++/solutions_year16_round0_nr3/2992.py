#include<bits/stdc++.h>
using namespace std;
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define INF 99999999
#define N 1001
#define ll long long
#define llu unsigned long long 
#define MOD 1000000007
#define gcd __gcd
#define fill(A,v) memset(A,v,sizeof(A))
ll arr[N];
ll hold[N],val[N],str[N];
int len=0;
ll po(ll a,ll b)
{
	ll x=1,y=a;
	while(b>0)
	{
		if(b%2==1)
		  x=x*y;
		y=y*y;
		b=b/2;
	}
	return x;
}
int prime(ll num)
{
   int c=0;
   ll i;
   if (num==2)
        c=0;
   else if (num%2==0)
   {
        c=1;
        str[len++]=2;
   }     
   else
   {
   ll k=sqrt(num);
   for(i=3;i<=k;i+=2)
   {
   	  if(num%i==0)
   	  {
   	  	c=1;
   	  	break;
   	  }
   }
   str[len++]=i;
   }
   return c;
}
void seti(int n,int ju)
{	
	 int e=n;
	 ll i,k,j;
	 int flag=0,cnt=0;
	 n=n-2;
     ll p=po(2,n);
	 for(i=0;i<p;i++)
	 {
	 	 flag=0;
	 	 len=0;
	 	 if(cnt==ju)
	 	   break;
	 	 for(j=2;j<=10;j++)
	 	 {
	 	   hold[j]=1;
	 	   val[j]=0;
	 	 }  
         for(j=0;j<n;j++)
	     {
	 	 if(i&(1<<j))
           arr[j+1]=1;
         else
           arr[j+1]=0;
	     }
	     arr[0]=arr[e-1]=1;
	     for(j=e-1;j>=0;j--)
	     {
	     	 for(k=2;k<=10;k++)
	 	     {
	 	     	 if(arr[j]==1)
	 	     	  val[k]+=hold[k];
	 	     	 hold[k]=hold[k]*k;
	 	     }
	     }
	     for(j=2;j<=10;j++)
	     {
	     	if(prime(val[j])==0)
	     	{
                flag=1;
                break;
	     	}   
	     }
	     if(flag==0)
	     {
	     	for(j=0;j<e;j++)
	     	   printf("%lld",arr[j]);
	     	   printf(" ");
	     	for(j=0;j<len;j++)
	     	  printf("%lld ",str[j]);
	     	printf("\n");  
	     	cnt++;
	     }
	 }
}
int main()
{
	int t,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		int n,j;
		scanf("%d%d",&n,&j);
		printf("Case #%d:\n",k);
		seti(n,j);
	}
	return 0;
}	