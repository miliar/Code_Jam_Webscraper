#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
using namespace std;

#define rep(i,N) for((i) = 0; (i) < (N); (i)++)
#define rab(i,a,b) for((i) = (a); (i) <= (b); (i)++)
#define Fi(N) rep(i,N)
#define Fj(N) rep(j,N)
#define Fk(N) rep(k,N)
#define sz(v) (v).size()
#define all(v) (v).begin(),(v).end()

int main() {
	int T, cs;
	int smax;
	char s[100000];
	int f,i,t;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %s",&smax,s);

		f = 0;
		t = 0;

		rab(i,0,smax) {
			if(s[i] == '0') continue;
			if (t < i) {
				f += (i - t);
				t = i;
			}
			t += s[i] - '0';
		}
		printf("Case #%d: %d\n",cs,f);
	}
	return 0;
}
