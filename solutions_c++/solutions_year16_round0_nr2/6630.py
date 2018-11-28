#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	//freopen("B-large.in","rt",stdin);    
  	//freopen("output.cpp","wt",stdout);  
	int t,j=1;
	cin>>t;
	while(j<=t)
	{
		cin.ignore();
		string s;
		cin>>s;
		int count=0;
		int i=0;
		if(s[0]=='-')
		{
			while(i<s.length() && s[i]!='+')
				i++;
			count++;
		}
		int count1=0,flag=0;;
		while(i<s.length())
		{
			if(s[i]=='-')
			{
				flag=1;
			}
			else
			{
				count1++;
				if(flag==1){
					count+=2;
					flag=0;
				}
			}
			i++;
		}
		if(s[i-1]=='-' && count1)
			count+=2;
		printf("Case #%d: %d\n",j,count);
		j++;
	}
}
