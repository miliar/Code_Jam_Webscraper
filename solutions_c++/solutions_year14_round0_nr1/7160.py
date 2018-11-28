#include <iostream>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
using namespace std;

typedef unsigned long long ull;
typedef vector<int> vi;
#define SZ(v) (int)(v.size())

void solve(int testcase){
	int first,second;
	int grid1[4][4],grid2[4][4];
	cin >> first;
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			cin >> grid1[i][j];
		}
	}
	cin >> second;
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			cin >> grid2[i][j];
		}
	}

	printf("Case #%d: ",testcase);
	
	first--;second--;
	vi possible;
	possible.clear();
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			if(grid1[first][i] == grid2[second][j]) possible.push_back(grid1[first][i]);
		}
	}
	if(SZ(possible) == 0) cout << "Volunteer cheated!";
	else if (SZ(possible) > 1 ) cout << "Bad magician!";
	else{
		cout << possible[0];
	}
	cout << endl;

}

int main() {
	int testcases;
	cin >> testcases;
	for(int i=1; i<=testcases; i++){
		solve(i);
	}
	return 0;
}

