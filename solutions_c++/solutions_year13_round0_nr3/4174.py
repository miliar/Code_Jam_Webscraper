#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <set>
using namespace std;

typedef long long LL;

int n, m;
set<LL> se;

void init()
{
	char str[100];
	for (int i = 1; i <= 10000000; i++)
	{
		LL temp = i;
		sprintf(str, "%lld", temp);
		int len = strlen(str);
		bool flag = true;
		for (int j = 0, k = len - 1; j <= k && flag; j++, k--)
			if (str[j] != str[k])
				flag = false;
		if (flag)
		{
			temp = (LL)i * i;
			sprintf(str, "%lld", temp);
			int len = strlen(str);
			flag = true;
			for (int j = 0, k = len - 1; j <= k && flag; j++, k--)
				if (str[j] != str[k])
					flag = false;
			if (flag)
			{
				se.insert(temp);
				cout << i << " " << temp << endl;
			}
		}
	}
}

void solved(int cas)
{
	printf ("Case #%d: ", cas);
	LL a, b;
	cin >> a >> b;
	set<LL>::iterator iter = se.lower_bound(a);
	LL ans = 0;
	for (; iter != se.end(); iter++)
	{
		if (*iter > b)
			break;
		ans++;
	}
	cout << ans << endl;
}

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	init();
	int T;
	scanf ("%d", &T);
	for (int i = 1; i <= T; i++)
		solved(i);
	return 0;
}