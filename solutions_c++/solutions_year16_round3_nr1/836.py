#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int N;

struct _magic_
{
	char let;
	int num;
};

bool cmp(_magic_ m1, _magic_ m2)
{
	if (m1.num != m2.num)
		return m1.num > m2.num;
	return m1.let < m2.let;
}

_magic_ m[55];

void solve()
{
	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		cin >> m[i].num;
		m[i].let = 'A' + i - 1;
	}
	for (int i = N + 1; i <= 26; i++)
	{
		m[i].num = 0;
		m[i].let = 'A' + i - 1;
	}
	while (true)
	{
		sort(m + 1, m + N + 1, cmp);
		if (m[1].num == 0)
		{
			break;
		}
		if (m[1].num == m[2].num && m[1].num == m[3].num)
		{
			cout << ' ' << m[1].let;
			m[1].num--;
		}
		else
		{
			if (m[1].num == m[2].num)
			{
				cout << ' ' << m[1].let << m[2].let;
				m[1].num--;
				m[2].num--;
			}
			else
			{
				cout << ' ' << m[1].let;
				m[1].num--;
			}
		}
	}
	return;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A2.txt", "w", stdout);
	int Test;
	cin >> Test;
	for (int i = 1; i <= Test; i++)
	{ 
		cout << "Case #" << i << ":";
		solve();
		cout << endl;
	}
	return 0;
}