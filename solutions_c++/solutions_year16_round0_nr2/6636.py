/**************************************************
 * author:huangjipeng
 * date:2016-3-12
 * filename:temp.cpp
 * ***********************************************/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
using namespace std;
char s[1005];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int t;
	cin>>t;
	for(int te=1;te<=t;te++)
	{
		cin>>s;
		cout<<"Case #"<<te<<": ";
		int len=strlen(s);
		int num=0;
		int i=0;
		if(s[0]=='-')
		{
			num++;
			while(i<len)
			{
				if(s[i]=='+')
					break;
				i++;
			}
		}
		for(;i<len;i++)
		{
			if(s[i]=='+')continue;
			num+=2;
			while(i<len)
			{
				if(s[i]=='+')
					break;
				i++;
			}
		}
		cout<<num<<endl;
	}
	return 0;
}
