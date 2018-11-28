#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>

using namespace std;
typedef long long int ll;

ll NUM = 10000001;

int nums[10000001];
ll numsq[10000001];
int numcnt[10000001];

bool palin(ll num){
	ll numCopy=num;
	ll rem=0,sum=0;
	while(num!=0)   
    	{
    	    rem=num%10;
    	    num=num/10;
    	    sum=sum*10+rem;
    	}
    	if(numCopy==sum)
    		return true;
    	else
    		return false;
}


int main()
{
	memset(nums,0,sizeof (nums));
	memset(numsq,0,sizeof (numsq));
	memset(numcnt,0,sizeof (numcnt));
	ll i;
	for(i=1;i<NUM;i++)
	{
		if(palin(i)==true)
		{
			nums[i]=i;
			ll val=i*i;
			if(palin(val)==true)
				numsq[i]=val;
		}
	}
	
	numcnt[0]=0;
	numcnt[1]=1;

	for(i=2;i<NUM;i++)
	{
		if(numsq[i]!=0)
			numcnt[i]=numcnt[i-1]+1;
		else
			numcnt[i]=numcnt[i-1];
	}

	int T,t;
	cin>>T;
	for(t=1;t<=T;t++)
	{
	ll A,B;
	cin>>A>>B;
	ll srA=ceil((long double)sqrt (A));
	ll srB=floor((long double)sqrt (B));
	
	ll ans=numcnt[srB]-numcnt[srA-1];
	cout<<"Case #"<<t<<": "<<ans<<endl;
	}
return 0;
}	
