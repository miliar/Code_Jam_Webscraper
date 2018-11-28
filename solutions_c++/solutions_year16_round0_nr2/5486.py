#include<bits/stdc++.h>
using namespace std;
int main()
{
	  int t;
	 // freopen("abc.in","r",stdin);
	  //freopen("out.txt","w",stdout);
	  cin>>t;
	  int tt=0;
	  while(t--)
	  {
	  	   tt++;
	  	   string s;
	  	   cin>>s;
	  	   int l=s.length();
	  	   int back=l-1;
	  	   while(s[back]=='+')
	  	   {
	  	     back--;	
		   }
		   if(back==-1)
		   {
		   	  cout<<"Case #"<<tt<<": "<<0<<endl;
		   	  continue;
		   }
		   int cnt=1;
		   for(int i=back;i>=1;i--)
		   {
		   	       if(s[i]!=s[i-1])
		   	       cnt++;
		   }
		   
		   cout<<"Case #"<<tt<<": "<<cnt<<endl;
		   
	  }
	  return 0;
}
