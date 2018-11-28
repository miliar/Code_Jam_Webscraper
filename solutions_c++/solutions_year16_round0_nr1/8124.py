//g++ -std=c++0x your_file.cpp -o your_program
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

int used[20], cnt, it;

inline bool Complete(int x)
{
	while (x)
	{
		if (used[x % 10] != it)
		{
			used[x % 10] = it;
			cnt--;
			if (!cnt)
				return 1;
		}
		x /= 10;
	}
	return 0;
}

inline void solve()
{
	memset(used, 0, sizeof(used));
	cin >> it;
//	cout << it << " -- ";
	if (!it)	
	{
		cout << "INSOMNIA";
		return ;
	}
	cnt = 10;
	for (int i = 1;;i++)
	{
		if (Complete(i * it))
		{
			printf("%d", i * it);
			return ;
		}
	}
}

int main()
{
	freopen (fname"input.txt", "r", stdin);
	freopen (fname"output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		if (i > 1)
			puts("");
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
