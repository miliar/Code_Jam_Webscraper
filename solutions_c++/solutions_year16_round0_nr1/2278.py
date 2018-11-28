#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <map>
#include <limits>
#include <set>

using namespace std;

map <long long int, long long int> mp;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	for (int i = 1; i <= 1000000; i++)
	{
		long long int a, b;
		cin >> a >> b;
		mp[a] = b;
	}
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		long long int val;
		cin >> val;
		if (val == 0)
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << i + 1 << ": " << mp[val] << endl;
	}
}