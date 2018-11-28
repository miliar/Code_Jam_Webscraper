#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <map>
#include <limits>
#include <set>

using namespace std;

int arr[50];
int gen_arr[50];
int mem_gen[1000][50];
int cnt;
int generate(int pos, int N)
{
	if (pos == N)
	{
		if (cnt < 1000)
		{
			int c = 0;
			for (int i = 1; i <= N; i++)
			{
				mem_gen[cnt][i] = gen_arr[i - 1];
				if (gen_arr[i - 1] == 1)
					c++;
			}
			mem_gen[cnt][0] = c;
			cnt++;
		}
		return 0;
	}
	for (int i = 0; i < 2; i++)
	{
		gen_arr[pos] = i;
		generate(pos + 1, N);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N, J;
		cin >> N >> J;
		cout << "Case #1:" << endl;
		generate(0, (N - 2) / 2);
		int good_cnt = 0;
		for (int q = 0; q < cnt; q++)
			for (int j = 0; j < cnt; j++)
			{
				if (mem_gen[q][0] == mem_gen[j][0])
				{
					for (int i = 0; i < N; i++)
						arr[i] = 0;
					arr[0] = 1;
					arr[N - 1] = 1;
					for (int z = 1; z <= (N - 2) / 2; z++)
						arr[(z - 1) * 2 + 1] = mem_gen[q][z];

					for (int z = 1; z <= (N - 2) / 2; z++)
						arr[(z - 1) * 2 + 2] = mem_gen[j][z];

					for (int i = 0; i < N; i++)
						cout << arr[i];
					cout << ' ';
					for (int i = 2; i <= 10; i++)
						cout << i + 1 << ' ';
					cout << endl;
					good_cnt++;
					if (good_cnt == J)
						return 0;
				}
			}
	}

}