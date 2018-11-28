// Lupus Nocawy 2016
// Google Code Jam 2016
// Round 1B 2016
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/11254486/dashboard
// Problem A. Getting the Digits

#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,b) for(int i=(a), _b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a), _b=(b); i>=_b; --i)
#define IT(i,x) __typeof__(x) i=x
#define FOREACH(it,x) for(__typeof__((x).begin()) it=(x).begin(); it!=(x).end(); ++it)
#define ALL(x) x.begin(),x.end()
#define MP make_pair
#define PB push_back
#define DEBUG(x) if(debug) cout << x << endl;
typedef long long int lli;
typedef unsigned long long int llu;
typedef pair<int,int> pii;
const int debug=0;

const int INF = 2147483647;
const int max_n = 2147483647;

int T[200];
int chars=0;
vector<int> result;

bool isInTable(string s){
	if(chars==0)
		return 0;
	int l = s.size();
	REP(i,l){
		if(T[(int)s[i]]==0)
			return 0;
	}
	return 1;
}

void deductFromTable(string s){
	int l = s.size();
	REP(i,l)
		T[(int)s[i]]--;
	chars -= l;
}

bool tryAndDeductFromTable(string s){
	if(chars==0)
		return 0;
	int l = s.size();
	bool enoughChars = true;
	REP(i,l){
		T[(int)s[i]]--;
		if(T[(int)s[i]]<0)
			enoughChars = false;
	}
	if(enoughChars==false){ //put them back
		REP(i,l)
			T[(int)s[i]]++;
		return 0;
	}
	else
		return 1;
}

void iterate(string s, int d){
	while(tryAndDeductFromTable(s)){
		result.PB(d);
		//printf("%d", d);
	}
}

void solve(int c){
	REP(i,200)
		T[i]=0;
	result.clear();
	
	char S[2002];
	scanf("%s ", S);
	int l = strlen(S);
	chars = l;
	
	REP(i,l){
		T[(int)S[i]]++;
	}
	
	// the order matters
	iterate("ZERO", 0);
	iterate("SIX", 6);
	iterate("SEVEN", 7);
	iterate("FIVE", 5);
	iterate("FOUR", 4);
	iterate("THREE", 3);
	iterate("EIGHT", 8);
	iterate("NINE", 9);
	iterate("TWO", 2);
	iterate("ONE", 1);
	
	sort(result.begin(), result.end());
	for(unsigned int i=0; i<result.size(); ++i)
		printf("%d", result[i]);
	
	printf("\n");
	return;
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c){
		printf("Case #%d: ", c);
		solve(c);
	}
	return 0;
}

/*
WEIGHFOXTOURIST
EIGHFOXTURIS
IGFOXUIS

*/
