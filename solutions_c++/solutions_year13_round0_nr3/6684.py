#pragma comment(linker, "/STACK:128777216")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <string>
#include <memory.h>
using namespace std;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
cin.sync_with_stdio(false);
cout.sync_with_stdio(false);
}

int a[1001];

string inttostr(int a)
{
	stringstream s;
	string str;
	s << a;
	s >> str;
	return str;
}

bool pal(int x)
{
	string s = inttostr(x);
	int n = s.length();
	bool flag = 1;
	for (int i = 0; i < n / 2; i++)
		if (s[i] != s[n - 1 - i])
			flag = 0;
	return flag;
			
}

int main()
{
	prepare();
	for (int i = 1; i < 34; i++)
		if (pal(i) && pal(i * i))
			a[i * i]++;
	for (int i = 1; i < 1001; i++)
		a[i] = a[i] + a[i - 1];
	int test;
	cin >> test;
	for (int t = 0; t < test; t++)
	{
		int d, b;
		cin >> d >> b;
		cout << "Case #" << t + 1 << ": ";
		cout << a[b] - a[d - 1] << endl;
	}
	return 0;
}
