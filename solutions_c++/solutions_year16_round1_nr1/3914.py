/* ***************************************************************
 * Program Name : Code Jam
 * Date:  4, 2016
 * Author: Mahmoud Ismail
 *Copyright: Your copyright notice
 ***************************************** *******************/
#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
#include<stdio.h>
#include<sstream>
#include <stdlib.h>
#include<iostream>
#include<string>
#include<algorithm>
#include <limits>
#include<queue>
#include<vector>
#include<set>
#include <cstdio>
#include <cstring>
#include<map>
#include<cmath>
#include<climits>
#include<iomanip>
#include<utility>
using namespace std;
int main() {

	int t,c=1;
	scanf("%d",&t);
	while(t--)
	{
		string s;
		cin>>s;

		int sz=s.size();
		string ans="";
		for(int i=0;i<sz;i++)
		{
			if(i==0)
			{
				ans+=s[i];
				continue;
			}
			if(i==1)
			{
				if(s[i]<s[i-1])
				{

					ans+=s[i];

				}
				else
				{

					ans=s[i];
					ans+=s[i-1];
				}

				continue;
			}

			if(s[i]>=ans[0])
			{

				string te=ans;

				ans=s[i];
				ans+=te;


			}
			else
			{

				ans+=s[i];

			}




		}




	cout<<"Case #"<<c++<<": "<<ans<<endl;




	}



	return 0;
}
