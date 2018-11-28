// GCJ.cpp : Defines the entry point for the console application.
//
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void readCase_D(vector<float> &naomi, vector<float> &ken, int &blockCount)
{
	string line;
	scanf("%d", &blockCount);
	getline(cin, line);
	const char *begin = line.c_str();
	for(int i = 0; i < blockCount; ++i)
	{
		float weight = 0;
		scanf("%f", &weight);
		naomi.push_back(weight);
	}
	getline(cin, line);
	for(int i = 0; i < blockCount; ++i)
	{
		float weight = 0;
		scanf("%f", &weight);
		ken.push_back(weight);
	}
}

void solve_D()
{
	int caseNum;
	scanf("%d", &caseNum);
	string line;
	getline(cin, line);
	for(int i = 0; i < caseNum; ++i)
	{
		printf("Case #%d: ", i + 1);
		vector<float> naomi, ken;
		int blockCount;
		readCase_D(naomi, ken, blockCount);
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		unsigned int score1 = 0;
		int kenIter = 0;
		for(int j = 0; j < blockCount; ++j)
		{
			if(naomi[j] > ken[kenIter]) {
				++score1;
				++kenIter;
			}
		}
		printf("%d ", score1);

		unsigned int score2 = 0;
		kenIter = 0;
		for(int j = 0; j < blockCount; ++j)
		{
			float naomiWeight = naomi[j];
			while(kenIter < blockCount)
			{
				if(ken[kenIter] > naomiWeight)
					break;
				++kenIter;
			}
			score2 += kenIter >= blockCount;
			++kenIter;
		}
		printf("%d", score2);
		printf("\n");
	}
	
}



int main()
{
	freopen("D-large.in", "rt", stdin);
	freopen("D-large.out", "wt", stdout);

	solve_D();
	return 0;
}



