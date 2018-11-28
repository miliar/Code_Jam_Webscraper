#include<iostream>
#include<cstdio>
#include<cstdlib>
#include <string.h>
#include<string>
#include<vector>
#include<set>
#include<list>
#include<algorithm>
using namespace std;
typedef long long ll;

int A[1005];
int main()
{
	freopen("in_A_large.txt", "r", stdin);
	freopen("out_A_large.txt", "w", stdout);
	int T;
	cin >> T;
	for (int TC = 1; TC <= T; ++TC)
	{
		int N;
		cin >> N;
		int mx_diff = 0;
		for (int i = 0; i < N; ++i)
			scanf("%d", A + i);
		int first = 0;
		for (int i = 1; i < N; ++i)
		{
			if (A[i] < A[i - 1])
				first += (A[i - 1] - A[i]);
			if ((A[i - 1] - A[i])>mx_diff)
				mx_diff = (A[i - 1] - A[i]);
		}
		int sec = 0,cur=0;
		for (int i = 0; i < N-1; ++i)
		{
			if ((A[i]) <= mx_diff)
				sec += A[i];
			else
				sec += mx_diff;

		}
		printf("Case #%d: %d %d\n", TC,first, sec);

	}
	return 0;
}

