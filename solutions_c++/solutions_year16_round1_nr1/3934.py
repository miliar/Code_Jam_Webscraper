// A_TheLastWord.cpp

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
#include <string.h>   
//#include <bits/stdc++.h>

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

#define rep(i, a, b) for(int i = a; i < b; i++)
#define S(x) scanf("%d", &x)
#define S2(x, y) scanf("%d %d", &x, &y)
#define S3(x, y, z) scanf("%d %d %d", &x, &y, &z)
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

string getAns(string line){

	string ans = "";
	ans += line.at(0);

	for(int i = 1; i < line.size(); i++){

		if(line.at(i) >= ans.at(0))
			ans = line.at(i) + ans;

		else
			ans += line.at(i);
	}

	return ans;
} 

int main(){

	int cases;
	S(cases);

	string line;

	for1(i, cases){

		cin>>line;
		printf("Case #%d: ", i);
		cout<<getAns(line)<<endl;
	}

	return 0;
}