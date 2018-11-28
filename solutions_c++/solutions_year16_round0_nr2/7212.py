//============================================================================
// Name        : gcjb.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<string.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int test=0;
	int l,i,ans;
	char c;
	while(test++<t)
	{
		char s[100];
		cin>>s;
		l=strlen(s);
		c=s[0];
		ans=0;
		for(i=1;i<l;i++)
		{
			if(s[i]!=c)
			{
				ans++;
				c=s[i];
			}
		}
		if(s[l-1]=='-')
			ans++;
		cout<<"Case #"<<test<<": "<<ans<<endl;

	}
	return 0;
}
