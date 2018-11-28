//In the name of God
#include <iostream>
#include <set>
using namespace std;

void solve()
{
  set<int> f,s;
  int a,x; cin>>a; 
  for(int i=1;i<=4;++i)
    for(int j=1;j<=4;++j)
      {
	cin>>x;
	if(i==a)
	  f.insert(x);
      }
  cin>>a;
  for(int i=1;i<=4;++i)
    for(int j=1;j<=4;++j)
      {
	cin>>x;
	if(i==a)
	  s.insert(x);
      }
  int cnt=0,ans=0;
  for(int i=1;i<=16;++i)
    if(f.find(i)!=f.end() and s.find(i)!=s.end())
      {cnt++; ans=i;}
  if(cnt<1)
    cout<<"Volunteer cheated!"<<endl;
  else if(cnt==1)
    cout<<ans<<endl;
  else
    cout<<"Bad magician!"<<endl;
}

int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;++i)
    {
      cout<<"Case #"<<i<<": ";
      solve();
    }
  return 0;
}
