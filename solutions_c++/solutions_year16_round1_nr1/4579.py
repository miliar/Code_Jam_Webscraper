#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<deque>
#include<vector>
#include<iostream>
#include<set>
#include<queue>
using namespace std;
char map[16];
int len;
deque<char>d;
priority_queue<string> Q;
vector<string> s;

void f(int pos)
{
	if (pos == len)
	{
		string t;
		for (int i = 0; i < d.size(); i++)
		{
			t += d[i];
		}
		if (s.empty()) s.push_back(t);
		else
		{
			if (t > s.front())
			{
				s.pop_back();
				s.push_back(t);
			}
		}
		return;
	}

	// 앞에 붙이기
	d.push_front(map[pos]);
	f(pos + 1);
	d.pop_front();
	if (pos > 0){
		d.push_back(map[pos]);
		f(pos + 1);
		d.pop_back();
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++)
	{
		memset(map, 0, sizeof(map));
		scanf(" %s", map);
		len = strlen(map);
		printf("Case #%d: ", T);
		f(0);
		cout << s[0] << endl;
		if(!s.empty())s.pop_back();
	}
}