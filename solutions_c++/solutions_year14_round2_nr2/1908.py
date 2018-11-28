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
		int a, b, k;
		int count = 0;
		cin >> a >> b >> k;

		for(int j = 0; j < a; j++){
			for(int l = 0; l < b; l++){
				if ((j & l) < k) count++;
			}
		}

		// for(int j = 0; j < b; j++){
		// 	for(int l = 0; l < a; l++){
		// 		if ((j & l) < k) count++;
		// 	}
		// }

		printf("Case #%d: %d\n", i+1, count);
	}
}