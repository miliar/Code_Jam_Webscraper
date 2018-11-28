#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <functional>
#include <array>
#include <random>
#include <iostream>
#include  "time.h"


using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define clr(x) memset((x), 0, sizeof(x))



struct stBlocks
{
	vector<double> vNaomi;
	vector<double> vKen;

	int iWarScoreNaomi, 
		iDeceitfulScoreNaomi;
};

void playWar (stBlocks& blocks)
{
	vector<double> vNaomi(blocks.vNaomi);
	std::sort (vNaomi.begin(), vNaomi.end(), std::greater<double>());
    
	vector<double> vKen(blocks.vKen);
	sort(vKen.begin(), vKen.end());
	int pointsNaomi = 0;

	int total = vNaomi.size();

	REP(i, total)
	{
		auto naomisBiggest = vNaomi[0];
		
		int indexKen = 0;
		REP (k, vKen.size())
		{
			if (vKen[k] > naomisBiggest)
			{
				indexKen = k;
				break;
			}
		}

		auto valueKen = vKen[indexKen];
		vKen.erase(vKen.begin() + indexKen);

		if (naomisBiggest > valueKen)
		{
			//if naomis biggest > kens biggest
			pointsNaomi++;
		}
		vNaomi.erase(vNaomi.begin());
	}

	blocks.iWarScoreNaomi = pointsNaomi;
}

void playDeceit (stBlocks& blocks)
{
	vector<double> vNaomi(blocks.vNaomi);
	std::sort (vNaomi.begin(), vNaomi.end(), std::greater<double>());
    
	vector<double> vKen(blocks.vKen);
	sort(vKen.begin(), vKen.end());
	int pointsNaomi = 0;
	int pointsKen = 0;

	int total = vNaomi.size();

	REP(i, total)
	{
		auto naomisBiggest = vNaomi[0];
		auto kensBiggest = vKen[vKen.size()-1];

		if (naomisBiggest > kensBiggest)
		{
			//if naomis biggest > kens biggest
			pointsNaomi++;

			vNaomi.erase(vNaomi.begin());
			
		}
		else
		{
			//get the smallest value from Naomi, and sacrifice it:
			//make Ken use its biggest for it
			auto naomisSmallest =  vNaomi[vNaomi.size()-1];

			pointsKen++;

			vNaomi.erase(vNaomi.begin() + vNaomi.size()-1);
		}
		vKen.erase(vKen.begin() + vKen.size()-1);
	}

	blocks.iDeceitfulScoreNaomi = pointsNaomi;
}

	
int _tmain(int argc, _TCHAR* argv[])
{
	srand(time(NULL));
	
	freopen("demo.in", "r", stdin);

	int tt;
	scanf("%d", &tt);
	REP(it, tt)
	{
		printf("Case #%d: ", it + 1);

		int N;
		scanf("%d\n", &N);

		stBlocks blocks;

		double f;

		REP(n, N)
		{
			scanf("%lf", &f);
			blocks.vNaomi.push_back(f);
		}
		vector<double> v2;
		REP(n, N)
		{
			scanf("%lf", &f);
			blocks.vKen.push_back(f);
		}

		
		//get the number of goes
		blocks.iDeceitfulScoreNaomi = blocks.iWarScoreNaomi = 0;
		playWar(blocks);
		playDeceit(blocks);
		printf("%d %d\n",  blocks.iDeceitfulScoreNaomi, blocks.iWarScoreNaomi);
	}

	return 0;
}


