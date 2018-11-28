#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <string>
long long L, X;
std::string inp;
bool frstFnd, ScndFnd;

char multiply(char * i_frst, char * i_scnd, char * o_thrd, bool & io_issigned)
{
	if (*i_frst == *i_scnd)
		return '-';
	if (*i_frst == '-')
		return '1';
	if (*i_frst == '1')
		return *i_scnd;
	if (*i_scnd - *i_frst == 1 || *i_scnd - *i_frst == -2)
		return *o_thrd;
	else
	{
		io_issigned = true;
		return *o_thrd;
	}
}
bool process(int curPos, int i_times, bool frstSign)
{
	char thrd;
	bool sign = false;
	char curChar = inp[curPos];
	while (true)
	{
	++curPos;
	if (curPos == L)
	{
		if (i_times == X)
			return false;
		curPos = 0;
		++i_times;
	}
	if (curChar == 'i')
		thrd = (inp[curPos] == 'j' ? 'k' : 'j');
	else if (curChar == 'j')
		thrd = (inp[curPos] == 'k' ? 'i' : 'k');
	else if (curChar == 'k')
		thrd = (inp[curPos] == 'j' ? 'i' : 'j');
	if (!frstSign)
	{
		if (!frstFnd && curChar == 'i')
		{
			frstFnd = true;
			return process(curPos, i_times, frstSign);
		}
		else if (frstFnd && !ScndFnd && curChar == 'j')
		{
			ScndFnd = true;
			return process(curPos, i_times, frstSign);
		}
		else if (curPos == 0 && i_times == X)
		{
			if (curChar == 'k' && frstFnd && ScndFnd)
				return true;
			else return false;
		}

	}
	sign = false;
	curChar = multiply(&curChar, &inp[curPos], &thrd, sign);
	if (curChar == '-')
	{
		curChar = '1';
		frstSign = !frstSign;
	}
	if (sign)
		frstSign = !frstSign;
	}
	//return process(curPos);
}
int main()
{
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
	int T;
	bool answer;
	scanf("%d\n", &T);
	for (int kace = 1; kace <= T; ++kace)
	{
		frstFnd = false;
		ScndFnd = false;
		scanf("%lld %lld\n", &L, &X);
		std::cin >> inp;
		//for (int i = 0; i < L; ++i)
		if (L < 2)
		{
			printf("%s%d: %s\n", "Case #", kace, "NO");
			continue;
		}
		/*for (int i = 1; i < X; i *= i)
			inp += inp;*/
		answer = process(0, 0, false);
		printf("%s%d: %s\n", "Case #", kace, (answer ? "YES" : "NO"));
	}
}
