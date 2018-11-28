// File Name   : Magic.cpp
// Development : Sat Apr 12 10:45:27 2014
// Author      : Vishwakarma

#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <map>
#include <set>
#include <float.h>
#include <new>
#include <sstream>
#include <complex>
#include <deque>

#define TR(c,i) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); i++ ) 
#define SWAP(a,b) {typeof(a) T; T=a; a=b; b=T;}
#define FOR(i,a,b) for ( i = a; i <= b; i++ )
#define ROF(i,a,b) for ( i = a; i >= b; i-- )
#define MEM(t,n) ( t * )malloc( (n)*sizeof( t ) )
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort( ALL(v) )
#define MAX(a,b) ((a) >= (b) ? (a) : (b))
#define MIN(a,b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SET(x,a) memset(x,a,sizeof(x))
#define IN(x,a) x.find(a) != x.end()  
#define SQ(x) (x)*(x)
#define DIST(x1,y1,x2,y2) SQ(x1-x2)+SQ(y1-y2)
#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

int store[5][5];

int main()
{
	int T, A;
	cin >> T;
	for(int k=1;k<=T;k++){
		cin >> A;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin >> store[i][j];
			}
		}
		set<int> row,row1;
		for(int i=0;i<4;i++){
			row.insert(store[A-1][i]);
		}
		cin >> A;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin >> store[i][j];
			}
		}
		for(int i=0;i<4;i++){
			row1.insert(store[A-1][i]);
		}
		set<int>::iterator it;
		int count = 0, val;
		for(it = row.begin(); it != row.end(); it++){
			if(row1.find(*it) != row1.end()){
				count++;
				val = *it;
			}
		}
		if(count == 1){
			cout << "Case #" <<k<<": " <<val << "\n";
		}
		else{
			if(count > 1){
				cout << "Case #" <<k<<": Bad magician!" << "\n";
			}
			else{
				if(count == 0){
					cout << "Case #" <<k<<": Volunteer cheated!" << "\n";
				}
			}
		}
	}
	return 0;
}

