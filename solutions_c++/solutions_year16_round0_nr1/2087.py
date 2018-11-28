#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

int main() {
	int TEST, N;
	scanf("%d",&TEST);

	FOR(test,TEST) {
		scanf("%d",&N);
		printf("Case #%d: ", (test+1));
		if (N==0) {
			printf("INSOMNIA\n");
		} else {
			int seen = 0;
			int v = 0;
			do {
				v += N;
				for(int x = v; x; x/=10) {
					int d = x%10;
					seen |= (1<<d);
				}
			} while (seen != 1023);

			printf("%d\n",v);
		}
	}
}













