#include <bits/stdc++.h>
#define ll long long int

using namespace std;

string fun(char a, string ans)
{
	if(a=='i')
		{
			if(ans=="1")
				ans="i";
			else if(ans=="-1")
				ans="-i";
			else if(ans=="i")
				ans="-1";
			else if(ans=="-i")
				ans="1";
			else if(ans=="j")
				ans="-k";
			else if(ans=="-j")
				ans="k";
			else if(ans=="k")
				ans="j";
			else if(ans=="-k")
				ans="-j";
		}
		else if(a=='j')
		{
			if(ans=="1")
				ans="j";
			else if(ans=="-1")
				ans="-j";
			else if(ans=="i")
				ans="k";
			else if(ans=="-i")
				ans="-k";
			else if(ans=="j")
				ans="-1";
			else if(ans=="-j")
				ans="1";
			else if(ans=="k")
				ans="-i";
			else if(ans=="-k")
				ans="i";
		}
		else if(a=='k')
		{
			if(ans=="1")
				ans="k";
			else if(ans=="-1")
				ans="-k";
			else if(ans=="i")
				ans="-j";
			else if(ans=="-i")
				ans="j";
			else if(ans=="j")
				ans="i";
			else if(ans=="-j")
				ans="-i";
			else if(ans=="k")
				ans="-1";
			else if(ans=="-k")
				ans="1";
		}
		return ans;
}

string fun2(char a, string ans)
{
	if(a=='i')
		{
			if(ans=="1")
				ans="i";
			else if(ans=="-1")
				ans="-i";
			else if(ans=="i")
				ans="-1";
			else if(ans=="-i")
				ans="1";
			else if(ans=="j")
				ans="k";
			else if(ans=="-j")
				ans="-k";
			else if(ans=="k")
				ans="-j";
			else if(ans=="-k")
				ans="j";
		}
		else if(a=='j')
		{
			if(ans=="1")
				ans="j";
			else if(ans=="-1")
				ans="-j";
			else if(ans=="i")
				ans="-k";
			else if(ans=="-i")
				ans="k";
			else if(ans=="j")
				ans="-1";
			else if(ans=="-j")
				ans="1";
			else if(ans=="k")
				ans="i";
			else if(ans=="-k")
				ans="-i";
		}
		else if(a=='k')
		{
			if(ans=="1")
				ans="k";
			else if(ans=="-1")
				ans="-k";
			else if(ans=="i")
				ans="j";
			else if(ans=="-i")
				ans="-j";
			else if(ans=="j")
				ans="-i";
			else if(ans=="-j")
				ans="i";
			else if(ans=="k")
				ans="-1";
			else if(ans=="-k")
				ans="1";
		}
		return ans;
}

char s[10010],st[10010];

int main()
{
	int t,f1,f2,f3,l,x,pos1,pos2;
	string ans;
	cin>>t;
	for(int loop=1;loop<=t;loop++)
	{
		f1=f2=f3=0;
		ans="1";
		cin>>l>>x;
		scanf("%s",s);
		for(int i=0;i<x;i++)
			for(int j=0;j<l;j++)
				st[(i*l)+j]=s[j];
		for(int i=0;i<l*x;i++)
		{
			ans=fun(st[i],ans);
			if(ans=="i"&&!f1)
			{
				f1++;
				pos1=i;
			}
		}
		if(ans=="-1")
			f3++;
		ans="1";
		for(int i=l*x-1;i>=0;i--)
		{
			ans=fun2(st[i],ans);
			if(ans=="k")
			{
				f2++;
				pos2=i;
				break;
			}
		}
		if(f1&&f2&&f3&&pos2-pos1>1)
			printf("Case #%d: YES\n",loop);
		else
			printf("Case #%d: NO\n",loop);
	}
	return 0;
}