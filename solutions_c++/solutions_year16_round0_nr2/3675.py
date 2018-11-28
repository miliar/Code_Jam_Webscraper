#include <bits/stdc++.h>
using namespace std;
int main()
{   int t,r=1;

	#ifndef ONLINE_JUDGE
	    freopen("input.txt","r",stdin);
	     //freopen("out.txt","w",stdout);
	  #endif

	cin>>t;
	while(t--)
	{  
      string s; long long ans = 0;
      cin>>s;

     for(int i=1;i<s.size();i++)
     {
        if(s[i-1]!=s[i])
          ans++;
     }

     if(s[s.size()-1] =='-')
       ans++;

      cout<<"Case #"<<r<<": "<<ans<<endl;
      r++;
	}
	return 0;
}