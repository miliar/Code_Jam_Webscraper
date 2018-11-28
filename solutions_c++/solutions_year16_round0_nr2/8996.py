#include <bits/stdc++.h>

using namespace std;

void change(int &cstate, int &count, char s)
{
	if( (cstate==0 && s=='-') || (cstate==1 && s=='+') )
	{
		return;
	}
	if(cstate==1 && s=='-')
	{
		cstate=0;
		count++;
	}		
	else
	{
		cstate=1;
		count++;
	}
}

int main()
{
	int t;
	cin>>t;
	
	for(int j=1;j<=t;j++)
	{
		string s;
			cin>>s;
		int count=0;
		int cstate;
			if(s[0]=='+')
				cstate=1;
			else
				cstate=0;
		for(int i=1;i<s.size();i++)
		{
			change(cstate,count,s[i]);
		}

		if(cstate==0)
			count++;
		printf("Case #%d: %d\n",j, count);
		
	}
	return 0;
}