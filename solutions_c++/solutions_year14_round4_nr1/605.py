#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <cctype>
#include <limits>
#include <vector>
#include <unordered_map>
#include <memory>
#include <algorithm>
#define maxN 100000

using namespace std;

int N, X;
int S[maxN];
bool used[maxN];

int main()
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		cin >> N >> X;
		for (int i = 0; i < N; i++)
			cin >> S[i];
		memset(used, 0, sizeof(used));
		sort(S, S + N);
		int count = 0;
		int j = N - 1;
		for (int i = 0; i < N; i++)
			if (!used[i])
			{
				used[i] = true;
				count++;
				for (;;)
				{
					if (j <= i || j < 0)
						break;
					if (S[i] + S[j] > X || used[j])
						j--;
					else
					{
						used[j] = true;
						j--;
						break;
					}
				}
			}
		cout << "Case #" << z << ": " << count << endl;
	}
	return 0;
}
