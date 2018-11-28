#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cctype>
#include <climits>
#include <string>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define INF	(int)1e9
#define EPS 1e-9

int main(){
	int casenum;
	cin >> casenum;

	for(int i = 0; i < casenum; i++){
		int n;
		cin >> n;
		vector<string> vect;

		string in;
		for(int j = 0; j < n; j++){
			cin >> in;
			vect.push_back(in);
		}

		vector<vi> counts;
		for(int j = 0; j < n; j++) counts.push_back(vi());
		vector<char> chars;


		char prev = vect[0][0];
		chars.push_back(prev);
		for(int j = 1; j < vect[0].length(); j++){
			if(vect[0][j] != prev){
				chars.push_back(vect[0][j]);
				prev = vect[0][j];
			} 
		}

		bool notfound = false;
		for(int j = 0; j < n; j++){
			char ch_idx = -1;
			char prev = '0';

			int k = 0;
			while(k < vect[j].length()){
				if(vect[j][k] == prev) counts[j][ch_idx]++;
				else{
					prev = vect[j][k];
					ch_idx++;
					if(chars[ch_idx] != prev){
						notfound = true;
						break;
					}
					counts[j].push_back(1);
				}
				k++;
			}
			if(notfound) break;
		}

		// for(int j = 0; j < n; j++){
		// 	for(int k = 0; k < counts[j].size(); k++){
		// 		printf("%d ", counts[j][k]);
		// 	}
		// 	printf("\n");
		// }
		// printf("\n");
		int sz = counts[0].size();
		for(int j = 1; j < n; j++){
			if(counts[j].size() != sz){notfound = true; break;}
		}

		if(notfound){
			printf("Case #%d: Fegla Won\n", i+1);
		} else{
			int moves = 0;
			for(int j = 0; j < chars.size(); j++){
				int tot = 0;
				double avg; 
				for(int k = 0; k < n; k++){
					tot += counts[k][j];
				}
				avg = round((double)tot / (double)n);
				// cout << avg << endl;
				for(int k = 0; k < n; k++){
					moves += abs(counts[k][j] - avg);
				}
			}

			printf("Case #%d: %d\n", i+1, moves);
		}
	}
}