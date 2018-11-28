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

int a[13][1<<12];
string str[13][1<<12];

int main(void) {
	ifstream ifs("input.txt");
	FILE *fp;
	fp = fopen("out.txt","w");
	int t;
	ifs >> t;
	REP(cas,t){		
		fprintf(fp,"Case #%d: ",cas+1);

		int n, r, p, s;
		ifs >> n >> r >> p >> s;

		bool f = 0;

		REP(k,3){
			a[0][0] = k;
			REP(i,n){
				REP(j,1<<i){
					if (a[i][j]==0){
						a[i+1][2*j] = 0;
						a[i+1][2*j+1] = 2;
					}
					if (a[i][j]==1){
						a[i+1][2*j] = 1;
						a[i+1][2*j+1] = 0;
					}
					if (a[i][j]==2){
						a[i+1][2*j] = 1;
						a[i+1][2*j+1] = 2;
					}
				}
			}
			int h[3] = {};
			REP(j,1<<n){
				h[a[n][j]]++;
			}
			if (h[0]==r && h[1]==p && h[2]==s){
				f = 1;
				string hand = "RPS";
				REP(j,1<<n){
					str[0][j] = hand[a[n][j]];
				}
				REP(i,n){
					REP(j,1<<(n-i-1)){
						string x = str[i][2*j]+str[i][2*j+1];
						string y = str[i][2*j+1]+str[i][2*j];
						if (x<y)
							str[i+1][j] = x;
						else
							str[i+1][j] = y;
					}
				}
				fprintf(fp,"%s\n", str[n][0].c_str());
				break;
			}
		}

		if (!f)
			fprintf(fp,"IMPOSSIBLE\n");


	}

	return 0;
}