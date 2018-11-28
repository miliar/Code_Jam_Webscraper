#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;

typedef long long LL;
bool ok[10];
int last;

void get_num(LL key)
{
	while (key)
	{
		if (ok[key % 10]) last--;
		ok[key % 10] = 0;
		key /= 10;
	}
}

void calc(LL key)
{
	for (int i = 0; i <= 9; i++) ok[i] = 1;
	last = 10;
	for (int i = 1; i <= 10000; i++)
	{
		get_num(i * key);
		if (last == 0)
		{
			cout << i * key << endl;
			return;
		}
	}
	cout << "INSOMNIA" << endl;
}

int main()
{
	//freopen("1.in", "r", stdin);
	//freopen("1.out", "w", stdout);
	int num_case, now;
	scanf("%d", &num_case);
	for (int icase = 1; icase <= num_case; icase++)
	{
		scanf("%d", &now);
		printf("Case #%d: ", icase);
		calc((LL)now);
	}
	//for (int i = 900000; i <= 1000000; i++) calc(i);
	return 0;
}
