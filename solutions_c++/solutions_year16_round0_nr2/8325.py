#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int main()
{
    freopen("inputblarge.in","r",stdin);
    freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++)
	{
		string s;
		cin>>s;
		int n = s.length();
		int j, count = 1;
		char p = s[0];
		for(j=1; j<n; j++)
		{
			if(p != s[j])
				count++;
			p = s[j];
		}
		if(s[n-1] == '+')
			count--;
		printf("Case #%d: %d\n", i, count);
	}
	return 0;
}
