#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int a[110];

int main()
{
	freopen("b.txt", "r", stdin);
	freopen("ob.txt", "w", stdout);
	int i,j,k,ans,cases;

	scanf("%d",&cases);

	for(int t = 1;t <= cases; t++)
	{
		string s;
		cin >> s;

		ans = 0;
		for(i = 0;i<s.length();i++)
			if(s[i] == '+') a[i] = 0;
			else
				a[i] = 1;

		int flag = 0;
		for(i = s.length()-1;i>=0;i--)
		{
			if(a[i]^flag){
				ans+=1;
				flag = flag ^ 1;
			}

		}

		printf("Case #%d: %d\n", t,ans);

	}

	return 0;

}
