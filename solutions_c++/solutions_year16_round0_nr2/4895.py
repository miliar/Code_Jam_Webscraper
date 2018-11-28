#include<iostream>
#include<string.h>
using namespace std;
void flip(string &s,int i)
{
	int k,j=i;
	string temp;
	for(k=0;k<=j;k++)
	{
		if(s[i]=='-')
		temp[k]='+';
		else
		temp[k]='-';
		i--;
	}
	for(k=0;k<=j;k++)
	s[k]=temp[k];
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w+",stdout);
	int t,count=1,store,i;
	cin>>t;
	while(count<=t)
	{
		
		string s;
		cin>>s;
		i=0;
		store=0;
		while(s.find('-')!=-1&&i<s.length())
		{
			char p=s[i];
			while(p==s[i]&&i<s.length())
			i++;
			if(i==s.length())
			{
				store++;
				break;
			}
			else
			{
				flip(s,i-1);
				store++;
				i=0;
			}
		}
		cout<<"Case #"<<count<<": ";
		cout<<store<<endl;
		count++;
	}
}

