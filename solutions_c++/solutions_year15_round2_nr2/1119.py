#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int cntrwa[1 << 18];

int rock, C, N;

int calculatore(int i)
{
	int answerwa = 0;
	for (int r = 0; r < rock; r++)
	{
		for (int c = 0; c < C; c++)
		{
			if (c > 0 and (i & (1 << (r * C + c))) and (i & (1 << (r * C + c - 1))))
				answerwa++;
			if (r > 0 and (i & (1 << (r * C + c))) and (i & (1 << (r * C + c - C))))
				answerwa++;
		}
	}
	return answerwa;
}

int main()
{
    freopen("abc.txt","r",stdin);
   	freopen("pqr.txt","w",stdout);
	int tester;
	cin >> tester;


	for (int t = 1; t <= tester; t++)
	{
		cin >> rock >> C >> N;

		int better = rock * C * N * 100;
		for (int i = 1; i < (1 << (rock * C)); i++)
		{
			cntrwa[i] = cntrwa[i - (i & -i)] + 1;
			if (cntrwa[i] == N) better = min(better, calculatore(i));
		}
		printf("Case #%d: %d\n", t, better);
	}
}
