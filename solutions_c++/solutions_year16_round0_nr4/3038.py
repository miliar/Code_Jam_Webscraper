#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <cstdint>
using namespace std;

void solve(int test_case)
{
	int64_t k, c, s;
	cin >> k >> c >> s;
	cout << "Case #" << test_case << ": ";
	for (int i = 0; i < k; ++i)
	{
		cout << i + 1 << " ";
	}
	cout << endl;	
}

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		solve(i+1);
	}
}