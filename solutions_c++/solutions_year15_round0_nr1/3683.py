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

int main(){
	ios_base::sync_with_stdio(false);
	ifstream in("A.in");
	ofstream out("result.txt");
	int T;
	in >> T;
	for (int test = 0; test < T; test++){
		int Smax;
		vector<int> S;
		cout << "Case #" << test+1 << ": ";
		out << "Case #" << test + 1 << ": ";
		in >> Smax;
		for (int i = 0; i <= Smax; i++){
			char k;
			in >> k;
			for (int j = 0; j < (int)(k-'0'); j++)
				S.push_back(i);
		}

		int previous = 0, ret = 0;
		for (int i = 0; i < S.size(); i++){
			if (S[i]>previous){
				int dif = (S[i] - previous);
				ret += dif;
				previous += dif;
			}
			previous++;
		}

		cout << ret << endl;
		out << ret << endl;
	}
	return 0;
}
