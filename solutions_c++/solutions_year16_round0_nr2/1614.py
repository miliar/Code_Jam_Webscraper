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
		string str;
		ifs >> str;
		int n = str.length();
		VI a(n);
		REP(i,n) a[i]=(str[i]=='+');
		int ans = 0;
		int f=1;
		FORR(i,n-1,0){
			if (a[i]!=f){
				ans++;
				f^=1;
			}
		}
		fprintf(fp,"%d\n",ans);
		cout << ans << endl;
	}

	return 0;
}