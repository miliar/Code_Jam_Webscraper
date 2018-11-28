#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <utility>
#include <set>
#include <functional>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <ctime>
using namespace std;

#define FOR(_i,_n) for(int (_i)=0;(_i)<(_n);(_i)++)
#define iss istringstream
#define oss ostringstream
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pi 3.141592653589793
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int,int> Pair;

int dx[8] = { 0, 1,-1, 0, 1, 1,-1,-1};
int dy[8] = { 1, 0, 0,-1,-1, 1, 1,-1};
int hx[8] = {-2,-2,-1,-1, 1, 1, 2, 2};
int hy[8] = {-1, 1,-2, 2,-2, 2,-1, 1};

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int t=1;t<=T;t++) {
		int N, M, a[111][111];
		cin >> N >> M;
		FOR(i, N) FOR(j, M) cin >> a[i][j];
		
		bool b = true;
		
		FOR(i, N) {
			FOR(j, M) {
				int cur = a[i][j];
				bool ver = false;
				bool hor = false;
				FOR(ii, N) {
					if(a[ii][j] > cur) {
						ver = true;
						break;
					}
				}
				FOR(jj, M) {
					if(a[i][jj] > cur) {
						hor = true;
						break;
					}
				}
				if(ver && hor) {
					b = false;
					break;
				}
			}
			if(b == false) break;
		}
		
		if(b) {
			cout << "Case #" << t << ": YES" << endl;
		} else {
			cout << "Case #" << t << ": NO" << endl;
		}
	}
	
	return 0;
}
