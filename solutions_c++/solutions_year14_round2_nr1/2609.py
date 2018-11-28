//============================================================================
// Name        : Algo.cpp
// Author      : Hand
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

string calBase(int dist[], string input);

int main() {
	int testcases = 0;

	cin >> testcases;

	//cout << "case : " << testcases << "\n";

	string input[100];
	int distance[100][100];
	string base = "";
	int baselength = 0;
	int sum[100];

	int n = 0;
	bool possible = true;
	int ans = 0;
	for (int i = 0; i < testcases; ++i) {
		ans = 0;
		cin >> n;

		//cout << "case : " << n << "\n";

		base = "";
		possible = true;

		memset(&sum, 0, sizeof sum);

		cin >> input[0];
		for (int k = 0; k < input[0].length(); ++k) {
			base = calBase(distance[0], input[0]);

		}

		baselength = base.length();

		//cout << base << "\n";

		for (int j = 1; j < n && possible; ++j) {
			cin >> input[j];

			for (int k = 0; k < input[j].length(); ++k) {
				if (base.compare(calBase(distance[j], input[j])) != 0) {
					possible = false;
					break;
				}
			}
		}

		for (int k = 0; k < n; ++k) {
			for (int j = 0; j < base.length(); ++j) {
				sum[j] += distance[k][j];
			}
		}

		for (int j = 0; j < base.length(); ++j) {
				sum[j] = floor( ((float)sum[j]/(float)n) + 0.5 );
		}

		for (int k = 0; k < n; ++k) {
					for (int j = 0; j < base.length(); ++j) {
						ans += abs(sum[j] - distance[k][j]);
					}
				}


		cout << "Case #" << i + 1 << ": ";
		if (!possible)
			cout << "Fegla Won\n";
		else
			cout << ans << "\n";
	}

	return 0;
}

string calBase(int dist[], string input) {
	string base = "";
	int distInd = 0;
	for (int k = 0; k < input.length(); ++k) {
		base += input.at(k);
		dist[distInd]=0;

		while (k < input.length() - 1 && input.at(k + 1) == input.at(k)) {
			++k;
			dist[distInd]++;
		}
		distInd++;
	}

	return base;
}
/*
 void calDist(int dist[], string input)
 {
 //int distance=0;
 int distInd = 0;
 for(int k =0;k< input.length();++k)
 {
 while(k < input.length()-1 && input.at(k+1)==input.at(k))
 {
 ++k;
 dist[distInd]++;
 }
 distInd++;
 }


 }*/
