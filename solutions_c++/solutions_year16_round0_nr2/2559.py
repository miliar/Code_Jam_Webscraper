// QualRound.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "vector"
#include "string"
#include "algorithm"
#include "string.h"
#include "stdio.h"
#include "iostream"
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		string str;
		cin>>str;
		int cnt=0;
		char ch = str[0];
		for(int i=1;i<str.size();i++)
		{
			if(str[i]!=str[i-1])
			{
				cnt++;
			}
			ch=str[i];
		}
		if(ch=='-') cnt++;
		cout<<"Case #"<<tc+1<<": "<<cnt<<endl;
	}
	return 0;
}

