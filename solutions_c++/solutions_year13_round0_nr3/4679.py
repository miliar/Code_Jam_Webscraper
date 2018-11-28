#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

long long numbers[10000005];
int Size = 0;

bool check(long long v)
{
	string r = "";
	while (v > 0)
	{
		r += '0' + v % 10;
		v /= 10;
	}
	string s = r;
	reverse(s.begin(), s.end());
	return s == r;
}

void preProcess()
{
	for (long long i = 1LL; i <= 10000000; i++)
		if (check(i) && check(i * i))
			numbers[Size++] = i * i;
}

int main()
{
	freopen("C-large-1.in", "r", stdin);
	freopen("issabelle.out", "w", stdout);
	preProcess();
	int totalCases;
	scanf("%d", &totalCases);
	for (int cases = 1; cases <= totalCases; cases++)
	{
		long long A, B;
		cin >> A >> B;
		int res = 0;
		int pos = 0;
		while (pos < Size)
		{
			while (pos < Size && numbers[pos] < A) pos++;
			while (pos < Size && numbers[pos] >= A && numbers[pos] <= B)
				pos++, res++;
			break;
		}
		printf("Case #%d: %d\n", cases, res);
	}
	return 0;
}