#include<bits/stdc++.h>
#define MAX 100000
#define pb push_back
#define forn(i,n) for(i=1;i<=n;i++)
#define fornb(i,n) for(i=n;i>=1;i--)
#define for0(i,n) for(i=0;i<n;i++)
#define for0b(i,n) for(i=n-1;i>=0;i--)

typedef long long ll;
typedef double lf;

using namespace std;

int n;set<int> S;

void rd_1()
{
  int i;
  for0(i,10){
    S.insert(i);
  }
  cin>>n;
}

int main()
{
  ios::sync_with_stdio(0);
  int i,j,t;
  cin>>t;
  forn(i,t)
  {
    rd_1();int ct=1;ll temp;
    if(n==0){
      cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
      continue;
    }
    while(true)
    {
      temp=ct*n;int digit;
      while(temp!=0)
      {
	digit=temp%10;
	if(S.find(digit)!=S.end())
		S.erase(digit);
	temp/=10;
      }
      if(S.empty()){
	cout<<"Case #"<<i<<": "<<(ll)ct*n<<endl;
	break;
      }
      ct++;
    }
  }
  return 0;
}
