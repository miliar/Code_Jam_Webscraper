#define _CRT_SECURE_NO_WARNINGS

#include		<cstdio>
#include		<cmath>
#include		<algorithm>
#include		<vector>
#include		<stack>
#include		<queue>
#include		<functional>
#include		<cstring>
#include		<string>
#include		<map>
#include		<set>
#include		<iostream>

#define ENP     printf("**Entry Point**\n")
#define A       first
#define B       second
#define MP      make_pair

using namespace std;

typedef long long		 ll;
typedef vector	<int>	 VI;

char buf[1010];
string s;
string answer;

void work()
{
	scanf("%s", buf);
	s = buf;
	deque<char> dq;
	char first = s[0];

	dq.push_back(first);
	
	for (int i = 1; i < s.size(); i++)
	{
		if (first <= s[i])
		{
			dq.push_front(s[i]);
			first = s[i];
		}
		else
		{
			dq.push_back(s[i]);
		}
	}

	answer.clear();
	for (auto it = dq.begin(); it != dq.end(); ++it)
	{
		answer.push_back(*it);
	}

	printf("%s\n", answer.c_str());
}

int main(int argc, char **argv)
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t;i++)
	{
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}

/* memo
*
*
*
*
*
*/