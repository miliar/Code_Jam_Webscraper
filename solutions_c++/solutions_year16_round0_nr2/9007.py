#include <bits/stdc++.h>
using namespace std;
int main()
{ ios_base::sync_with_stdio(0);
	int t,i,k;
	cin>>t; char s[105];
	for(int j=1;j<=t;j++)
	{
		cin>>s; int l,p=0;
		l=strlen(s);
		for(i=0;s[i]!='\0';i++)
		{
		    if(s[i]=='+' && s[i+1]=='-')
			{
				for(k=i+1;s[k]!='\0';k++)
				{ 	i=k;
					if(s[k]=='-')
						continue;
					else if(s[k]=='+'){ i=k-1; 
					 break; }
				} 
				p=p+2; 
			} 	
			else if(s[i]=='-')
			{	
				for(k=i;s[k]!='\0';k++)
				{ 
					if(s[k]=='-')
					{	i=k;
						continue;}
					else if(s[k]=='+')
					{	i=k-1;
						break;}
				}   p++;
			}
		}
		printf("Case #%d: %d\n",j,p);
	}
}
