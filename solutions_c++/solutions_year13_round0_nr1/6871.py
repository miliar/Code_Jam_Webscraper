#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <fstream>

using namespace std;

#define DEBUG(x) cout<< #x << ':' << x << endl
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define REP(i,n) FOR(i,0,n-1)
#define FORIT(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(), (a).end()
#define ZERO(a) memset(a, 0, sizeof(a))
#define PB push_back
#define MP make_pair
#define LEN(a) (int)(sizeof(a) / sizeof(a[0]))
#define abs(x) (((x)^((x)>>31))-((x)>>31))
const int inf = ~0u>>1;

typedef long long ll;

void tprint(int ii, string buf){
	printf("Case #%d: %s\n",ii,buf.c_str());
}

int main()
{
	int T;
	cin>>T;
	string a[4];
	FOR(ii,1,T){
		getchar();
		REP(i,4) getline(cin,a[i]);
		bool end = true;
		int state = 0;
		REP(i,4){
			int xcnt = 0;
			int ocnt = 0;
			REP(j,4){
				if (end && a[i][j] == '.') end=false;
				switch(a[i][j]){
					case 'X':xcnt++;break;
					case 'O':ocnt++;break;
					case 'T':xcnt++;ocnt++;break;
					default:break;
				}
			}
			if (xcnt == 4) {state = 1;break;}
			if (ocnt == 4) {state = -1;break;}
		}
		if (state == 0){
			REP(i,4){
				int xcnt = 0,ocnt = 0;
				REP(j,4){
					switch(a[j][i]){
						case 'X':xcnt++;break;
						case 'O':ocnt++;break;
						case 'T':xcnt++;ocnt++;break;
						default:break;
					}
				}
				if (xcnt == 4) {state = 1;break;}
				if (ocnt == 4) {state = -1;break;}
			}
		}
		if (state == 0){
			int xcnt = 0,ocnt = 0;
			REP(i,4){
				switch(a[i][i]){
					case 'X':xcnt++;break;
					case 'O':ocnt++;break;
					case 'T':xcnt++;ocnt++;break;
					default:break;
				}
			}
			if (xcnt == 4) state = 1;
			if (ocnt == 4) state = -1;
		}
		if (state == 0){
			int xcnt = 0,ocnt = 0;
			REP(i,4){
				switch(a[i][4-i-1]){
					case 'X':xcnt++;break;
					case 'O':ocnt++;break;
					case 'T':xcnt++;ocnt++;break;
					default:break;
				}
			}
			if (xcnt == 4) state = 1;
			if (ocnt == 4) state = -1;
		}
		if (state == 0){
			if (end) tprint(ii,"Draw");
			else tprint(ii,"Game has not completed");
		} else {
			if (state == 1) tprint(ii,"X won");
			else tprint(ii,"O won");
		}
	}
	return 0;
}
