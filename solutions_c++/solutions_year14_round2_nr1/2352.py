#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long LL;


ifstream fin ("C:\\CodeJam\\2014\\1B\\A\\A-small-attempt1.in");
ofstream fout ("C:\\CodeJam\\2014\\1B\\A\\A-small-attempt1.out");

int testCase = 0;

/*

who are you stop looking i dont like you

for (int i = 0; i < N; i++)
for (int j = 0; j < N; j++)
for (int k = 0; k < N; k++)

std::sort(A, A + N, std::less<int>());

vector.erase(vector.begin()+i);

*/

string S[100];
int IS[100];
int COUNT[100];

void Solve()
{

	int N;

	fin>>N;
	
	string word;

	for (int i = 0; i < N; i++) {

		fin>>S[i];

	}
	for (int i = 0; i < N; i++)
		IS[i] = 0;
	
	int total = 0;
	int i = 0;
	while (IS[0] < S[0].size()) {

		char c = S[0][IS[0]];

		for (int j = 0; j < N; j++) {

			if (IS[j] >= S[j].size() || S[j][IS[j]] != c) {
				fout << "Case #" << testCase << ": "<<"Fegla Won"<<endl;
				return;
			}
			
			int nexti = IS[j];

			while (nexti < S[j].size() && S[j][IS[j]] == S[j][nexti])
				nexti++;
			COUNT[j] = nexti-IS[j];
			IS[j] = nexti;
		}
		
		int maxCount = 0;
		for (int j = 0; j < N; j++) {
			maxCount = max(maxCount, COUNT[j]);
		}
		
		int minMove = 1000;
		for (int j = 1; j <= maxCount; j++) {
			int move = 0;
			for (int k = 0; k < N; k++) {
				move += abs(COUNT[k]-j);
			}

			minMove = min(minMove,move);

		}


		total += minMove;

		

	}
		
	
	for (int j = 0; j < N; j++) {
		if (IS[j] != S[j].size()) {
			fout << "Case #" << testCase << ": "<<"Fegla Won"<<endl;
			return;
		}
	}



	fout << "Case #" << testCase << ": "<<total<<endl;

}




void main()
{

	fout.precision(15);
	cout.precision(15);
	

	int TestCases = 0;
	fin>>TestCases;

	for (testCase = 1; testCase <= TestCases; testCase++) {
		
		Solve();
		if (testCase == 1+TestCases/20) {
			cout<<"5%"<<endl;
		} else if (testCase == 1+TestCases/4) {
			cout<<"25%"<<endl;
		} else if (testCase == 1+2*TestCases/4) {
			cout<<"50%"<<endl;
		} else if (testCase == 1+3*TestCases/4) {
			cout<<"75%"<<endl;
		}

	}

	cout<<"100%"<<endl;
	cout<<"finished"<<endl;
	getchar();

}



