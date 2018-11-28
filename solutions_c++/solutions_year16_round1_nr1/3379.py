#include <stdio.h>
#include <iostream>
#include <algorithm>

#define ln(c) (int)c.length()

using namespace std;

int test, n;
string s, p;

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	
	scanf("%d" ,&test);
	
	for(int t=1; t<=test; t++)
	{
		cin >> s;
		
		n = ln(s);
		p.clear();
		
		for(int i=0; i<n; i++)
		{
			if(p+s[i] > s[i]+p)
				p=p+s[i];
			else
				p=s[i]+p;
		}
		
		printf("Case #%d: %s\n" ,t ,p.c_str());
	}
}
