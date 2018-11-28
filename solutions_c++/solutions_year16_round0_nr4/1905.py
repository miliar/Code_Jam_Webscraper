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


int main()
{
freopen("D-small-attempt2.in","r",stdin);
	freopen("16Ds.out","w",stdout);
ll t,i;
cin>>t;
for(i=1;i<=t;i++)
{
ll k,c,s,g=1;
cin>>k>>c>>s;
cout<<"Case #"<<i<<": ";
while(k--)
cout<<k+1<<" ";
cout<<endl;
}

   return 0;

}


