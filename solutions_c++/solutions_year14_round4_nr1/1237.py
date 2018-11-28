#include <iostream>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <string>
#include <list>
#include <vector>
#include <string.h>
#include <stack>
#include <algorithm>
#include <math.h>

using namespace std;

int A[100100];

int main()
{
	int T, n, X, i, j;
	cin >> T;
	for (int tt = 1; tt <= T; tt++)
	{
		cin >> n >> X;
		for (i = 0; i < n; i++)
			cin >> A[i];
		sort(A, A + n);
		int ret = 0;
		i = n - 1, j =0;
		while (i>j)
		{
			if (A[i] + A[j] > X)
				i--;
			else
			{
				i--;
				j++;
			}
			ret++;
		}
		if (i == j)
			ret++;
		cout << "Case #" << tt << ": " << ret << endl;
	}
}