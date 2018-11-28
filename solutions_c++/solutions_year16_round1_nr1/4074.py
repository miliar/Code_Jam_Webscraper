#include <iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
#include<set>
//#include<bits/stdc++.h>

#define pb push_back
#define ll long long int
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	ll t,n,i,ans,u,st,e;
	//string s,temp;
	char s[1003],temp[3005];
	scanf("%lld",&t);
	for(u=1;u<=t;u++)
	{
		st=2000;
		e=2000;
		for(i=0;i<=2005;i++)
			temp[i]='A';
		scanf("%s",s);
		temp[2000]=s[0];
		for(i=1;i<strlen(s);i++)
		{

			{
				if((ll)s[i]>=(ll)temp[st])
				{
					st--;
					temp[st]=s[i];

				}
				else
				{
					e++;
					temp[e]=s[i];
				}
			}

		}
		//s=temp.substr(st,2);
		printf("Case #%lld: ",u);
		for(i=st;i<=e;i++)
			printf("%c",temp[i]);
		printf("\n");
		//sort(s.begin(),s.end(),greater<char>());
		//printf("Case #%lld: %s\n",u,s.c_str());
	}
	return 0;
}
