#include <iostream>
#include<cmath>
#include<cstdio>
using namespace std;
#define lld long long int
lld ar[200],br[200],cr[200],ans,n;
void rec(lld v,lld a)
{
	lld i;
	if(v==n)
	{
		lld count=0,b;
		//cout<<a;
		b=a;
		while(b>0)
		{
			//cout<<a;
			b-=(b& -b);
			count++;
			//cout<<count<<" ";
		}
		//cout<<count;
		if(count<ans)
		ans=count;
		return ;
	}
	//lld flag=0;
	for(i=0;i<n;i++)
	{
		if(cr[i]==0&&((ar[i]^br[v])==a))
		{
			//cout<<v<<i<<a<<" ";
			cr[i]=1;
			rec(v+1,a);
			//flag=1;
			cr[i]=0;
		}
	}
	return ;
}
int main() 
{
	lld t,i,j,l,a,k;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n>>l;
		for(i=0;i<n;i++)
		{
			cin>>a;
			ar[i]=0;
			for(k=0;a>0;k++)
			{
				if(a%10==1)
				ar[i]+=pow(2,k);
				a/=10;
			}
			//cout<<ar[i]<<" ";
		}
		//cout<<"        ";
		for(i=0;i<n;i++)
		{
			cin>>a;
			br[i]=0;
			for(k=0;a>0;k++)
			{
				if(a%10==1)
				br[i]+=pow(2,k);
				a/=10;
			}
			//cout<<br[i]<<" ";
		}
		//if(ar[2]^br[1]==2)
		//cout<<"boom";
		//cout<<br[1]<<" ";
		ans=200;
		for(i=0;i<n;i++)
		{
			a=(ar[i]^br[0]);
			//cout<<a<<" ";
			cr[i]=1;
			rec(1,a);
			cr[i]=0;
		}
		if(ans==200)
		cout<<"Case #"<<j<<": NOT POSSIBLE\n";
		else
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}