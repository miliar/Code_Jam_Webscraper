#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
#define try1(a) cout<<a<<endl;
#define try2(a,b) cout<<a<<" "<<b<<" "<<endl;
#define try3(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl;
#define try4(a,b,c,d) cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;
 
 
 
using namespace std;
 
int main() {

freopen("B-large.in","r",stdin);

freopen("out4.txt","w",stdout);

ll t;
cin>>t;
ll k1=0;
while(t--)
{
k1++;

ll n;
cin>>n;
ll arr[1005]={};
ll max=-1;
for(ll i=0;i<n;i++)
	{
		cin>>arr[i];
	
		if(arr[i]>max)
			max=arr[i];
	}
ll ans=1000005;
if(max==1)
	ans=1;
else if(max==2)
	ans=2;
else
{

for(ll i=1;i<=max;i++)
{
	ll t1=i;
	for(ll j=0;j<n;j++)
	{
		if(arr[j]>i)
		{
			if(arr[j]%i!=0)
                    t1=t1+(arr[j]/i);
                else if(arr[j]%i==0)
                    t1=t1+(arr[j]/i-1);


		}
	}
	ans=min(ans,t1);

}

}



// Case #1: 0
cout<<"Case #"<<k1<<": "<<ans<<endl;
}


 return 0;
}