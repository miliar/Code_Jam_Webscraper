#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <string>

using namespace std;

void solve();
int main()
{
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
}
int findmax(vector<int> &v);
bool allzeros(vector<int>&v)
{
	for (int i = 0; i < v.size(); i++)
	{
		if (v[i] != 0)
			return false;
	}
	return true;
}
void eat(vector<int> &in, vector<int> &out)
{
	out.resize(in.size());
	for (int i = 0; i < in.size(); i++)
	{
		if (in[i])
			out[i] = in[i] - 1;
		else
			out[i] = 0;
	}
}
void breakup(vector<int>&in, vector<int>&out)
{
	//out.resize(in.size() + 1);
	int max = findmax(in);
	bool broken = false;
	for (int i = 0; i < in.size(); i++)
	{
		if (max == in[i] && !broken)
		{
			broken = true;
			out.push_back(max / 2);
			out.push_back(max - (max / 2));
		}
		else
		{
			out.push_back(in[i]);
		}
	}
}
void solve()
{
	int d;
	vector<int> p;
	int pi;
	scanf("%d", &d);
	int max = 0;
	for (int i = 0; i < d; i++)
	{
		scanf("%d", &pi);
		p.push_back(pi);
		
	}
	
	int time = 0;
	vector<vector<int>> config;
	config.push_back(p);
	vector<vector<vector<int>>> allconfigs;
	vector<vector<pair<int, int>>> allrelation;
	allconfigs.push_back(config);
	vector<pair<int, int>> relation;
	relation.push_back(make_pair(-1, -1));
	allrelation.push_back(relation);
	while (1)
	{
		time++;
		int ind = time - 1;
		vector<vector<int>> newconfig;
		vector<pair<int, int>> rel;
		bool done = false;
		for (int i = 0; i < allconfigs[ind].size(); i++)
		{
			vector<int> eaten;
			
			eat(allconfigs[ind][i], eaten);
			
			if (allzeros(eaten))
			{
				/*int pind = ind, pi = i;
				while (pind != -1 && pi != -1)
				{
					for (int a = 0; a < allconfigs[pind][pi].size(); a++)
					{
						printf("%d ", allconfigs[pind][pi][a]);
					}
					printf("\n");
					int npind = allrelation[pind][pi].first;
					int npi = allrelation[pind][pi].second;
					pind = npind;
					pi = npi;
				}*/
				done = true;
				break;
			}

			
			newconfig.push_back(eaten);
			rel.push_back(make_pair(ind, i));
			
			
			//int b[1000] = { 0 };
			int max = findmax(allconfigs[ind][i]);
			for (int j = 0; j < allconfigs[ind][i].size(); j++)
			{	
				int v = allconfigs[ind][i][j];
				if (v == max)
				{	
					//b[v] = 1;
					for (int l = 1; l <= v / 2; l++)
					{
						vector<int> broken;
						broken.push_back(l);
						broken.push_back(v - l);
						for (int k = 0; k < allconfigs[ind][i].size(); k++)
						{
							if (k == j)
								continue;
							broken.push_back(allconfigs[ind][i][k]);
						}
						newconfig.push_back(broken);
						rel.push_back(make_pair(ind, i));
						//printf("Config size: %d\n", newconfig.size());
					}
					break;
					/*for (int k = 0; k < allconfigs[ind][i].size(); k++)
					{
						if (k == j)
						{
							int v = allconfigs[ind][i][k];
							for (int l = 1; l <= v / 2; l++)
							{	
								broken.push_back(l);
								broken.push_back(v - l);
							}
						}
						else
						{
							int v = allconfigs[ind][i][k];
							broken.push_back(v);
						}
					}*/
				}
			}
			/*
			vector<int> broken;
			breakup(allconfigs[ind][i], broken);
			newconfig.push_back(broken);*/
			/*if (allzeros(broken))
			{
				done = true;
				break;
			}*/
		}
		if (done)
			break;
		//allconfigs.erase(allconfigs.begin());
		allconfigs.push_back(newconfig);
		allrelation.push_back(rel);
	}
	printf("%d", time);
}

int findmax(vector<int> &v)
{
	int max = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (max < v[i])
		{
			max = v[i];
		}
	}
	
	return max;
}