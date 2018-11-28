#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define pb(x) push_back(x)
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define RREP(i,x,y) for(int (i)=(y-1);(i)>=(x);i--)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define debug(x) cerr << #x << ": " << x << endl;
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<ii, int> tri;
typedef queue<int> qi;
typedef unsigned int uint;

const double PI = 3.14159265359;
const double E = 2.718281828459;

// 0: up
// 1: right
// 2: down
// 3: left

int r, c, flg, cnt, fnd;
int f, s;

char a;

int cod(char a){
	if (a == '.') return -1;
	if (a == '^') return 0;
	if (a == '>') return 1;
	if (a == 'v') return 2;
	if (a == '<') return 3;
}

int mk[110][110][4]; // (child id, direction)
int dir[110][110]; // actual direction

int main(){
	int nCases;
	scanf("%d", &nCases);
	REP(casenum,0,nCases){
		scanf("%d %d\n", &r, &c);

		REP(i,0,r) REP(j,0,c) REP(k,0,4) mk[i][j][k] = 0;

		REP(i,0,r) {
			REP(j,0,c){
				scanf("%c", &a);
				dir[i][j] = cod(a);
//				cout << "(" << i << "," << j << ") = " << cod(a) << endl;
			}
			scanf("\n");
		}

		REP(i,0,r){
			f = -1;
			REP(j,0,c){
				if (dir[i][j] >= 0){
					if (f != -1) mk[f][s][1] = 1;
					f = i;
					s = j;
				}
			}
		}
		REP(j,0,c){
			f = -1;
			REP(i,0,r){
				if (dir[i][j] >= 0){
					if (f != -1) mk[f][s][2] = 1;
					f = i;
					s = j;
				}
			}
		}
		REP(i,0,r){
			f = -1;
			RREP(j,0,c){
				if (dir[i][j] >= 0){
					if (f != -1) mk[f][s][3] = 1;
					f = i;
					s = j;
				}
			}
		}
		REP(j,0,c){
			f = -1;
			RREP(i,0,r){
				if (dir[i][j] >= 0){
					if (f != -1) mk[f][s][0] = 1;
					f = i;
					s = j;
				}
			}
		}
		flg = 0;
		cnt = 0;
		REP(i,0,r) REP(j,0,c){
			if (dir[i][j] == -1) continue;
//			cout << "Checking (" << i << "," << j << ")";
//			cout << " with dir: " << dir[i][j] << endl;
			if (mk[i][j][dir[i][j]]) continue;
			fnd = 0;
			REP(k,0,4) if (mk[i][j][k]) fnd = 1;
			if (fnd) cnt++;
			else {
//				cout << "Failed at (" << i << "," << j << ")" << endl;
				flg = 1;
				break;
			}
			if (flg) break;
		}
		printf("Case #%d: ", casenum+1);
		if (!flg) printf("%d\n", cnt);
		else printf("IMPOSSIBLE\n");
//		cout << endl << endl;
	} 
	return 0;
}

