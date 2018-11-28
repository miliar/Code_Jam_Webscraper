#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

void main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int nCase;
	cin>>nCase;

	int nBlock;
	vector<double> naomiBlock, kenBlock;

	for(int caseIndex = 0 ; caseIndex < nCase ; caseIndex++)
	{
		cin>>nBlock;
		naomiBlock.resize(nBlock);
		kenBlock.resize(nBlock);

		for(int i = 0 ; i < nBlock ; i++)
			cin>>naomiBlock[i];
		for(int i = 0 ; i < nBlock ; i++)
			cin>>kenBlock[i];

		sort(naomiBlock.begin(), naomiBlock.end(), less<double>());
		sort(kenBlock.begin(), kenBlock.end(), less<double>());

		int nNaomiWin = 0;
		int kenIndex = 0;
		
		for(int naomiIndex = 0 ; naomiIndex < nBlock ; naomiIndex++)
		{
			if(naomiBlock[naomiIndex] > kenBlock[kenIndex])
			{
				nNaomiWin++;
				kenIndex++;
			}
		}

		int nKenWin2 = 0;
		int nNaomiWin2 = 0;
		int naomiIndex = 0;

		for(int kenIndex = 0 ; kenIndex	 < nBlock ; kenIndex++)
		{
			if(naomiBlock[naomiIndex] < kenBlock[kenIndex])
			{
				nKenWin2++;
				naomiIndex++;
			}
		}
		nNaomiWin2 = nBlock - nKenWin2;
		cout <<"Case #"<<caseIndex+1<<": "<<nNaomiWin<<" "<<nNaomiWin2<<endl;
	}
}