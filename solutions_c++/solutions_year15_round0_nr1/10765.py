#include<cstdio>
#include<iostream>
#include<string>
using namespace std;


int func_conv(char ch)
{
	return(ch-48);
}

int main()
{
	int t,n,count,j=1;
	string s;
	scanf("%d",&t);
	while(t--)
	{
		count=0;
		int extra=0;
		scanf("%d",&n);
		cin>>s;
		for(int i=0;i<s.length();i++)
		{
			if(count<(i)&&func_conv(s[i])>0)
			{
				extra+=i-count;
				count+=extra;
			}
			
			count+=func_conv(s[i]);
		}
		cout<<"Case #"<<j++<<": ";
		printf("%d\n",extra);
	}
}
