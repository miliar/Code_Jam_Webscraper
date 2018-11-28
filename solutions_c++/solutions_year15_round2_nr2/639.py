#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

#define X 20
int rooms[X][X];
int r, c, n;

int score() {
	int ret = 0;
	REP(i, 0, r) {
		REP(j, 0, c) {
			if (rooms[i][j] && rooms[i][j+1]) {
				ret++;
			}
			if (rooms[i][j] && rooms[i+1][j]) {
				ret++;
			}
		}
	}
	return ret;
}

int go(int at, int left) {
	if (left == 0) {
		return score();
	}
	if (at >= r * c) return (1<<29);
	int ret = (1<<29);
	int a = at / c;
	int b = at % c;
	// place
	rooms[a][b] = 1;
	ret = min(ret, go(at + 1, left - 1));
	// don't place
	rooms[a][b] = 0;
	ret = min(ret, go(at + 1, left));
	return ret;
}

int main() {
  clock_t startTime = clock();
  ios_base::sync_with_stdio(false);

  int test; cin>>test;
  for (int t = 1; t <= test; t++) {
  	cin>>r>>c>>n;
  	cout<<"Case #"<<t<<": ";
  	cout<<go(0, n)<<"\n";
  }

  clock_t endTime = clock();
  cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
  return 0;
}