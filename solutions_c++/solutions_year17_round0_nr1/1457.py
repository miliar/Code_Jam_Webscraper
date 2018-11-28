#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long int
#define M(x) M(x%MOD + MOD)
#define _pb push_back
#define ff first
#define ss second
#define _mp make_pair
#define sc(x) scanf("%lld",&x)

ll mul(ll x,ll y)
{ ll ans=1;
  while(y>0)
  { if(y&1)
	ans=(ans*x)%MOD;

	x=(x*x)%MOD;
	y/=2;
  }
  return ans;
}

//........................................................................................................................................................


int main()
{ freopen("A-large.in","r",stdin);
  freopen("out2.txt","w",stdout);
  
  ll t,c;
  cin>>t;

  for(c=1;c<=t;c++)
  { string str;
	ll cnt=0,i,j,k;
  	cin>>str>>k;
  	ll l=str.size();
  	
  	for(i=0;i<l;i++)
  	if(str[i]=='-' && i+k-1<l)
  	{ ++cnt;
	  for(j=0;j<k;j++)
	  if(str[j+i]=='-')
	  str[j+i]='+';
	  else
	  str[j+i]='-';
	}

  
  ll flag=0;
  for(i=0;i<l;i++)
  if(str[i]=='-')
  {flag=1;
   break;
  }
  
  if(flag==1)
  cout<<"Case #"<<c<<": "<<"IMPOSSIBLE\n";
  else
  cout<<"Case #"<<c<<": "<<cnt<<"\n";
  }
  
   return 0;
}
