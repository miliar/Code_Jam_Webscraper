#include <iostream>
#include <iomanip>
#include <deque>
#include <algorithm>
using namespace std;

bool comp(double i, double j)
{
	return (i > j);
}

void deceit_solve(deque<double> nblocks, deque<double> kblocks, int numBlocks)
{
	int points = 0;

	for(int i=0; i < numBlocks; i++) {
		double ken = kblocks.front();
		kblocks.pop_front();

		double fnaomi = nblocks.front();
		double bnaomi = nblocks.back();
		double naomi;
		if(fnaomi > ken) {
			nblocks.pop_front();
			naomi = fnaomi;
		} else {
			nblocks.pop_back();
			naomi = bnaomi;
		}

		if(naomi > ken) {
			points++;
		}
	}

	cout << points << " ";
}

void normal_solve(deque<double> nblocks, deque<double> kblocks, int numBlocks)
{
	int points = 0;

	for(int i=0; i < numBlocks; i++) {
		double naomi = nblocks.front();
		nblocks.pop_front();

		double fken = kblocks.front();
		double bken = kblocks.back();
		double ken;
		if(fken > naomi) {
			kblocks.pop_front();
			ken = fken;
		} else {
			kblocks.pop_back();
			ken = bken;
		}

		if(naomi > ken) {
			points++;
		}
	}

	cout << points;
}

int main()
{
	double tmp;
	int numCases;
	cin >> numCases;

	for(int i=0; i < numCases; i++) {
		int numBlocks;
		cin >> numBlocks;

		deque<double> nblocks;
		deque<double> kblocks;
		for(int j=0; j < numBlocks; j++) {
			cin >> tmp;
			nblocks.push_back(tmp);
		}

		for(int j=0; j < numBlocks; j++) {
			cin >> tmp;
			kblocks.push_back(tmp);
		}
		sort(nblocks.begin(), nblocks.end(), comp);
		sort(kblocks.begin(), kblocks.end(), comp);

		cout << "Case #" << i+1 << ": ";
		deceit_solve(nblocks, kblocks, numBlocks);
		normal_solve(nblocks, kblocks, numBlocks);
		cout << endl;
	}

	return 0;
}
