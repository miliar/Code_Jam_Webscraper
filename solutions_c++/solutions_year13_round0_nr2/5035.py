#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <memory.h>
#include <stdio.h>
#include <vector>
#include <fstream>
#include <math.h>
using namespace std;


#define R(x) scanf("%d",&x);
#define FOR(i,j) for(int i = 0;i < j;i++)
#define i64 long long
#define N 110

ofstream myfile ("/Users/mac/Desktop/ans.txt");
ifstream infile ("/Users/mac/Desktop/A-large.in");

int table [N][N];
int n,m;


bool check(int i,int j) {

	int value = table[i][j];
	int x = i;
	int y = j;
	bool flag1 = true;

	for(; y < m ; y++) {
		if(table[x][y] > value) {
			flag1 = false;
			break;
		}
	}

	y = j;
	bool flag2 = true;
	for(; y >= 0 ; y--) {
		if(table[x][y] > value) {
			flag2 = false;
			break;
		}
	}

	if(flag1 && flag2)
		return true;

	x = i;
	y = j;
	bool flag3 = true;
	for(; x < n ; x++) {
		if(table[x][y] > value) {
			flag3 = false;
			break;
		}
	}

	x = i;
	y = j;
	bool flag4 = true;
	for(; x >= 0 ; x--) {
		if(table[x][y] > value) {
			flag4 = false;
			break;
		}
	}

	if(flag3 && flag4)
		return true;

	return false;
}


 int main() {

	int t;
	infile >> t;

	for(int i=1;i<=t;i++) {
		memset(table,0,sizeof table);
		infile >> n >> m;
		FOR(x,n) {
			FOR(y,m) 
				infile >> table[x][y];
		}
		bool checker = true;
		FOR(x,n) {
			FOR(y,m) {
				if(!check(x,y)) {
					myfile << "Case #" << i << ": NO\n";
					checker = false;
					x = n;
					y = m;
				}				
			}
		}
		if(checker)
			myfile << "Case #" << i << ": YES\n";


	}

}




