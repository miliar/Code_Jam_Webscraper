#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int n;
char a[200], b[200];

int work()
{
	char a[200];
	scanf("%s", a + 1);
	n = strlen(a + 1);
	int m = 0;
	for (int i = 1; i <= n; i ++)
		if (i == 1 || a[i] != b[m]) b[++ m] = a[i];
	if (b[m] == '+') m --;
	return m;
}

int main()
{
	freopen ("b.in", "r", stdin);
	freopen ("b.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i ++) cout << "Case #"<< i << ": " << work() << endl; 
	return 0;
}