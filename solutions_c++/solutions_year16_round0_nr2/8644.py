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

int n;string s,s1;

void rd_1()
{
  s.clear();
  s1.clear();
  cin>>s;
}

int main()
{
  ios::sync_with_stdio(0);
  int i,j,t;
  cin>>t;
  forn(i,t)
  {
    rd_1();
    int l=s.length();int l1=0;
    for0(j,l-1)
    {
      if(s[j] == s[j+1]) 
	continue;
      else{
	s1[l1]=s[j];
	l1++;
      }
    }
    s1[l1]=s[l-1];l1++;
    if(l1%2 == 0)
    {
      if(s1[0] == '-')
	cout<<"Case #"<<i<<": "<<l1-1<<endl;
      else
	cout<<"Case #"<<i<<": "<<l1<<endl;
    }
    else{
      if(s1[0] == '-')
	cout<<"Case #"<<i<<": "<<l1<<endl;
      else
	cout<<"Case #"<<i<<": "<<l1-1<<endl;
    }
  }
  return 0;
}
