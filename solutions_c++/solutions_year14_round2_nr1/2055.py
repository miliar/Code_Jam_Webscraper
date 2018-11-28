#define _CRT_SECURE_NO_DEPRECATE
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <map>
#include <list>
#include <sstream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <iomanip>
#include <queue>
#include <set>	
#include <cstring>
using namespace std;
typedef long long		ll;
typedef pair<int, int>	ii;
typedef pair<ii, int>	iii;
typedef vector<ii>		vii;
typedef vector<iii>		viii;
typedef vector<int>		vi;
typedef vector<char>	vc;
typedef vector<vc>		vvc;
typedef vector<string>	vs;
typedef unsigned long long	ull;
typedef vector<ull>		vul;
typedef vector<bool>	vb;
typedef vector<vi>		vvi;
typedef vector<vii>		vvii;
typedef vector<double>	vd;
#define INF 1000000000
#define PI 3.14159265


int main(int argc, char *argv[]){
	freopen("C:\\Users\\Vincent\\Desktop\\in.txt","r",stdin);
	freopen("C:\\Users\\Vincent\\Desktop\\out.txt","w",stdout);

	int T, N;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N;
		vector<string> words(N);
		for (int i=0; i<N; i++)  cin >> words[i];

		// use word 0 as basis
		vector<vector<char>> charseq(N);
		vector<vector<int>> charcount(N);

		for (int w_i = 0; w_i<N; w_i ++) {
			for (int i=0; i<words[w_i].size(); i++) {
				char c = words[w_i][i];

				int count_c = 1;
				while (words[w_i][i+1] == c) {
					count_c ++;
					i++;
				}
				charseq[w_i].push_back(c);
				charcount[w_i].push_back(count_c);
			}
		}

		// check if all char sequences are the same
		bool correct = true;
		for (int w_i = 0; correct && w_i<N; w_i ++) {
			if (charseq[w_i].size() != charseq[0].size()) {
				correct = false;
			} 
			for (int i=0; correct && i<charseq[w_i].size(); i++) {
				if (charseq[w_i][i] != charseq[0][i]) {
					correct = false;
				}
			}
		}

		if (correct) {
			// calculate most efficient (smallest distance)
			int total_sol = 0;
			for (int i=0; i<charcount[0].size(); i++) {

				int max_count = charcount[0][i];
				for (int n=0; n<N; n++) {
					if (charcount[0][i] > max_count) max_count = charcount[n][i];
				}
				int best_sol = INF;
				for (int cc=1; cc<=max_count; cc++) {
					int current_sol = 0;
					for (int n=0; n<N; n++) {
						current_sol += abs(charcount[n][i] - cc);
					}
					best_sol = min(current_sol,best_sol);
				}
				total_sol += best_sol;
			}
			cout << "Case #" << t <<": " << total_sol << endl;
		}
		else {
			cout << "Case #" << t <<": " << "Fegla Won" << endl;
		}
	}


	return EXIT_SUCCESS;
}