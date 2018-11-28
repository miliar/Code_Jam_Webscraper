#include<bits/stdc++.h>
using namespace std;

int i,t,t1,rs,n,last;
string s,curr;

int main()
{
  ifstream cin("input.txt");
  ofstream cout("output.txt");

  ios_base::sync_with_stdio(0); cin.tie(0);

  cin>>t1;
  for(t=1;t<=t1;++t)
  {
    cout<<"Case #"<<t<<": ";

    cin>>s; rs=0; curr.clear(); n=s.length();

    for(i=0,last=n-1;i<n;++i) curr+='+';

    while(curr!=s)
    {
      while(last>=0 && curr[last]==s[last]) --last;

      reverse(curr.begin(),curr.begin()+last+1);

      for(i=0;i<=last;++i)
      if(curr[i]=='+') curr[i]='-';
      else curr[i]='+';

      ++rs;
    }

    cout<<rs<<'\n';
  }

 return 0;
}
