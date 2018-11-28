#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

bool check[11];
bool check2[3000001];
queue<int> q;

int main() {
	FILE *fin = fopen("A-small-attempt1.in", "r");
	FILE *fout = fopen("output.txt", "w");

	int t_case;
	int num;
	int k = 1;
	int ret;
	fscanf(fin, "%d", &t_case);
	while (t_case--)
	{
		memset(check, false, sizeof(check));
		memset(check2, false, sizeof(check2));
		bool c = true;
		fscanf(fin,"%d", &num);
		q.push(num);
		while (!q.empty())
		{
			int x = q.front();
			ret = x;
			while (x / 10 > 0)
			{
				check[x % 10] = true;
				x = x / 10;
			}
			check[x] = true;
			bool test = true;
			for (int i = 0; i <= 9; i++)
			{
				if (check[i] == false)
					test = false;
			}
			if (test){
				
				fprintf(fout,"Case #%d: ", k++);
				fprintf(fout, "%d\n", ret);
				c = false;
				break;
			}
			q.pop();
			if (ret +num != x && check2[ret+num]==false){
				q.push(ret +num);
				check2[ret +num] = true;
			}
		}
		if (c){
			fprintf(fout,"Case #%d: ", k++);
			fprintf(fout,"INSOMNIA\n");
		}
		while (!q.empty()) q.pop();
	}

	return 0;	// 정상종료 시 반드시 0을 리턴해야 합니다.
}