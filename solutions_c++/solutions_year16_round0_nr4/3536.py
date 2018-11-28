#include<bits/stdc++.h>
using namespace std;

int i,t,t1,k,c,s;

int main()
{
  ifstream cin("input.txt");
  ofstream cout("output.txt");

  ios_base::sync_with_stdio(0); cin.tie(0);

  cin>>t1;
  for(t=1;t<=t1;++t)
  {
    cout<<"Case #"<<t<<": ";

    cin>>k>>c>>s;

    for(i=1;i<=s;++i) cout<<i<<" \n"[i==s];
  }

 return 0;
}
