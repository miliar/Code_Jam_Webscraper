#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int arr[200];
int S[500000][105];
int siz = 0;

inline void add(int n)
{
    for (int i = 0; i < n; i++)
		S[siz][i] = arr[i];
	siz++;
}

int sz;

void DFS(int ind, int cnt)
{
	if (2 * ind == sz - 1)
	{
		arr[ind] = 0;
		add(sz);
		arr[ind] = 1;
		add(sz);
		if (cnt < 5)
		{
			arr[ind] = 1;
			add(sz);
		}
		arr[ind] = 0;
		return;
	}
	else
		if (2 * ind == sz)
		{
			add(sz);
			return;
		}

	arr[ind] = arr[sz - ind - 1] = 0;
	DFS(ind + 1, cnt);

	if (cnt < 8)
	{
		arr[ind] = arr[sz - ind - 1] = 1;
		DFS(ind + 1, cnt + 2);
	}
	
	arr[ind] = arr[sz - ind - 1] = 0;
}

void multiply(int i)
{
	memset(arr, 0, sizeof(arr));
	for (int k = 0; k < 50; k++)
		for (int j = 0; j < 50; j++)
			arr[k + j] += S[i][k] * S[i][j];

	for (int i = 0; i < 103; i++)
		if (arr[i] > 10)
		{
			arr[i+1] += arr[i] / 10;
			arr[i] %= 10;
		}
}

bool naklebia(string s)
{
	int k = 103;
	while (arr[k] == 0)
		k--;
	k++;
	if (s.size() > k)
		return true;
	else
		if (k > s.size())
			return false;

	for (int i = 0; i < k; i++)
		if (s[i] - '0' > arr[i])
			return true;
		else
			if (s[i] - '0' < arr[i])
				return false;

	return false;
}

bool metia(string s)
{
	int k = 103;
	while (arr[k] == 0)
		k--;
	k++;
	if (s.size() < k)
		return true;
	else
		if (k < s.size())
			return false;

	for (int i = 0; i < k; i++)
		if (s[i] - '0' < arr[i])
			return true;
		else
			if (s[i] - '0' > arr[i])
				return false;
	return false;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	S[0][0] = 1;
	S[1][0] = 2;
	S[2][0] = 3;
	siz = 3;

	for (sz = 2; sz < 51; sz++)
	{
        memset(arr, 0, sizeof(arr));
		arr[0] = arr[sz-1] = 1;
		DFS(1, 2);

		memset(arr, 0, sizeof(arr));
		arr[0] = arr[sz-1] = 2;
		add(sz);
		if (sz%2)
		{
			arr[sz/2] = 1;
			add(sz);
		}
	}

	int t, a, b, o, beg;
	string s1, s2;
	scanf("%d\n", &t);
	for (int test = 0; test < t; test++)
	{
		cin>>s1>>s2;
		a = 0; 
		b = siz;

		while (a < b)
		{
			o = (a + b) / 2;
			multiply(o);
			if (naklebia(s1))
				a = o + 1;
			else
				b = o;
		}
		beg = a;

		a = 0;
		b = siz;
		while (a < b)
		{
			o = (a + b + 1) / 2;
			multiply(o);
			if (metia(s2))
				b = o - 1;
			else
				a = o;
		}

		//cout<<a<<" "<<beg<<endl;
		printf("Case #%d: %d\n", test + 1, a - beg + 1);
	}
	
	
	return 0;
}
