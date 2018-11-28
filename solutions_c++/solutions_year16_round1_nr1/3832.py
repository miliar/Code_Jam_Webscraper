#include<bits/stdc++.h>
using namespace std;


int main()
{
	int t,k;
	string s;
	cin>>t;
	k=1;
	while(t--)
	{
          cin>>s;
          string ans; int j=0; int l=1,cur=0;
          string mystring="" ;
          	      mystring+=s[0];
          ans.insert(j,mystring);
          for(int i=1;i<s.length();i++)
          {    
          	 if( ans[0] <= s[i])
          	 {    mystring="" ;
          	      mystring+=s[i];
          	      ans.insert(0,mystring);
          	 	 l++;
          	 	//cur=cur;
          	 	}
          	 else{
          	 	ans=ans+s[i];
               // cur=l;
                 l++;
          	 }
          	
          

          }
          	cout<<"Case #"<<k++<<": "<<ans<<endl;
	}
}