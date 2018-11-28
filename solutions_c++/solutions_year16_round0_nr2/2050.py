#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t,T,l,ct;
	bool flag;
	string s;
	cin>>t;
	T=t;
	while(t--)
	{
		cin>>s;
		l=s.length();
		if(s[0]=='-')
		flag=0;
		else
		flag=1;
		
		ct=1;
		for(int i=1;i<l;i++)
		{
			if(s[i]=='-')
			{
				if(flag==1)
				{
					flag=0;
					ct++;
				}
			}
			else
			{
				if(flag==0)
				{
					flag=1;
					ct++;
				}
			}
		}
		
		if(s[l-1]=='+')
		ct--;
		
		printf("Case #%d: %d\n",T-t,ct);
	}
	return 0;
}