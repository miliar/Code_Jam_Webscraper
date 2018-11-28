#include<bits/stdc++.h>
using namespace std;
int main() 
{
	int t,i,j,last,ans;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
	    ans=0;
	    char s[200];
	    cin>>s;
	    last=strlen(s)-1;
	    while(last>=0)
	    {
	        if(s[last]=='+')
	          {
	            last--;
	          }
	        else if(s[0]=='-')
	        {
	            ans++;
	            for(i=0,j=last;i<=j;i++,j--)
	            {
	                char temp;
	                temp=s[i];
	                s[i]=s[j];
	                s[j]=temp;
	            }
	            for(i=0;i<=last;i++)
	            {
	                if(s[i]=='+')
	                s[i]='-';
	                else s[i]='+';
	            }
	        }
	        else if(s[0]=='+')
	        {
	            ans++;
	            int rev;
	            for(i=last;i>=0;i--)
	            {
	                if(s[i]=='+')
	                {
	                    rev=i;
	                    break;
	                }
	            }
	            for(i=0,j=rev;i<=j;i++,j--)
	            {
	                char temp;
	                temp=s[i];
	                s[i]=s[j];
	                s[j]=temp;
	            }
	            for(i=0;i<=rev;i++)
	            {
	                if(s[i]=='+')
	                s[i]='-';
	                else s[i]='+';
	            }
	        }
	    }
	    cout<<"Case #"<<tc<<": "<<ans<<"\n";
	}
	return 0;
}
