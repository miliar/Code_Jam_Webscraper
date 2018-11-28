/*
Problem #524 Prime Ring Problem - UVA
http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=465
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>
#include <string>
using namespace std;

typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		int k, c, s;
		cin >> k >> c >> s;
		printf("Case #%d: ", z);
		cout << 1;
		for (int i = 1; i < k; i++)
			cout << ' ' << i + 1;
		cout << endl;

	}
	return 0;
}
