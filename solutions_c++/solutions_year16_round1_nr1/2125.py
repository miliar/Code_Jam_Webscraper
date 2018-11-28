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
#define TR(i,x) for(typedef((x).begin())i=x.begin();i!=x.end();i++)
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

string ans[1100];


string win(string s) {

	int len = s.size();
	
	if (ans[len] != "")
		return ans[len];
	

	if (len == 1)
		return s;

	//cout << s << endl;
	string last =  s.substr(len - 1, 1);
	string first = win(s.substr(0, len - 1));
	
	if (s[len - 1] >= first[0]) {
	//	cout<<last<<" "<<first<<endl;
		ans[len] = last + first;
		cout<<ans[len]<<endl;
		return last + first;
	}
	else {
	//	cout<<first<<" "<<last<<endl;;
		ans[len] = first + last;
		cout<<ans[len];
		return first + last;
	}
}



int main()
{
	std::ifstream fin("A_large.txt", std::ifstream::in);
	std::ofstream fout("A_large_out.txt", std::ifstream::out);

	int no_tc;
	fin >> no_tc;

	for (int tc = 1; tc <= no_tc; tc++) {
		vector<string>::iterator x;
		REP (i,0,1100){
			ans[i] = "";
		}
		//cout<<ans.size()<<endl;
		
		string s;
		fin >> s;
		
		fout<<"Case #"<<tc<<": ";
		fout<<win(s)<<endl;
		

	}

	return 0;
}

