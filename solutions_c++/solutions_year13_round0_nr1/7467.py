#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include<iostream>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

//global variables

//some functions

int main() {
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int t;
	scanf("%d", &t);  //case num
	FOR(test, 1, t) {
		char tb[4][4];
		FOR(i,0,3){
		scanf("%s", tb[i]); 
		}
		char result='Z';
		//draw
		FOR(i,0,3)
		 FOR(j,0,3){
			if (tb[i][j]=='.')
				result='A';
			    break;
		}


		FOR(j,0,3){
			//check row
         if (tb[j][0]!='.' && tb[j][0]==tb[j][1] && tb[j][0]==tb[j][2] && tb[j][0]==tb[j][3])
			 result=tb[j][0];

		 if (tb[j][0]=='T' && tb[j][1]!='.' && tb[j][1]==tb[j][2] && tb[j][1]==tb[j][3])
			 result=tb[j][1];

         if (tb[j][1]=='T' && tb[j][0]!='.' && tb[j][0]==tb[j][2] && tb[j][0]==tb[j][3])
			 result=tb[j][0];

		 if (tb[j][2]=='T' && tb[j][0]!='.' && tb[j][0]==tb[j][1] && tb[j][0]==tb[j][3])
			 result=tb[j][0];

		 if (tb[j][3]=='T' && tb[j][0]!='.' && tb[j][0]==tb[j][2] && tb[j][0]==tb[j][1])
			 result=tb[j][0];

		 //check col
		  if (tb[0][j]!='.' && tb[0][j]==tb[1][j] &&  tb[0][j]==tb[2][j] &&  tb[0][j]==tb[3][j])
			 result=tb[0][j];

		 if (tb[0][j]=='T' && tb[1][j]!='.' && tb[1][j]==tb[2][j] && tb[1][j]==tb[3][j])
			 result=tb[1][j];

         if (tb[1][j]=='T' && tb[0][j]!='.' && tb[0][j]==tb[2][j] && tb[0][j]==tb[3][j])
			 result=tb[0][j];

		 if (tb[2][j]=='T' && tb[0][j]!='.' && tb[0][j]==tb[1][j] && tb[0][j]==tb[3][j])
			 result=tb[0][j];

		 if (tb[3][j]=='T' && tb[0][j]!='.' && tb[0][j]==tb[2][j] && tb[0][j]==tb[1][j])
			 result=tb[0][j];
		}
		 //check diag
          if (tb[0][0]!='.' && tb[0][0]==tb[1][1] && tb[0][0]==tb[2][2] && tb[0][0]==tb[3][3])
			 result=tb[0][0];
		 if (tb[0][0]=='T' && tb[1][1]==tb[2][2] && tb[1][1]==tb[3][3] && tb[1][1]!='.')
			 result=tb[1][1];
		 if (tb[0][0]!='.' && tb[1][1]=='T' && tb[0][0]==tb[2][2] && tb[0][0]==tb[3][3])
			 result=tb[0][0];
		 if (tb[0][0]!='.' && tb[2][2]=='T' && tb[0][0]==tb[1][1] && tb[0][0]==tb[3][3])
			 result=tb[0][0];
		 if (tb[0][0]!='.' && tb[3][3]=='T' && tb[0][0]==tb[1][1] && tb[0][0]==tb[2][2])
			 result=tb[0][0];
	     //check reverse diag
          if (tb[3][0]!='.' && tb[3][0]==tb[1][2] && tb[3][0]==tb[2][1] && tb[3][0]==tb[0][3])
			 result=tb[3][0];
		 if (tb[3][0]=='T' && tb[1][2]!='.' && tb[1][2]==tb[2][1] && tb[1][2]==tb[0][3])
			 result=tb[1][2];
		 if (tb[1][2]=='T' && tb[3][0]!='.' && tb[3][0]==tb[2][1] && tb[3][0]==tb[0][3])
			 result=tb[3][0];
		 if (tb[2][1]=='T' && tb[3][0]!='.' && tb[3][0]==tb[1][2] && tb[3][0]==tb[0][3])
			 result=tb[3][0];
		 if (tb[0][3]=='T' && tb[3][0]!='.' && tb[3][0]==tb[2][1] && tb[3][0]==tb[1][2])
			 result=tb[3][0];

		
		
		printf("Case #%d: ", test); //test cases
		if (result=='O' ||result=='X')
				printf("%c won ", result); 
		if (result=='Z')
				printf("Draw");
	    if (result=='A')
				printf("Game has not completed"); 
	    printf("\n");
		
	
		 
		// FOR(i,0,3)
		// FOR(j,0,3){
		//	tb[i][j]=='-';

		//}
		
	}

	exit(0);
}