#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll powmod(ll base, ll exponent)
{ ll ans=1;
while(exponent)
{ while(exponent%2==0)
{base=(base*base);
exponent/=2;
}
exponent--;
ans=(ans*base);
}
return ans;
}

ll cnt=0;
int main()
{
	//freopen("A-large-practice.in","r",stdin);
	freopen("16Cll.out","w",stdout);
ll t,i,j,k,base;

cout<<"Case #"<<1<<":"<<endl;
for(i=(1<<15)+1;i<(1<<16);i+=2)
{

	  vector<ll> v;
		for(base=2;base<11;base++)
		{ll temp=0;
			for(j=15;j>=0;j--)
			if(i&1<<j)
			{
			     temp+=powmod(base,j);
				 
			}
			//cout<<temp<<endl;
			bool flag=false; 
		for(k=3;k<=ll(sqrt(temp));k+=2)
		{
			if(temp%k==0)
			{
			v.push_back(k);
			//cout<<v.size()<<endl;
			flag=true;
			break;
			}
			
			
		}
		if(flag)
		continue;
		}
		if(v.size()==9)
		{
			for(k=15;k>=0;k--)
			cout<<(i&1<<k?1:0);
			for(k=15;k>=0;k--)
			cout<<(i&1<<k?1:0);
			cout<<" ";
			for(k=0;k<9;k++)
			cout<<v[k]<<" ";
			cout<<endl;
			v.clear();
			cnt++;
		}

if(cnt==500)
return 0;
}

   return 0;

}


