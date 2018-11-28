#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>

using namespace std;


int func (string &a)
{
	int n = a.size();
	a += '+';
	int ans = 0;
	for (int i = 0; i < n; ++i)
	{
		if (a[i] != a[i + 1])
			++ans;
	}
	return ans;
}

void caseN(int number, string &s)
{
	printf("Case #%d: ", number);
	
	printf("%d", func(s));
	printf("\n");
}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		string s;
		cin >> s;
		caseN(i + 1, s);
	}

	return 0;
}