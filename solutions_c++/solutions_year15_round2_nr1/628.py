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

LL REV(LL num) {
	LL ret = 0;
	while(num > 0) {
		ret = ret * 10 + num % 10;
		num /= 10;
	}
	return ret;
}

LL go(LL at, LL to) {
	cerr<<at<<"\n";
	int dig = 0;
	LL tmp = at, lpow = 1;
	while (tmp > 0) {
		dig++;
		tmp /= 10;
		lpow *= 10;
	} lpow /= 10;
	tmp = to; LL topow = 1;
	while (tmp > 0) {
		tmp /= 10;
		topow *= 10;
	} topow /= 10;
	// cout<<at<<" "<<lpow<<" "<<topow<<" "<<topow - lpow<<"\n";
	if (lpow < topow) {
		if (at == 1) return go(lpow * 10, to) + 9;
		else {
			int d1 = (dig + 1)/2;
			int d2 = dig - d1;
			LL p1 = 1, p2 = 1;
			REP(i, 0, d1) p1 *= 10;
			REP(i, 0, d2) p2 *= 10;
			return go(lpow * 10, to) + (p1-1) + p2;
		}
	} else {
		LL r1 = to - at;
		while (lpow > 0) {
			LL f1 = to / lpow;
			LL s1 = to % lpow;
			// cout<<f1<<" "<<s1<<" "<<lpow<<"\n";
			if (s1 >= 1)
				r1 = min(r1, REV(f1) + 1 + s1 - 1);
			else {
				f1 = f1 - 1;
				s1 = lpow;
				r1 = min(r1, REV(f1) + 1 + s1 - 1);
			}
			lpow /= 10;
		}
		return r1;
	}
	return to - at;
}

int main() {
  clock_t startTime = clock();
  ios_base::sync_with_stdio(false);

  int test; cin>>test;
  for (int t = 1; t <= test; t++) {
  	cout<<"Case #"<<t<<": ";
  	LL n;
  	cin>>n;
  	cout<<go(1, n) + 1<<"\n";
  }

  clock_t endTime = clock();
  cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
  return 0;
}