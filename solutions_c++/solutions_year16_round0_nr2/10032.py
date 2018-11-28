#include <cstdio>
#include <stack>
#include <queue>
#include <string>

using namespace std;

int minFlip = 2000000000;

bool checkCakes(char cakes[101], int cakeCnt)
{
	for (int i = 0; i < cakeCnt; i++)
	{
		if (cakes[i] == '-')
			return false;
	}
	return true;
}

void solveCake(int n, char cakes[101], int cakeCnt, int t)
{
	stack<char> s1;
	stack<char> s2;
	queue<char> q1;
	queue<char> q2;
	char cakeNow[101];
	char cakeNow2[101];

	if (checkCakes(cakes, cakeCnt))
	{
		if (minFlip > n)
			minFlip = n;
		return;
	}

	if (n > cakeCnt)
		return;

	for (int i = cakeCnt - 1; i >= 0; i--)
	{
		s1.push(cakes[i]);
		s2.push(cakes[i]);
	}

	// 전체뒤집기
	for (int i = 0; i < cakeCnt; i++)
	{
		char ch = s1.top();
		if (ch == '+')
			ch = '-';
		else
			ch = '+';
		q1.push(ch);
		s1.pop();
	}

	for (int i = 0; i < cakeCnt; i++)
	{
		s1.push(q1.front());
		q1.pop();
	}

	for (int i = 0; i < cakeCnt; i++)
	{
		cakeNow[i] = s1.top();
		s1.pop();
	}
	solveCake(n + 1, cakeNow, cakeCnt, t);

	// 탑에서 같은것끼리만 뒤집기
	char prev = '1';
	for (int i = 0; i < cakeCnt; i++)
	{
		char ch = s2.top();
		if (prev == '1' || prev == ch)
		{
			s2.pop();
			if (prev == '1')
				prev = ch;
			if (ch == '+')
				ch = '-';
			else
				ch = '+';
			q2.push(ch);
		}
		else if (prev != '1' && prev != ch)
			break;
	}

	int size = q2.size();
	for (int i = 0; i < size; i++)
	{
		s2.push(q2.front());
		q2.pop();
	}

	for (int i = 0; i < cakeCnt; i++)
	{
		cakeNow2[i] = s2.top();
		s2.pop();
	}
	solveCake(n + 1, cakeNow2, cakeCnt, t);
}

int main() {
	int T;

	//freopen("input2.txt", "r", stdin);
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		char first[101];
		int cakeCnt = 0;
		scanf("%s", first);
		cakeCnt = strlen(first);
		solveCake(0, first, cakeCnt, t);
		printf("Case #%d: %d\n", t, minFlip);
		minFlip = 2000000000;
	}

	return 0;
}
