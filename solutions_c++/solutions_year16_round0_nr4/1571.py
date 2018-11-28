#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORR(i,a,b) for (int i=a; i>=b; i--)
#define pi M_PI

typedef long long ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

int main(void) {
	ifstream ifs("input.txt");
	FILE *fp;
	fp = fopen("out.txt","w");
	int t;
	ifs >> t;
	REP(cas,t){
		fprintf(fp,"Case #%d: ",cas+1);
		int k,c,s;
		ifs >> k >> c >> s;
		REP(i,k){
			ll x = 1, ans = 1;
			REP(j,c){
				ans += i*x;
				x *= k;
			}
			fprintf(fp,"%lld ",ans);
		}
		fprintf(fp,"\n");
	}

	return 0;
}