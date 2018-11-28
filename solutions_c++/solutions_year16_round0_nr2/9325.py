#include <bits/stdc++.h>
using namespace std;
int main ()
{

  freopen ("myfile.txt","w",stdout);
  freopen ("input.txt","r",stdin);
  int t,p=1;cin>>t;
  while(t--)
  {
	  int c=0;
	  string s;
	  cin>>s;
	  int l=s.length();
	  for(int i=0;i<l-1;++i)
	  {
	  	if(s[i]!=s[i+1]) c++;
	  }
	  if(s[l-1]=='-') cout<<"Case #"<<p<<": "<<c+1<<endl;
	  else cout<<"Case #"<<p<<": "<<c<<endl;
	  p++;
  }
  return 0;
}

	

