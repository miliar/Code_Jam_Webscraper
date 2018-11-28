#pragma warning(disable:4996)

#include <conio.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, const char *argv[])
{
	int test_case_totalnum, now_case_num = 0;
	FILE *hFile;

	vector<char> dic;
	vector<int> vec[100];
	vector<int> avrvec;

	int N, num_of_string;
	int i, j;
	int tmp;
	int count = 0;
	char tmpstr[999];

	bool isFeglaWon = false;

	hFile = fopen(argv[1], "r");
	fscanf(hFile, "%d", &test_case_totalnum);

	while (now_case_num++ < test_case_totalnum)
	{
		printf("Case #%d: ", now_case_num);
		fscanf(hFile, "%d", &N);
		
		num_of_string = N;

		for (i = 0; i < 100; i++)
		{
			vec[i].clear();
		}
		dic.clear();
		avrvec.clear();
		isFeglaWon = false;

		char c, pc = '\0';
		
		while ((c = fgetc(hFile)) == '\n');
		while (1)
		{
			if (c == '\n') break;
			if (pc != c)
			{
				dic.push_back(c);
				vec[N-1].push_back(0);
				avrvec.push_back(0);
			}
			vec[N-1].back()++;
			avrvec.back()++;
			pc = c;
			c = fgetc(hFile);
		}
		
		N--;

		pc = '\0';
		int cur_dic_index = 0;
		while (N > 0)
		{
			c = fgetc(hFile);
			if (c == '\n' || c == -1)
			{
				pc = '\0';
				cur_dic_index = 0;

				N--;
				if (vec[N].size() != dic.size())
					isFeglaWon = true;
				if (N == 0) break;
				continue;
			}
			if (pc != c)
			{
				if (dic.size() < cur_dic_index+1 || dic[cur_dic_index] != c)
				{
					isFeglaWon = true;
					break;
				}
				cur_dic_index++;
				vec[N - 1].push_back(0);
			}
			vec[N - 1].back()++;
			avrvec[cur_dic_index-1]++;
			pc = c;
		}

		if (isFeglaWon == true)
		{
			printf("Fegla Won\n");
			for (i = 0; i < N; i++)
			{
				fgets(tmpstr, 999, hFile);
			}
			continue;
		}

		count = 0;
		for (i = 0; i < vec[0].size(); i++)
		{
			avrvec[i] = (int)(avrvec[i] / (double)num_of_string + 0.5);
			for (j = 0; j < num_of_string; j++)
			{
				count += abs(avrvec[i] - vec[j][i]);
			}
		}


		printf("%d\n", count);

	}
	return 0;
}