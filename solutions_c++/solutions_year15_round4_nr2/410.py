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

struct str{
	int index;
	int val;
};

int bagua(map<int, vector<str>>& Fri, vector<int>& sex)
{
	int degree = 0;

	for (map<int, vector<str>>::iterator it = Fri.begin(); it!=Fri.end(); ++it)
	{
		int n1, n2;
		n1 = it->first;
		for (int i=0; i<it->second.size(); ++i)
		{
			n2 = it->second[i].index;
			if (sex[n1] != sex[n2])
				degree += it->second[i].val;
		}
	}
	return degree;
}

int main()
{
	freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int ca;
	scanf("%d", &ca);

	for (int caseN = 1; caseN<=ca; ++caseN)
	{
		printf("Case #%d:\n", caseN);
		int N,M,Q;
		scanf("%d %d %d", &N, &M, &Q);

		//vector<vector<int>> friends(N, vector<int>(N, 0));
		map<int, vector<str>> FRI;
		vector<int> sex(N, 0);

		for (int i=0; i<N; ++i)
		{
			int v;
			scanf("%d", &v);
			sex[i] = v;
		}
		//sex;
		for (int i=0; i<M; ++i)
		{
			int n1, n2, val;
			scanf("%d %d %d", &n1, &n2, &val);
			if (n1 > n2)
			{
				int ttt = n1;
				n1 = n2;
				n2 = ttt;
			}
			str ttttt;
			ttttt.index = n2-1;
			ttttt.val = val;
			FRI[n1-1].push_back(ttttt);
			//friends[n1-1][n2-1] = val;
			//friends[n2-1][n1-1] = val;
		}
		//friends;
		//sex;
		while (Q--)
		{
			//friends;
			int op;
			scanf("%d", &op);
			if (op == 3)
			{
				int degree = bagua(FRI, sex);
				printf("%d\n", degree);
				continue;
			}
			if (op == 1)
			{
				int user;
				scanf("%d", &user);
				sex[user-1] = sex[user-1] == 0? 1:0;
				continue;
			}

			if (op == 2)
			{
				int n1, n2, val;
				scanf("%d %d %d", &n1, &n2, &val);
				if (n1 > n2)
				{
					int ttt = n1;
					n1 = n2;
					n2 = ttt;
				}
				if (FRI.find(n1-1) == FRI.end())
				{
					str ttttt;
					ttttt.index = n2-1;
					ttttt.val = val;
					FRI[n1-1].push_back(ttttt);
				}
				else
				{
					int flagg = 0;
					for (int jj=0; jj<FRI[n1-1].size(); ++jj)
					{
						if (FRI[n1-1][jj].index == n2-1)
						{
							flagg = 1;
							FRI[n1-1][jj].val = val;
							break;
						}
					}
					if (flagg == 0)
					{
						str ttttt;
						ttttt.index = n2-1;
						ttttt.val = val;
						FRI[n1-1].push_back(ttttt);
					}

				}

				//friends[n1-1][n2-1] = val;
				//friends[n2-1][n1-1] = val;
				continue;
			}
		}
	}
	//printf("Case #%d: %d\n", T, i + 1);
	return 0;
}

