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

char buff[400];

void solve(){
	lo n = strlen(buff);
	lo turns=0;
	for (lo i=n-1;i>=0;i--)
		if (buff[i]=='-' ^ turns%2==1) turns++;
	printf("%I64d\n", turns);
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	lo t;
	scanf("%I64d", &t);
	for (lo i=0;i<t;i++){
		scanf("%s", &buff);
		printf("Case #%I64d: ", i+1);
		solve();
	}
	return 0;
}