#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <hash_map>
#include <sstream>
#include <time.h>
#include <cmath>
#include <set>
#include <queue>
#include <stack>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

long long cnt = 0;
int flag = 1;

void swap(vector<string>& vec, int i, int j)
{
	string tmp = vec[i];
	vec[i] = vec[j];
	vec[j] = tmp;
}

bool judge(vector<string>& vec)
{
	for (int i=1; i<vec.size(); ++i)
	{
		if (vec[i][0] == vec[i-1][0])
			return false;
	}
	return true;
}

void backtrack(int k, vector<string>& vec, map<char, vector<int>>& ditu)
{
	int len = vec.size();
	if (k >= len)
	{
		if (judge(vec))
		{
			cnt++;
			flag = 1;
			map<char, int> tmp;
			for (int i=0; i<len; ++i)
			{
				if (tmp.find(vec[i][0]) == tmp.end())
				{
					tmp[vec[i][0]]++;
					ditu[vec[i][0]][i]++;
				}
			}
		}
		else
			flag = 0;
		return;
	}

	int flag = 1;
	for (int i = k; i<len; ++i)
	{
		if (vec[i][0] == vec[k][0] && flag == 0)
			continue;

		if (vec[i][0] == vec[k][0] && ditu[vec[i][0]][k] > 0)
		{
			cnt += ditu[vec[i][0]][k];
			continue;
		}

		swap(vec, i, k);
		backtrack(k+1, vec, ditu);
		swap(vec, i, k);
	}
}

int main()
{
	freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int ca;
	scanf("%d", &ca);

	for (int caseN = 1; caseN<=ca; caseN++)
	{
		cnt = 0;
		flag  = 1;
		int NUM;
		scanf("%d", &NUM);
		vector<string> vec;
		map<char, vector<int>> ditu; 
		for (int i=0; i<NUM; ++i)
		{
			char ss[5];
			scanf("%s", ss);
			vec.push_back(ss);
			vector<int> tmp(NUM, 0);
			ditu[ss[0]] = tmp;
		}
		backtrack(0, vec, ditu);
		long long res = cnt % ((long long)(pow(2.0, 64.0)));
		printf("Case #%d: %lld\n", caseN, res);
	}
	//printf("Case #%d: %d\n", T, i + 1);
	return 0;
}

