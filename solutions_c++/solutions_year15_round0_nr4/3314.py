#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
#include <climits>
#include <bitset>

using namespace std;

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;

#define INF 1e9
#define EPS 1e-9
#define PI acos(-1.0)
#define MOD 1234567

int canFill(int X, int R, int C) {
	if((R * C) % X != 0) return 0;
	if(X <= 2) return 1;
	if(X == 3) return R > 1 && C > 1;
	if(X == 4) return (R >= 3 && C == 4) || (R == 4 && C >= 3);	
}


int main() {		
	// open files
	//freopen("homework.txt","r",stdin);
    //freopen("output.txt","w",stdout);	

	ofstream fout ("D_out.txt");
    ifstream fin ("D-small-attempt1.in");
	
	int T, X, R, C, caseNo = 1;

	fin >> T;
	while(T--) {
		fin >> X >> R >> C;
		
		fout << "Case #" << (caseNo++) << ": " << (canFill(X, R, C) ? "GABRIEL" : "RICHARD") << endl;
	}

	
	//system ("pause");
	return 0;	
}