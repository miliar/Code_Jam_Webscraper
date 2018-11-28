#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for(int q=1;q<=t;q++)
    {
      string s;
      cin>>s;
      int a=0;
      for(int i=1;i<s.size();i++)
	if(s[i]!=s[i-1])
	  a++;
      if(s[s.size()-1]=='-')
	a++;
      cout<<"Case #"<<q<<": "<<a<<endl;
    }
}
