#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <exception>
#include <numeric>

using namespace std;

typedef long long lo;
typedef vector< vector<long long> > vvl;
typedef vector< long long> vl;
typedef pair<lo, lo> ll;
typedef vector< ll > vll;
typedef vector< vll > vvll;
typedef pair<long, pair<long, long>> lll;
typedef vector<lll> vlll;
typedef vector<vvl> vvvl;
typedef vector<set<long>> vs;

char buff[2100];
long digits[10];

void solve(){
	map<char, lo> ch;
	lo n=strlen(buff);
	for (lo i=0;i<n;i++)
		ch[buff[i]]++;
	for (lo i=0;i<10;i++)
		digits[i]=0;
	while (ch['Z']>0){
		digits[0]++;
		ch['Z']--;
		ch['E']--;
		ch['R']--;
		ch['O']--;
	}
	while (ch['W']>0){
		digits[2]++;
		ch['T']--;
		ch['W']--;
		ch['O']--;
	}
	while (ch['X']>0){
		digits[6]++;
		ch['S']--;
		ch['I']--;
		ch['X']--;
	}
	while (ch['U']>0){
		digits[4]++;
		ch['F']--;
		ch['O']--;
		ch['U']--;
		ch['R']--;
	}
	while (ch['S']>0){
		digits[7]++;
		ch['S']--;
		ch['E']--;
		ch['V']--;
		ch['E']--;
		ch['N']--;
	}
	while (ch['R']>0){
		digits[3]++;
		ch['T']--;
		ch['H']--;
		ch['R']--;
		ch['E']--;
		ch['E']--;
	}
	while (ch['T']>0){
		digits[8]++;
		ch['E']--;
		ch['I']--;
		ch['G']--;
		ch['H']--;
		ch['T']--;
	}
	while (ch['V']>0){
		digits[5]++;
		ch['F']--;
		ch['I']--;
		ch['V']--;
		ch['E']--;
	}
	while (ch['O']>0){
		digits[1]++;
		ch['O']--;
		ch['N']--;
		ch['E']--;
	}
	while (ch['N']>0){
		digits[9]++;
		ch['N']--;
		ch['I']--;
		ch['N']--;
		ch['E']--;
	}

	for (lo i=0;i<10;i++)
		while (digits[i]--)
			printf("%I64d", i);
	printf("\n");
}
int main() {
	freopen("A-large(1).in","r",stdin);
	freopen("out.txt","w",stdout);
	lo t, n;
	scanf("%I64d", &t);
	for (lo i=0;i<t;i++){
		scanf("%s", &buff);
		printf("Case #%I64d: ", i+1);
		solve();
	}
	return 0;
}