#include <iostream>
#include <cstring>
#include <cctype>
#include <limits>
#include <vector>
#include <unordered_map>
#include <memory>
#include <algorithm>
#define maxN 2000

using namespace std;

int N;
int A[maxN];

int main()
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> A[i];
		int ans = 0;
		for (int i = 0; i < N; i++)
		{
			int L = 0, R = 0;
			for (int j = 0; j < i; j++)
				if (A[j] > A[i])
					L++;
			for (int j = i + 1; j < N; j++)
				if (A[j] > A[i])
					R++;
			ans += min(L, R);
		}
		cout << "Case #" << z << ": " << ans << endl;
	}
	return 0;
}
