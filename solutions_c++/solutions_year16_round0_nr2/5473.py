#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	string s;
	cin>>t;
	int c=0;
	int i,ctr,len;
	while(t--)
	{
		ctr=0;
		cin>>s;
		s=s+'+';
//		char prev='+';
		len=s.length();
//		cout<<len<<endl;
		for(i=1;i<len;i++)
		{
			if(s[i]==s[i-1])
				continue;
			else
				ctr++;
		}
		printf("Case #%d: %d\n",++c,ctr);
	}
}
