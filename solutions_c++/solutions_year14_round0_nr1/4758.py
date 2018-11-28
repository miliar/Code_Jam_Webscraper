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
	int datas[2][4];
	int casenum;
	cin >> casenum;

	for(int i = 0; i < casenum; i++){
		int row1, row2, dummy, count = 0, match;
		cin >> row1;
		for(int j = 1; j <= 4; j++){
			if(j == row1){
				cin >> datas[0][0] >> datas[0][1] >> datas[0][2] >> datas[0][3];
			} else {
				cin >> dummy >> dummy >> dummy >> dummy;
			}
		}
		cin >> row2;
		for(int j = 1; j <= 4; j++){
			if(j == row2){
				cin >> datas[1][0] >> datas[1][1] >> datas[1][2] >> datas[1][3];
			} else {
				cin >> dummy >> dummy >> dummy >> dummy;
			}
		}

		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				if(datas[0][j] == datas[1][k]){
					count++;
					match = datas[0][j];
					break;
				}
			}
		}

		if(count == 0){
			printf("Case #%d: Volunteer cheated!\n", i + 1);
		} else if(count == 1){
			printf("Case #%d: %d\n", i + 1, match);
		} else{
			printf("Case #%d: Bad magician!\n", i + 1);
		}
	}
}