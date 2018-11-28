#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X));
#define xx first
#define yy second
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

int cc[300], ret[10];

vector<string> tab;
void fillTab() {
	tab.pb("ZERO");
	tab.pb("ONE");
	tab.pb("TWO");
	tab.pb("THREE");
	tab.pb("FOUR");
	tab.pb("FIVE");
	tab.pb("SIX");
	tab.pb("SEVEN");
	tab.pb("EIGHT");
	tab.pb("NINE");
}

void take(int p) {
	for(int i=0;i<sz(tab[p]);i++) {
		cc[tab[p][i]]--;
	}
}

void printRet() {
	for(int i=0;i<=9;i++) {
		for(int j=ret[i];j>0;j--) {
			printf("%d",i);
		}
	}
}

int main(){
	int T;
	scanf("%d", &T);
	fillTab();
	for(int caso=1;caso<=T;caso++) {
		string s;
		cin >> s;
		memset(cc,0,sizeof(cc));
		memset(ret,0,sizeof(ret));
		for(int i=0;i<sz(s);i++) {
			cc[s[i]]++;
		}
		while(cc['Z']) {
			ret[0]++;
			take(0);
		}
		while(cc['W']) {
			ret[2]++;
			take(2);
		}
		while(cc['X']) {
			ret[6]++;
			take(6);
		}
		while(cc['G']) {
			ret[8]++;
			take(8);
		}
		while(cc['H']) {
			ret[3]++;
			take(3);
		}
		while(cc['R']) {
			ret[4]++;
			take(4);
		}
		while(cc['S']) {
			ret[7]++;
			take(7);
		}
		while(cc['V']) {
			ret[5]++;
			take(5);
		}
		while(cc['I']) {
			ret[9]++;
			take(9);
		}
		while(cc['O']) {
			ret[1]++;
			take(1);
		}
		printf("Case #%d: ", caso);
		printRet();
		printf("\n");
	}
	return 0;
}
