#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <ctime>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define fs first
#define sc second
#define abs(a) ((a)<0?-(a):(a))
#define sqr(a) ((a)*(a))

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;


const double eps = 1e-9;
const int mod = (int)1e+9 + 7;
const double pi = acos(-1.);
const int maxn = 100100;

char s[200][200];

int main() {

	#ifdef SOL
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	}
	#else
	srand(time(0));
	const string file = "";
	if(!file.empty()) {
		freopen((file + ".in").c_str(),"r",stdin);
		freopen((file + ".out").c_str(),"w",stdout);
	}
	#endif

	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; T++) {
		printf("Case #%d: ", T);
		int r, c;
		scanf("%d%d", &r, &c);
		for(int i = 0; i < r; i++) {
			scanf("\n");
			for(int f = 0; f < c; f++) {
				s[i][f] = getchar();
//				cout << s[i][f] << endl;
			}
		}
		bool ok = 1;
		int cnt = 0;
		for(int i = 0; i < r; i++) {
			for(int f = 0; f < c; f++) if(s[i][f] != '.') {
				bool okup = 0, okdown = 0, oklf = 0, okrg = 0;
				for(int g = 1; ; g++) {
					if(i - g < 0 && i + g >= r && f - g < 0 && f + g >= c) {
						break;
					}
					if(i - g >= 0 && s[i - g][f] != '.') {
						okup = 1;
					}
					if(i + g < r && s[i + g][f] != '.') {
						okdown = 1;
					}
					if(f - g >= 0 && s[i][f - g] != '.') {
						oklf = 1;
					}
					if(f + g < c && s[i][f + g] != '.') {
						okrg = 1;
					}
				}
				if(s[i][f] == '<' && !oklf) {
					cnt++;
					if(!(okrg || okup || okdown)) {
						ok = 0;
					}
				}
				if(s[i][f] == '>' && !okrg) {
					cnt++;
					if(!(oklf || okup || okdown)) {
						ok = 0;
					}
				}
				if(s[i][f] == '^' && !okup) {
					cnt++;
					if(!(oklf || okrg || okdown)) {
						ok = 0;
					}
				}
				if(s[i][f] == 'v' && !okdown) {
					cnt++;
					if(!(oklf || okup || okrg)) {
						ok = 0;
					}
				}
			}
		}
		if(ok) {
			printf("%d\n", cnt);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}

	return(0);
}

// by Kim Andrey
