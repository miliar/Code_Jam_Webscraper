#include<iostream>
#include<string>

using namespace std;

int main()
{
    int t,u;
    string s;
    cin>>t;
    for (int o=1;o<=t;o++)
    {
      cin>>u>>s;
      int ans = 0, st = s[0] - '0';
      for (int i=1;i<=u;i++)
      {
	if (s[i] > '0') 
	{
	  ans += max(0, i - st);
	  st += max(0, i - st);
	}
	st += s[i] - '0';
      }
      cout<<"Case #"<<o<<": "<<ans<<endl;
    }
    return 0;
}