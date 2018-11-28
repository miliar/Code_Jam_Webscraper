// ProblemB.cpp : Defines the entry point for the console application.
//

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

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define clr(x) memset((x), 0, sizeof(x))


struct stGo
{
	std::set<int> cards;
	//int cards[4];
	int chosenCard;
};

void parseGo(stGo& onego){
	scanf("%d", &onego.chosenCard);

	int minRange = (onego.chosenCard - 1) * 4,
	    maxRange = minRange + 4;
	REP(i, 16)
	{
		int tmp;
		scanf("%d", &tmp);

		if (i>= minRange && i< maxRange)
		{
			onego.cards.insert(tmp);
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	//freopen("SampleData.in", "r", stdin);
	//freopen("train.in", "r", stdin);
	freopen("demo.in", "r", stdin);
	//freopen("C-small-practice-2.out", "w", stdout);
	//freopen("train.out", "w", stdout);




	int tt;
	scanf("%d", &tt);
	REP(it, tt)
	{
		printf("Case #%d: ", it + 1);
		stGo goes[2];

		//get the number of goes
		REP(i, 2){			
			parseGo(goes[i]);
		}

		std::vector<int> v_intersection;
 
		std::set_intersection(goes[0].cards.begin(), goes[0].cards.end(),
							  goes[1].cards.begin(), goes[1].cards.end(),
							  std::back_inserter(v_intersection));

		switch (v_intersection.size())
		{
			case 0: printf("Volunteer cheated!\n"); break;
			case 1: printf("%d\n", v_intersection[0]); break;
			default: printf("Bad magician!\n"); break;
		}

		int icarajo = 234;
	}

	return 0;
}

