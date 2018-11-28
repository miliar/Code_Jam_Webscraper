#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<stdlib.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, N, X, arr[10010];
	bool hash[10010];
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++)
	{
		scanf("%d%d", &N, &X);
		for(int i = 0; i < N; i++)
		{
			scanf("%d", &arr[i]);
			hash[i] = false;
		}
		sort(arr, arr + N);
		int ans = 0;
		for(int i = N - 1; i >= 0; i--)
		{
			if(hash[i] == true) continue;
			ans++;
			for(int j = i - 1; j >= 0; j--)
			{
				if(hash[j] == false && arr[i] + arr[j] <= X)
				{
					hash[j] = true;
					break;
				}
			}
			hash[i] = true;
		}
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}

