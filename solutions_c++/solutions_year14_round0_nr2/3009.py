#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#define REP(i, a, b) for ( int i = int(a); i <= int(b); i++ )
#define pb push_back
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define DFS_WHITE -1
#define DFS_BLACK 1
#define MAXN 1000
using namespace std;

int T;
double C, F, X, N, F_old, n1, n2, n3;

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		F_old = 2.0;		
		N = 0.0;
		printf("Case #%d: ", t);

		if(X <= C) {
			N = X/F_old;
		} else {
			while(true) {
				n1 = X/F_old;
				n2 = C/F_old;
				n3 = X/(F_old + F);
				if((N+n1) <= (N+n2+n3)) {
					N += n1;
					break;
				}
				N += n2;
				F_old += F;
			}
		}

		printf("%0.7lf\n", N);
	}
    return 0;
}
