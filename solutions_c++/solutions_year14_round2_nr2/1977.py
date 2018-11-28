#include <iostream>
#include <vector>
#include <algorithm>

#pragma warning(disable: 4996)

using namespace std;

int Count(int a, int b, int k)
{
	int res = 0;
	for (int i = 0; i<a; i++)
		for (int j = 0; j<b; j++)
			if ((i & j) < k)
				res++;
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Tests, A, B, K;
	cin >> Tests;
	for (int i = 0; i<Tests; i++)
	{
		cin >> A >> B >> K;
		cout << "Case #" << i+1 << ": " << Count(A, B, K) << endl;
	}
	return 0;
}
