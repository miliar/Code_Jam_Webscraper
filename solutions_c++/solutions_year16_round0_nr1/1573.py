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
	REP(s,t){
		fprintf(fp,"Case #%d: ",s+1);
		ll n;
		ifs >> n;
		if (n==0){
			fprintf(fp,"INSOMNIA\n");
			continue;
		}
		ll x = 0;
		int a = 0;
		bool f[10] = {};
		while(a<10){
			x += n;
			ll y = x;
			while(y){
				int s = y%10;
				y /= 10;
				if (!f[s]){
					f[s] = 1;
					a++;
				}
			}
		}
		fprintf(fp,"%lld\n",x);
	}

	return 0;
}