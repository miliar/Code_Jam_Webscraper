#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define fast() {cin.sync_with_stdio(false);cin.tie(false);cout.tie(false);}
#define pb push_back
#define mp make_pair
#define  MAX 1005
ll arr[MAX];
int main()
{
  fast();
  //freopen("B-large.in","r+",stdin);
  //freopen("output2.txt","w+",stdout);
  int t;
  cin>>t;
  int test=0;
  while(t--)
  {
    test++;
    ll D;
    cin>>D;
    ll max_v = 0;
    for(int i=1;i<=D;i++)
    {
      cin>>arr[i];
      if(arr[i]>max_v) max_v=arr[i];
    }
    ll val=max_v;
    for(ll i=1;i<=max_v;i++)
    {
      ll p=0,q=0;
      for(int j=1;j<=D;j++)
      {
     	if(arr[j]>i)
     	{
       		p += (arr[j]/i);
			if(arr[j]%i!=0)
			  p+=1;
			p--;   
       		q=max(q,i);
     	}
     	else q=max(q,arr[j]);
      }
       p+=q;
      if(p<val)val=p;
    }
    cout<<"Case #"<<test<<": "<<val<<endl;
  }
  return 0;
}
