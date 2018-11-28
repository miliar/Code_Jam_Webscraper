// A_GettingTheDigits.cpp

#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <math.h>
#include <functional>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <bitset> 	
using namespace std;

// Shortcuts for "common" data types in contests
typedef long long int LL;
typedef pair<int, int > pii;
typedef vector<int > vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

#define INF 1000000000
#define rep(i, a, b) for(int i = a; i < b; i++)
#define S(x) scanf("%d", &x)
#define S2(x, y) scanf("%d%d", &x, &y)
#define P(x) printf("%d", x)
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

/*
	If there's a Z, there's a 0
	If there's a W, there's a 2
	If there's a T, there's a 3 or an 8
	If there's an X, there's a 6
	if there's a G, there's an 8
*/

vector<int> getNumbers(char letters[]){

	sort(letters, letters + strlen(letters));
	int bin[strlen(letters)];
	vector<int> ans;

	int i = strlen(letters) - 1;

	while(letters[i] == 'Z'){

		ans.pb(0);
		i--;
	}

	while(letters[i] == 'X'){

		ans.pb(6);
		i--;
	}

	while(letters[i] == 'W'){

		ans.pb(2);
		i--;
	}

	while(letters[i] == 'G'){

		ans.pb(8);
		i--;
	}

	sort(ans.begin(), ans.end());
	return ans;
}

vector<int> getNumbers2(char letters[]){

	// "ONE", "NINE"
	map<char, int> totLet;
	vector<int> ans;

	forn(i, strlen(letters))
		totLet[letters[i]]++;

	while(totLet['Z'] > 0){ //0

		ans.pb(0);
		totLet['Z']--;
		totLet['E']--;
		totLet['R']--;
		totLet['O']--;
	}

	while(totLet['W'] > 0){ //2

		ans.pb(2);
		totLet['T']--;
		totLet['W']--;
		totLet['O']--;
	}

	while(totLet['G'] > 0){ //8

		ans.pb(8);
		totLet['E']--;
		totLet['I']--;
		totLet['G']--;
		totLet['H']--;
		totLet['T']--;
	}

	while(totLet['X'] > 0){ //6

		ans.pb(6);
		totLet['S']--;
		totLet['I']--;
		totLet['X']--;
	}

	while(totLet['T'] > 0){ //3

		ans.pb(3);
		totLet['T']--;
		totLet['H']--;
		totLet['R']--;
		totLet['E']--;
		totLet['E']--;
	}

	while(totLet['U'] > 0){ //4

		ans.pb(4);
		totLet['F']--;
		totLet['O']--;
		totLet['U']--;
		totLet['R']--;
	}

	while(totLet['F'] > 0){ //5

		ans.pb(5);
		totLet['F']--;
		totLet['I']--;
		totLet['V']--;
		totLet['E']--;
	}

	while(totLet['V'] > 0){ //7

		ans.pb(7);
		totLet['S']--;
		totLet['E']--;
		totLet['V']--;
		totLet['E']--;
		totLet['N']--;
	}

	while(totLet['I'] > 0){ //9

		ans.pb(9);
		totLet['N']--;
		totLet['I']--;
		totLet['N']--;
		totLet['E']--;
	}

	while(totLet['O'] > 0){ //1

		ans.pb(1);
		totLet['O']--;
		totLet['N']--;
		totLet['E']--;
	}

	sort(ans.begin(), ans.end());
	return ans;
}

int main(){

	int cases;
	S(cases);

	char letters[2005];

	for1(i, cases){

		scanf("%s", letters);

		vector<int> ans = getNumbers2(letters);

		printf("Case #%d: ", i);
		forn(i, ans.size())
			P(ans[i]);

		printf("\n");
	}

	return 0;
}