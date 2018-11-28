#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>

using namespace std; 

const int INF = 1<<29;
typedef long long ll;

bool check(char s[])
{
	int l = strlen(s);
	for(int i = 0; i < l; i++)
		if(s[i] != '+')
			return false;

	return true;
}

int main()
{
	freopen("B-l.in", "r", stdin);
	freopen("B-l.out", "w", stdout);	

	int tt,j;
	scanf("%d", &tt);
	for(int qq = 1; qq <= tt; qq++){
		
		char s[101];
		scanf("%s", s);

		int l = strlen(s);
		if(check(s))printf("Case #%d: 0\n", qq);
		else
		{
			int count = 0;
				
			//Do the magic!
			for(int i = l-1; i >= 0; i--)
			{
				if(s[i] != '+')
				{
					for(int j = 0; j <= i; j++)
					{
						if(s[j] == '+')s[j]='-';
						else s[j]='+';
					}
					count++;
				}
				if(check(s))break;
			}

			printf("Case #%d: %d\n", qq, count);
		}
	}

	return 0;
}

		