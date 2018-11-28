#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>

using namespace std;
char mul(char y,char x)
{
	if(x=='i')
	{
		if(y=='i')
			return 'q';
		if(y=='j')
			return 'c';
		if(y=='k')
			return 'j';
		if(y=='p')
			return 'i';
		if(y=='a')
			return 'p';
		if(y=='b')
			return 'k';
		if(y=='c')
			return 'b';
		if(y=='q')
			return 'a';
	}
	if(x=='j')
	{
		if(y=='i')
			return 'k';
		if(y=='j')
			return 'q';
		if(y=='k')
			return 'a';
		if(y=='a')
			return 'c';
		if(y=='b')
			return 'p';
		if(y=='c')
			return 'i';
		if(y=='p')
			return 'j';
		if(y=='q')
			return 'b';
	}
	if(x=='k')
	{
		if(y=='i')
			return 'b';
		if(y=='j')
			return 'i';
		if(y=='k')
			return 'q';
		if(y=='a')
			return 'j';
		if(y=='b')
			return 'a';
		if(y=='c')
			return 'p';
		if(y=='p')
			return 'k';
		if(y=='q')
			return 'c';
	}
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T,t=1;
	cin>>T;
	while(T--)
	{
		int l,x,x1=0,x2=0;
		cin>>l>>x;
		string s;
        cin>>s;
		char ans='p';
		if(x>12)
			x=x%4+12;
        for(int i=0;i<x;i++)
		{
             for(int j=0;j<l;j++)
			 {
				 ans=mul(ans,s[j]);
				 if(ans=='i')
					 x1=1;
				 else if(ans=='k'&&x1==1)
					 x2=1;
			 }
		}
		if(ans=='q'&&x1==1&&x2==1)
			printf("Case #%d: YES\n",t++);
		else
			printf("Case #%d: NO\n",t++);
	}
	return 0;
}
