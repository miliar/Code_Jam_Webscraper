#include <bits/stdc++.h>
using namespace std;

int main() {int t,n,i,j;
	cin>>t;
	{
	    for(j=1;j<=t;j++)
	    {
	        cin>>n;
	        char s[n+1];
	        cin>>s;int std=0,nd=0;
	        for(i=0,s[i]!=48;i<strlen(s);i++)
	        {
	            if(std<i) {
	                nd+=i-std;std+=nd+(s[i]-48);
	            }
	            else std+=(s[i]-48);
	        }
	        printf("Case #%d: %d\n",j,nd);
	    }
	}
	
	return 0;
}