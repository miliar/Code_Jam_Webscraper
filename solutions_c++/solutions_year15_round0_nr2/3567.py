#include <iomanip>
#include <algorithm>
#include <iterator>     // std::insert_iterator
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

int calc(vector<int> &P, int minimum){
	int ret = 0;
	for (int i = 0; i < P.size(); i++){
		if (P[i] <= minimum) continue;
		ret += P[i] / minimum;
		if (P[i] % minimum != 0) ret++;
		ret--;
	}
	return ret;
}

int solve(vector<int> &P){
	sort(P.rbegin(), P.rend());
	int ret = P[0] + 1;;
	for (int normal = P[0]; normal >= 1; normal--){
		ret = min(ret, calc(P, normal)+normal);
	}
	return ret;
}


int main(){
	ios_base::sync_with_stdio(false);
	ifstream in("A.in");
	ofstream out("result.txt");
	int T;
	in >> T;
	for (int test = 0; test < T; test++){
		int D;
		cout << "Case #" << test+1 << ": ";
		out << "Case #" << test + 1 << ": ";
		in >> D;
		vector<int> P(D);
		for (int i = 0; i <D; i++){
			in >> P[i];
		}
		vector<int> P2 = P;
		int ret = solve(P);
		cout << ret << endl;
		out << ret << endl;
	}
	return 0;
}
