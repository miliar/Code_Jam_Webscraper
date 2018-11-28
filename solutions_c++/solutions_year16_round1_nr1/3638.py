#include<bits/stdc++.h>
#define MAX 100000
#define pb push_back
#define pf push_front
#define forn(i,n) for(i=1;i<=n;i++)
#define fornb(i,n) for(i=n;i>=1;i--)
#define for0(i,n) for(i=0;i<n;i++)
#define for0b(i,n) for(i=n-1;i>=0;i--)

typedef long long ll;
typedef double lf;

using namespace std;

int t;string S;deque<char> D;

void rd_1()
{
  cin>>t;
}

int main()
{
  ios::sync_with_stdio(0);cin.tie(NULL);
  int i,j;
  rd_1();
  forn(j,t){
    cin>>S;
    D.pb(S[0]);
    forn(i,S.length()-1)
    {
      if(S[i] >= D.front())
	D.pf(S[i]);
      else
	D.pb(S[i]);
    }
    cout<<"Case #"<<j<<": ";
    while(!D.empty())
    {
      cout<<D.front();
      D.pop_front();
    }
    cout<<"\n";
  }
  return 0;
}
