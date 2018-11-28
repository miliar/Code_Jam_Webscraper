#include <cstring>
#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

string x;

int main()
{
	int tc, cs = 1;
	cin >> tc;
	while(tc--)
	{
		cin >> x;
		//printf("hello 1\n");
		int sz = (int)x.size();
		
		int idx = sz - 1;
		
		while(idx >= 0){
			if(x[idx] == '+')idx--;
			else break;
		}
		
		//printf("1\n");
		if(idx < 0){
			printf("Case #%d: 0\n", cs++);
			continue;
		}
		if(idx == 0)
		{
			printf("Case #%d: 1\n", cs++);
			continue;
		}
		//printf("2\n");
		char prev = x[idx--];
		char pres;
		int changes = 0;
		//printf("3\n");
		while(idx >= 0)
		{
			pres = x[idx];
			if(pres != prev)changes++;
			prev = pres;
			idx--;
		}
		//printf("4\n");
		printf("Case #%d: %d\n", cs++, changes + 1);
	}
	return 0;
}

