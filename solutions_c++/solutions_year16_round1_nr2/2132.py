#include <iostream>
#include <cstdio>
#include <fstream>
#include <set>
#include <string>
#include <vector>
#include <set>

using namespace std;


void problemB()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		int N;
		in >> N;
		vector<vector<int>> lists(2 * N - 1, vector<int>(N));
		for (int i = 0; i < lists.size(); i++)
		{
			for (int k = 0; k < N; k++)
			{
				in >> lists[i][k];
			}
		}
		set<int> pool;
		for (int i = 0; i < lists.size(); i++) pool.insert(i);

		vector<vector<int>> pairs(N);
		for (int i = 0; i < N; i++)
		{
			int mdx = -1;
			for (auto iter = pool.begin(); iter != pool.end(); ++iter)
				if (mdx == -1 || lists[mdx][i] > lists[*iter][i]) mdx = *iter;

			pairs[i].push_back(mdx);
			pool.erase(mdx);
			vector<int> removes;
			for (auto iter = pool.begin(); iter != pool.end(); ++iter)
			{
				if (lists[mdx][i] == lists[*iter][i])
				{
					pairs[i].push_back(*iter);
					removes.push_back(*iter);
				}
			}
			for (int k = 0; k < removes.size(); k++)
				pool.erase(removes[k]);
		}

		int recon = 0;
		for (int i = 0; i < N; i++)
		{
			if (pairs[i].size() == 1)
			{
				recon = i;
				break;
			}
		}

		vector<int> ans(N);
		ans[recon] = lists[pairs[recon][0]][recon];
		for (int i = 0; i < N; i++)
		{
			if (i == recon) continue;

			int cand1 = lists[pairs[i][0]][recon];
			int cand2 = lists[pairs[i][1]][recon];
			int used = lists[pairs[recon][0]][i];

			ans[i] = cand1;
			if (used == cand1) ans[i] = cand2;
		}
		out << "Case #" << t << ":";
		for (int i = 0; i < ans.size(); i++) out << " " << ans[i];
		out << endl;
	}
}


int main(int argc, char** argv)
{
	problemB();
	return 0;
}