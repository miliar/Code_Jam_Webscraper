#include <bits/stdc++.h>
using namespace std;
char s[5000];
int h[5000],k;
ifstream input;
ofstream output;
    
void order(int x)
{
	int max=0,i;
	if(x==0)
	return;
	for(i=0;i<x;++i)
	{
		if(max<s[i]&&h[i]!=1)
		max=s[i];
	}
	for(i=0;i<x;++i)
	{
		if(s[i]==max)
		output<<s[i],h[i]=1;
	}
	for(i=0;i<x;++i)
	{
		if(s[i]==max)
		{
			order(i);
			break;
		}
	}
}
int main() 
{
	input.open("A-large.in");
    output.open("output.txt");
	int t,j=1;
	input>>t;
	while(t--)
	{
		output<<"Case #"<<j<<": ";
		j++;
		k=0;
		int max=0,i;
		input>>s;
		int n=strlen(s);
		for(i=0;i<=1000;++i)
		h[i]=0;//ans[i]='\0';
		//cout<<s<<" ";
		for(i=0;i<n;++i)
		{
			if(max<s[i])
			max=s[i];
		}
		for(i=0;i<n;++i)
		{
			if(s[i]==max)
			output<<s[i],h[i]=1;
		}
		for(i=0;i<n;++i)
		{
			if(s[i]==max)
			{
				order(i);
				break;
			}
		}
		for(i=0;i<n;++i)
		{
			if(h[i]!=1)
			output<<s[i];
		}
		output<<endl;
	}
	output.close();
	input.close();
	//sakshamsinghnsit
	return 0;
}
