#include <iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<set>
#include<map>
#include<list>
using namespace std;

int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		string s,str,max,s1="";
		cin>>s;
		str=s[0];
		max=s[0];
		//if(max>str)cout<<max;
		for(int i=1;i<s.size();i++)
		{
			s1=s[i];
			//cout<<s1<<" ";
			if(max.compare(s1)<=0)
			{
				//cout<<max<<" "<<s[i]<<"\n";
				max=s[i];
				//cout<<"max"<<s[i]<<" ";
				str=s[i]+str;
				
			}
			else str+=s[i];
		}
		cout<<"Case #"<<k<<": "<<str<<"\n";
	}
	return 0;
}