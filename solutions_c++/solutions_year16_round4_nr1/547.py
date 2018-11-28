#include <iostream>
#include <cstdio>
using namespace std;

char name[4] = "PRS";
int tree[3][10000];
int cnt[3][13][3];
int ans_arr[10000];
void cal(int cur, int &left, int &right)
{
	if (cur == 0)
	{
		left = 0;
		right = 1;
	}
	else if (cur == 1)
	{
		left = 1;
		right = 2;
	}
	else
	{
		left = 2;
		right = 0;
	}
}
void sort(int *arr, int start, int cnt)
{
	if((cnt - start) != 2)
	{
		sort(arr, start, start + (cnt - start)/2);
		sort(arr, start + (cnt - start)/2, cnt);
	}
	bool flag = true;
	for (int i = start; i < start + (cnt - start)/2; ++i)
	{
		if(arr[i] > arr[i + (cnt - start)/2])
		{
			flag = false;
			break;
		}
	}
	if(!flag)
	{
		int i = start;
		while(i < start + (cnt - start)/2)
		{
			swap(arr[i], arr[i + (cnt - start)/2]);
			i++;
		}
	}
	return;
}
int main()
{
	for (int i = 0; i < 3; ++i)
	{
		tree[i][0] = i;
		for (int j = 1; j <= 12; ++j)
		{
			int start = (1 << (j - 1)) - 1;
			int end = start + (1 << (j - 1));
			for (int k = start; k < end; ++k)
			{
				cal(tree[i][k], tree[i][k * 2 + 1], tree[i][k * 2 + 2]);
				cnt[i][j][tree[i][k * 2 + 1]]++;
				cnt[i][j][tree[i][k * 2 + 2]]++;
			}
		}
	}
	int T; cin >> T;
	for (int TT = 1; TT <= T; ++TT)
	{
		printf("Case #%d: ", TT);
		int n; cin >> n;
		int cnt_in[3];
		scanf("%d %d %d", cnt_in + 1, cnt_in, cnt_in + 2);
		int ans = -1;
		for (int i = 0; i < 3; ++i)
		{
			int flag = true;
			for (int j = 0; j < 3; ++j)
			{
				if (cnt[i][n][j] != cnt_in[j])
				{
					flag = false;
					break;
				}
			}
			if (flag)
			{
				ans = i;
				break;
			}
		}
		if (ans == -1)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			int ans_cnt = (1 << n);
			int ptr = (1 << n) - 1;
			for (int i = 0; i < ans_cnt; ++i)
			{
				ans_arr[i] = tree[ans][i + ptr];
			}
			// for (int i = 0; i < ans_cnt; ++i)
			// {
			// 	printf("%d", ans_arr[i]);
			// }
			// printf("\n");
			sort(ans_arr, 0, ans_cnt);
			for (int i = 0; i < ans_cnt; ++i)
			{
				printf("%c", name[ans_arr[i]]);
			}
			printf("\n");
			// for (int i = 0; i < ans_cnt; ++i)
			// {
			// 	printf("%d", ans_arr[i]);
			// }
			// printf("\n");
		}
	}
	return 0;
}
