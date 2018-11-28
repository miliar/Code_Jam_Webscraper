// -*- compile-command: "g++ -o main -Wall -Wextra -g lawnmower.cpp" -*-
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <vector>
#include <utility>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <sstream>
#include <stack>
#define FOR(i,c) for(__typeof(c.begin()) i=c.begin();i!=c.end();++i)
using namespace std;

int field[100][100] = {};
int greatestInRow[110] = {};
int greatestInColumn[110] = {};

int main() {

    int T;
    scanf("%d", &T);
    for( int t = 0; t < T; t++ ) {	
	int N, M;
	scanf("%d %d", &N, &M);

	for( int i=0;i<N;i++) {
	    for(int j=0;j<M;j++) {
		scanf("%d", &field[i][j]);
	    }
	}

	for(int i=0; i<N;i++) {
	    int greatest = -1;
	    for(int j=0; j<M;j++) {
		greatest = max(greatest,field[i][j]);
	    }
	    greatestInRow[i] = greatest;
	}

	for( int j=0; j<M;j++) {
	    int greatest = -1;
	    for( int i =0;i<N;i++) {
		greatest = max(greatest,field[i][j]);
	    }
	    greatestInColumn[j] = greatest;
	}

	bool isPossible = true;
	for( int i=0;i<N;i++) {
	    for(int j=0;j<M;j++) {
		if( !(field[i][j] >= greatestInRow[i] || field[i][j] >= greatestInColumn[j] ))
		    isPossible = false;
	    }
	}
	if( isPossible )
	    printf("Case #%d: YES\n", t+1);
	else
	    printf("Case #%d: NO\n", t+1);
    }
  return 0;
}
