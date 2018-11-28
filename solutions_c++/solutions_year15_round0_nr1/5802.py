// 9.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>

using namespace std;


int main()
{
	FILE *f;
	freopen_s(&f,"in.txt","r",stdin);
	freopen_s(&f,"out.txt","w",stdout);
	int T;
	cin>>T;
	int smax,ans=0,pl=0,buff;
	string s;
	for (int i=0; i<T; i++)
	{
		ans=0;
		pl=0;
		buff=0;
		cin>>smax;
		cin>>s;
		for (int j=0; j<=smax; j++)
		{
			if (pl<j)
			{
				buff=j-pl;
				ans+=buff;
				pl+=buff;
			}
			pl+=(int)s[j]-'0';			
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}

