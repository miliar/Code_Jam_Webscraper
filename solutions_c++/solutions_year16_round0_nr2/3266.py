#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define MOD 1e9+7
int main()
{
  int t;
  cin>>t;
  for(int k=1;k<=t;k++)
  {
     string s;
     cin>>s;
     int i=0;
     int c=0;
     bool f=0;
     while(i<s.length())
     {
     	f=0;
     	while(i<s.length() && s[i]=='-')
     	{
     		i++;
     		if(f==0)
            {
            	  f=1;
                 c++;
            }
	 	}
        while(i<s.length() && s[i]=='+')
        {
        	i++;
        }
     }
   	  cout<<"Case #"<<k<<": ";
     if(s[0]=='-')
	  cout<<2*c-1<<endl;
	  else cout<<2*c<<endl;     
  }
  return 0;
}
