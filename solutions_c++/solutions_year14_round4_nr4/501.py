#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<stdlib.h>
using namespace std;

int cmp( const void *a , const void *b ) 
{ 
return strcmp((char *)a, (char *)b); 
} 

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, M, N;
	char str[10][12], s[65538][12];
	int id[10], arr[65538];
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++)
	{
		scanf("%d%d", &M, &N);
		int totalnum = 0;
		for(int i = 0; i < M; i++)
		{
			scanf("%s", &str[i]);
		}
		//printf("%d %d %d\n", M, N, (int)pow(N, M));
		for(int tnum = 0; tnum < (int)pow(N, M); tnum++)
		{
            int num = tnum;
			bool hash[10] = {false};
			for(int i = 0; i < M; i++)
			{
				id[i] = num % N;
				hash[id[i]] = true;
				num /= N;
			}
			bool flag = true;
			for(int i = 0; i < N; i++)
			{
				if(hash[i] == false)
				{
					flag = false;
					break;
				}
			}
			if(flag == false) continue;
			int ct = 0;
			for(int i = 0; i < N; i++)
			{
				int len = 0;
				s[0][0] = '\0';
				len++;
				for(int j = 0; j < M; j++)
				{
					if(id[j] == i)
					{
						for(int k = 0; k < strlen(str[j]); k++)
						{
							for(int l = 0; l <= k; l++)
							{
								s[len][l] = str[j][l];
							}
							s[len][k + 1] = '\0';
							len++;
						}
					}
				}
				qsort(s, len, sizeof(s[0]), cmp);
				int pos = 0;
				while(pos < len)
				{
					ct++;
					int pre = pos;
					while(pos < len && strcmp(s[pos], s[pre]) == 0) pos++;
				}
			}
			arr[totalnum++] = ct;
		}
		sort(arr, arr + totalnum);
		int Max = arr[totalnum - 1];
		int sum = 0;
		int pos = totalnum - 1;
		while(pos >= 0 && arr[pos] == Max)
		{
			pos--;
			sum++;
		}
		printf("Case #%d: %d %d\n", cases, Max, sum);
	}
	return 0;
}

