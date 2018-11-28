#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<stdlib.h>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, N, arr[1010];
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++)
	{
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
		{
			scanf("%d", &arr[i]);
		}
		int ans = 0;
		int left = 0;
		int right = N - 1;
		for(int i = 0; i < N; i++)
		{
			int Min = arr[left];
			int idx = left;
			for(int j = left + 1; j <= right; j++)
			{
				if(arr[j] < Min)
				{
					Min = arr[j];
					idx = j;
				}
			}
			if(idx - left <= right - idx)
			{
				for(int j = idx; j > left; j--)
				{
					arr[j] = arr[j - 1];
				}
				ans = ans + idx - left;
				left++;
			}
			else
			{
				for(int j = idx; j < right; j++)
				{
					arr[j] = arr[j + 1];
				}
				ans = ans + right - idx;
				right--;
			}
		}
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}

