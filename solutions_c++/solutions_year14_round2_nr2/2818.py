#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <math.h>

using namespace std;



int T;
int N;

typedef unsigned long long ull;
#define SMALL
//#define LARGE
int main() {
#ifdef SMALL
	freopen("c:\\B.in","rt",stdin);
	freopen("c:\\B.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	scanf("%d", &T);
	ull A, B, K;
	for(int i = 0; i < T; i++)
	{
		scanf("%lld %lld %lld", &A, &B, &K);

		ull count = 0;
		for(int j = 0; j < A; j++)
		{
			for(int k = 0; k < B; k++)
			{
				if((j & k) < K)
					count++;
			}
		}
		printf("Case #%d: %d\n", i+1, count);
	}
	
	return 0;
}
