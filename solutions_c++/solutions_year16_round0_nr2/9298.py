// B_Pancakes.cpp

#include <iostream>
#include <vector>
#include <iomanip>
#include <queue>
#include <string>
#include <math.h>
#include <functional>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <cstdio>
#include <bitset>
#include <algorithm>    

using namespace std;

//Shortcuts for "common" data types in contests
typedef long long int ll;
typedef pair<int, int > pii;
typedef vector<int > vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

//  ans = a ? b : c;                    //To simplify: if(a) ans = b; else ans = c
//  ans += val;                         //To simplify: ans = ans + val;
//  index = (index + 1)%n;          
//  index = (index + n - 1)%n;
//  int ans = (int)((double)d + 0.5);   //For rounding to the nearest integer
//  ans = min(ans, new_computation);    //min/max shortcut

#define INF 1000000000
#define rep(i, a, b) for(int i = a; i < b; i++)
#define S(x) scanf("%d", &x)
#define S2(x, y) scanf("%d%d", &x, &y)
#define S3(x, y, z) scanf("%d%d%d", &x, &y, &z)
#define P(x) printf("%d\n", x)
#define all(v) v.begin(), v.end()
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

/*
	- - + -
	+ + + - 
	- - - +
	+ + + +

	0010     2
	1110    14
	0001     1  
	1111    15

	+ + - + + + - - 
	- - + + + + - - 
	+ + + + + + - -
	- - - - - - + +
	+ + + + + + + +

	Idea:
	
		Definitions:

			Hole: set of adjacent '-' signs
			Low hole: hole which is located at the start of the string
			Deep hole: hole which is NOT located at the start of the string

		Strategy:
	
			Each deep hole adds up +2, while each low hole adds up +1
*/

int iStart, iEnd;

void getNextHoleIndex(string line, int index){

	iStart = index;

	while(iStart < line.size() && line.at(iStart) != '-')
		iStart++;

	iEnd = iStart + 1;

	while(iEnd < line.size() && line.at(iEnd) != '+')
		iEnd++;
}

int getTotalSum(string line){

	int totSum = 0;
	
	int j = 0;

	while(j < line.size()){

		getNextHoleIndex(line, j);

		if(iStart == 0)
			totSum++;

		else if(iStart != 0 && iStart < line.size())
			totSum += 2;
		
		j = iEnd + 1;
	}

	return totSum;
}

int main(){

	int cases;
	S(cases);

	string line;

	for1(i, cases){

		cin>>line;
		iStart = 0;
		iEnd = 0;
		printf("Case #%d: %d\n", i, getTotalSum(line));
	}

	return 0;
}