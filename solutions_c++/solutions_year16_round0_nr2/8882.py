#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

int checkalternative(string str)
{
	int len=str.length();
	int i,count=0;
	for(i=0;i<len;i++)
	{
		if(str[i]!=str[i+1] && i!=len-1)
		{
			count++;
		}
		if(i==len-1 && str[i]=='-')
			count++;
	}
	return count;
}

int main()
{
	int t,i;
	cin>>t;
	for(i=0;i<t;i++)
	{
		string str;
		cin>>str;
		int count=checkalternative(str);
		printf("Case #%d: %d\n",i+1,count);
	}
}