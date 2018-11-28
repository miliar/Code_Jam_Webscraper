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

bool check(int a[])
{
	for(int i = 0; i < 10; i++)
	{
		if(a[i] == 0)return false;
		else if(a[i] > 0)continue;
	}
	return true;
}

int main()
{
	freopen("A-.in", "r", stdin);
	freopen("A-l.out", "w", stdout);	

	int tt,o,ret;
	scanf("%d", &tt);
	for(int qq = 1; qq <= tt; qq++)
	{
		int n;
		scanf("%d", &n);

		if(n == 0){
			printf("Case #%d: INSOMNIA\n", qq);
		}
		else{

			int a[10];
			for(int i = 0; i < 10; i++)a[i] = 0;

			int c = 0;

			while(1)
			{
				if(check(a)==true)break;
				else{
					c++;
					o = c*n;
					ret = o;
					while(o)
					{
						a[o%10]++;
						o /= 10;
					}
				}
			}
			printf("Case #%d: %d\n",qq, ret);
		}

	}

	return 0;
}

		