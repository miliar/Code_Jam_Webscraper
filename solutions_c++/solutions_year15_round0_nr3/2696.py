#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,l,x,i,neg,tc,ans;
	string str;
	char tmp;
	scanf("%d",&t);
	tc=1;
	while(tc<=t)
	{
		neg=ans=0;
		scanf("%d%d",&l,&x);
		cin>>str;
		string s;
		for(i=0;i<x;i++)
		{
			s.append(str);
		}
		for(i=0;i<s.length()-1;i++)
		{
			tmp=s[i];
			if(ans==0 && tmp=='i')
				ans=1;
			else if(ans==1 && tmp=='k')
				ans=2;
            if(s[i+1]==tmp && tmp!='1')
			{
				s[i+1]='1';
				neg=1-neg;
			}
			else if(tmp=='1')
				continue;
			else if(s[i+1]=='1')
				s[i+1]=s[i];
			else if(s[i+1]==tmp-2 || s[i+1]==tmp+1)
			{
				if(tmp=='j')
					s[i+1]='i';
				else
					s[i+1]=s[i+1]+1;
			}
			else if(s[i+1]==tmp-1 || s[i+1]==tmp+2)
			{
				if(tmp=='j')
					s[i+1]='k';
				else
					s[i+1]=s[i+1]-1;
				neg=1-neg;
			}
		}
		if(s[s.length()-1]=='1' && neg==1 && ans==2)
			printf("Case #%d: YES\n",tc);
		else
			printf("Case #%d: NO\n",tc);
		tc++;
	}
	return 0;
}