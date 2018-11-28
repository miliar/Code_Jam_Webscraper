#include<bits/stdc++.h>
#define ll long long
#define sc1ll(x) scanf("%lld",&x)
#define sc2ll(x,y) scanf("%lld%lld",&x,&y)
using namespace std;
vector<ll> arr(15);
ll modular_exp(ll num,ll pow)
{
    if(pow==0)
        return 1;
    else if(pow==1)
        return num;
    else if(pow%2==0)//if power is even
        return modular_exp((num*num),pow/2);
    else//if power is odd
        return (num*modular_exp(num*num,pow/2));
}

ll find_fact(ll num)
{
	for(ll i=2;(i*i)<=num;i++)
	{
		if(num%i==0)
			return i;
	}
	return num;
}
bool prime_check(ll num)
{
	for(ll i=2;(i*i)<=num;i++)
	{
		if(num%i==0)
			return false;
	}
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	ll n,val,test,count,limit,i,j,k,cnt,index,sum,final_total;
	scanf("%lld",&test);
	for(k=1 ; k<=test ; k++)
	{
		val=0;
		sc2ll(n,final_total);
		limit=pow(2,14);
		count=pow(2,15)+pow(2,0);
		printf("Case #%lld: \n",k);
		for(i=0 ; i<limit ; i+=1)
		{
			bool valid=true;
			for(j=2 ; j<=10 ; j+=1)
			{
				cnt=count+(i<<1);
				sum=index=0;
				while(cnt)
				{
					if(cnt&1)
						sum=sum+modular_exp(j,index);
					index+=1;
					cnt>>=1;
				}
				if(prime_check(sum)==true)
					arr[j]=0;
				else
					arr[j]=find_fact(sum);
				if(arr[j]==0)
				{ valid=false;break; } 
			}
			if(valid==true)
			{
				val+=1;
				cnt=count+(i<<1);
				for(j=15;j>=0;j-=1)
				{
					if( ( cnt & (1<<j) ) )
						printf("1");
					else
						printf("0");
				}
				printf(" ");			
				for(j=2;j<=10;j+=1)
				{
					if(j==10)
						printf("%lld\n",arr[j]);
					else
						printf("%lld ",arr[j]);
				}
			}
			if(val==final_total)
				break;
		}
	}
	return 0;
}
