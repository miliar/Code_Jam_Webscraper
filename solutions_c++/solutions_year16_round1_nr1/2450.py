// Round1A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "iostream"
#include "vector"
#include "algorithm"
#include "stdio.h"
#include "string"
#include "string.h"
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		string str;
		cin>>str;
		string cur;
		for(int i=0;i<str.size();i++)
		{
			if(i==0 || str[i]<cur[0])
			{
				cur.push_back(str[i]);
			}
			else 
			{
				cur=str[i]+cur;
			}
		}
		cout<<"Case #"<<tc+1<<": "<<cur<<endl;
	}
	return 0;
}

