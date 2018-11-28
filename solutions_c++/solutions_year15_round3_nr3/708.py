#include<iostream>
#include<stdio.h>
#include<queue>
#include<vector>
#pragma warning(disable:4996)

using namespace std;	


int main()
{
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int TT;
	int C, D, V;
	fscanf(in, "%d", &TT);
	for (int t = 1; t <= TT;t++)
	{
		int T[131] = { 0, };
		int coin[16];
		int Dy[131] = { 0, };
		fscanf(in,"%d %d %d", &C, &D, &V);
		for (int i = 0; i < D; i++)
		{
			fscanf(in, "%d", &coin[i]);
			T[coin[i]] = 1;
		}
		Dy[0] = 1;
		for (int j = 0; j < D; j++)
		{
			for (int i = V; i >= coin[j]; i--)
			{
				Dy[i] += Dy[i - coin[j]];
			}
		}
		int cnt = 0;		
		int flag = 0;
		for (int j = 1; j <= V; j++)
		{
			if (Dy[j] == 0){
				flag = 1;
				break;
			}
		}
		if (flag == 1)
		{
			for (int i = 1; i <= V; i++)
			{
				if (Dy[i] != 0)continue;
				cnt++;
				for (int j = V; j >= i; j--)
				{
					Dy[j] += Dy[j - i];
				}

				flag = 0;
				for (int j = 1; j <= V; j++)
				{
					if (Dy[j] == 0){
						flag = 1;
						break;
					}
				}
				if (flag == 0)
				{
					break;
				}
			}
		}
		fprintf(out, "Case #%d: %d\n", t, cnt);
	}
} 