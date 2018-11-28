#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t,n,i,k,ans=0,j,c=0,y=1;
	char s[105];
	cin>>t;
	while(t--)
	{ans=0;
	c=0;
		cin>>s;
		n=strlen(s);
		for(i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
			  ans++;
			  k=i+1;
			  while(s[k]!='+' && k<n)
			  {
			    k++;
			  }
			  c=1;
			  break;
			}
			
			else
			{
				for(j=0;j<n-1;j++)
				if(s[j]=='+' && s[j+1]=='-')
			 	ans+=2;
			 	break;
			}
		}	  
		if(c==1)
		{
			 for(j=k;j<n-1;j++)
			 {
			 	if(s[j]=='+' && s[j+1]=='-')
			 	ans+=2;
			 }
		}	
	  cout<<"Case "<<"#"<<y<<": "<<ans<<endl;
	  y++;
			
		
	}
	return 0;
}
