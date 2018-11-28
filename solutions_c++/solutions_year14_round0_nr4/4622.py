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
		int size, deceit = 0, war = 0;
		double input;
		vector<double> naomi, ken;

		cin >> size;
		for(int j = 0; j < size; j++){
			cin >> input;
			naomi.push_back(input);
		}
		for(int j = 0; j < size; j++){
			cin >> input;
			ken.push_back(input);
		}

		sort(naomi.begin(), naomi.end(), std::greater<double>());
		sort(ken.begin(), ken.end(), std::greater<double>());

		// for(int j = 0; j < size; j++){
		// 	if(naomi[j] > ken[j]) deceit++;
		// }

		int j = 0, k = 0;
		for(j = 0; j < size; j++){
			while(k < size && naomi[j] < ken[k]) k++;
			if(k >= size) break;
			deceit++;
			k++;
		}

		j = 0; k = 0;
		while(j < size && k < size){
			if(naomi[j] > ken[k]){
				war++;
				j++;
			} else {
				j++;
				k++;
			}
		}
		printf("Case #%d: %d %d\n", i+1, deceit, war);
	}
}