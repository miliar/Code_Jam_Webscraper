// codejam.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h> 

using namespace std;

#define INF (int)1e9
#define EPS (double)(1e-9)
#define PI (double)(3.141592653589793)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<string, int> si;
typedef pair<int, ii> iii;
typedef vector <si> vsi;
typedef vector <ii> vii;
typedef vector <int> vi;
typedef vector <char> vc;
typedef vector <string> vs;
typedef vector<vector<int> > vvi;


#define REP(i,a,b) for(int i=a;i<b;i++)
//#define TR(i,x) for(typedef(x.begin()) i=x.begin();i!=x.end();i++)
#define pb push_back
#define mp make_pair


void(*func)(vi elements) = NULL;

void forEachCombination(vi elements, int k) {
	static vi comb;

	if (k == 0) {
		func(comb);
		return;
	}

	if (elements.size() < k) {
		return;
	}

	comb.push_back(elements[0]);
	elements.erase(elements.begin());
	forEachCombination(elements, k - 1);
	comb.pop_back();
	forEachCombination(elements, k);
}


void forEachFullPermutation(vi elements) {

	sort(elements.begin(), elements.end());
	do {
		func(elements);
	} while (std::next_permutation(elements.begin(), elements.end()));
}



void forEachPermutation(vi elements, int k) {
	static vi comb;

	if (k == 0) {
		forEachFullPermutation(comb);
		return;
	}

	if (elements.size() < k) {
		return;
	}

	comb.push_back(elements[0]);
	elements.erase(elements.begin());
	forEachPermutation(elements, k - 1);
	comb.pop_back();
	forEachPermutation(elements, k);
}









/*void print(vi elements) {
	TR(i, elements) {
		printf("%d ", *i);
	}
	printf("\n");

}*/





int main()
{
	std::ifstream fin("B_large.txt", std::ifstream::in);
	std::ofstream fout("B_large_out.txt", std::ifstream::out);

	int no_tc;
	fin >> no_tc;

	for (int tc = 1; tc <= no_tc; tc++) {
	
		int  N;
		int list[100][100];
		fin >> N;
		REP (i, 0, (2*N-1)){
			REP(j, 0, N){
				fin >> list[i][j];
			}
		}


		int count[3000];
		REP(i, 0, 3000)
			count[i] = 0;
			
		REP (i, 0, (2*N-1)){
			REP(j, 0, N){
				count[list[i][j]]++;
			}
		}

		vi missing;
		REP(i, 0, 3000) {
			if (count[i] % 2 == 1)
				missing.push_back(i);
		}
		if (missing.size() != N){
			cout<<"Problem"<<endl;
		}
		
		std::sort (missing.begin(), missing.end());
		
		
		fout<<"Case #"<<tc<<": ";
		vi::iterator x;
		for (x=missing.begin(); x<missing.end(); x++){
			fout<<*x<<" ";
		}
		fout<<endl;



	}

	return 0;
}

