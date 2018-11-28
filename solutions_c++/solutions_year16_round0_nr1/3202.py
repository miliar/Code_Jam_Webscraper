#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define MOD 1e9+7
set<int> s;
void add(ll n)
{
	while(n>0)
	{
		s.insert(n%10);
		n/=10;
	}	
}
int main()
{
  int t;
  cin>>t;
  for(int k=1;k<=t;k++)
  {
     	ll n;
        cin>>n; 	
        if(n==0)
        {
     	     cout<<"Case #"<<k<<": ";
        	 cout<<"INSOMNIA"<<endl;
        	 continue;
        }
       add(n);
      ll int i=2;
	  while(s.size()!=10) 
      {
      	add(i*1LL*n);
      	i++;
      }
	  cout<<"Case #"<<k<<": ";
      cout<<(i-1)*1LL*n<<endl; 
      s.clear();
  }
  
  return 0;
}
