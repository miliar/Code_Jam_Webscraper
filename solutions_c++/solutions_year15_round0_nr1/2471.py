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

freopen("inp.txt","r",stdin);

freopen("out.txt","w",stdout);
ll t;
cin>>t;
ll k=0;
while(t--)
{
k++;
ll n;
cin>>n;
string str;
cin>>str;
ll ans=0,sum=str[0]-48;
// try1(sum);
for(ll i=1;i<str.length();i++)
{ 
	if(str[i]!=0)
	{
  if(sum<i)
  {
  	ans+=i-sum;
  	sum+=i-sum;
  	sum+=str[i]-48;
  }
  else
  {
  	sum+=str[i]-48;
  }
}

}
// Case #1: 0
cout<<"Case #"<<k<<": "<<ans<<endl;
}


 return 0;
}