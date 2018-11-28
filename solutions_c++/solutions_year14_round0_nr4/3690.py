#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

int worst_index(std::vector<double> blocks)
{
	double worst = 2.0;
	int index = -1;
	for (int j = 0; j < blocks.size(); j++)
		{
			if (blocks[j] < worst)
			{
					worst = blocks[j];
					index = j;
			}
		}	
	return index;
}

double worst_value(std::vector<double> blocks)
{
	double worst = 2.0;
	int index = -1;
	for (int j = 0; j < blocks.size(); j++)
		{
			if (blocks[j] < worst)
			{
					worst = blocks[j];
					index = j;
			}
		}	
	return worst;
}

int best_index(std::vector<double> blocks)
{
	double best = -1;
	int index = -1;
	for (int j = 0; j < blocks.size(); j++)
		{
			if (blocks[j] > best)
			{
					best = blocks[j];
					index = j;
			}
		}	
	return index;
}

double best_value(std::vector<double> blocks)
{
	double best = -1;
	int index = -1;
	for (int j = 0; j < blocks.size(); j++)
		{
			if (blocks[j] > best)
			{
					best = blocks[j];
					index = j;
			}
		}	
	return best;
}


int index_Ken_strategy(std::vector<double> blocks, double Told_Naomi)
{
	// return the smallest of the biggest
	double weight = 2;
	int index = -1;
	for (int j = 0; j < blocks.size(); j++)
		{
			if (blocks[j] > Told_Naomi && blocks[j] < weight)
				{
					weight = blocks[j];
					index = j;
				}
		}
	if (index == -1) // no better than Naomi's, return smallest
		return worst_index(blocks);
	else return index;
}

double Told_Naomi_generation_cheating(std::vector<double> blocks_Ken, std::vector<double> blocks_Naomi, int num_tries)
{
	// if I have something that beats your worst, I tell you your best plus something
	// else I send the worst
	double your_worst = worst_value(blocks_Ken);
	double weight = 2;
	int index = -1;
	for (int j = 0; j < blocks_Naomi.size(); j++)
		{
			if (blocks_Naomi[j] > your_worst && blocks_Naomi[j] < weight)
				{
					weight = blocks_Naomi[j];
					index = j;
				}
		}
	if (index != -1) return best_value(blocks_Ken) + 0.000000001 * num_tries;
	else return worst_value(blocks_Naomi);
}

double Told_Naomi_generation(std::vector<double> blocks_Naomi)
{
	return best_value(blocks_Naomi);
}

int index_Naomi_strategy_cheating(std::vector<double> blocks_Ken, std::vector<double> blocks_Naomi)
{
	// if I have something that beats your worst, I send the worst of mine which beats
	// the worst of yours; else I send the worst
	double your_worst = worst_value(blocks_Ken);
	double weight = 2;
	int index = -1;
	for (int j = 0; j < blocks_Naomi.size(); j++)
		{
			if (blocks_Naomi[j] > your_worst && blocks_Naomi[j] < weight)
				{
					weight = blocks_Naomi[j];
					index = j;
				}
		}
	if (index != -1) return index;
	else return worst_index(blocks_Naomi);
}

int index_Naomi_strategy(std::vector<double> blocks_Naomi)
{
	// always the best
	return best_index(blocks_Naomi);
}


int main()
{
		
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T; // test cases
	scanf("%d",&T);
			
	for (int i = 0; i < T; i++)
	{
		double N;
	  cin >> N ;
		std::vector<double> blocks_Naomi_war;
	  std::vector<double> blocks_Ken_war;
		for (int j = 0; j < N; j++)
		{
			double aux;
			cin >> aux;
			blocks_Naomi_war.push_back(aux);
		}
		for (int j = 0; j < N; j++)
		{
			double aux;
			cin >> aux;
			blocks_Ken_war.push_back(aux);
		}
		std::vector<double> blocks_Naomi_dec(blocks_Naomi_war);
		std::vector<double> blocks_Ken_dec(blocks_Ken_war);
		int points_Naomi_war = 0;
		int points_Naomi_dec = 0;
		while (blocks_Naomi_war.size() > 0)
		{
			int chosen_Naomi = index_Naomi_strategy(blocks_Naomi_war);
			double told_Naomi = Told_Naomi_generation(blocks_Naomi_war);
			int chosen_Ken = index_Ken_strategy(blocks_Ken_war, told_Naomi);
			if (blocks_Naomi_war[chosen_Naomi] > blocks_Ken_war[chosen_Ken])
				points_Naomi_war++;
			blocks_Naomi_war.erase (blocks_Naomi_war.begin() + chosen_Naomi);
			blocks_Ken_war.erase (blocks_Ken_war.begin() + chosen_Ken);
		}
		int num_tries = 0;
		while (blocks_Naomi_dec.size() > 0)
		{
			num_tries++;
			int chosen_Naomi = index_Naomi_strategy_cheating(blocks_Ken_dec, blocks_Naomi_dec);
			double told_Naomi = Told_Naomi_generation_cheating(blocks_Ken_dec, blocks_Naomi_dec, num_tries);
			int chosen_Ken = index_Ken_strategy(blocks_Ken_dec, told_Naomi);
			if (blocks_Naomi_dec[chosen_Naomi] > blocks_Ken_dec[chosen_Ken])
				points_Naomi_dec++;
			blocks_Naomi_dec.erase (blocks_Naomi_dec.begin() + chosen_Naomi);
			blocks_Ken_dec.erase (blocks_Ken_dec.begin() + chosen_Ken);
		}
		cout << "Case #" << i + 1 << ": " << points_Naomi_dec << " " << points_Naomi_war << endl;	
	}
	

	return 0;
};

