#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("shyamu.text","w",stdout);
	int t;
	cin>>t;
	int c1=0;
	while(t--)
	{
	  string s;
	  int k,c=0,f=0;
	  cin>>s;
	  cin>>k;
	  for(int i=0;i<=(s.size()-k);i++)
	  {
	  	if(s[i]=='-')
	  	{    c++;
	  		for(int j=i;j<(i+k);j++)
	  		{
	  			if(s[j]=='-')
	  			 s[j]='+';
	  			 else
	  			 s[j]='-';
			  }
		  }
	  }
	  for(int i=0;i<s.size();i++)
	  {
	  	if(s[i]=='-'){
	  	  f++;
	  	  break;}
	  }
	  if(f>0){
	  	c1++;
	  cout<<"Case #"<<c1<<": "<<"IMPOSSIBLE"<<endl;
}
  else
  {
  	c1++;
  	cout<<"Case #"<<c1<<": "<<c<<endl;
  }
	}
}
