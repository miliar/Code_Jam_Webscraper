#include <cstdio>
#include <fstream>
#include <iostream>

#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <vector>
#include <bitset>
#include <string>
#include <cstring>
#include <algorithm>

#include <ctime>
#include <cstdlib>
#include <cassert>

#define pb push_back
#define mp make_pair
#define sz(A) (int) (A).size()

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define eputs(A) fputs((A), stderr)

#define sqr(A) ((A) * (A))
#define x first
#define y second
  
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;

const int N = (int) 1e6;

int t, we, n, a[N];
vector <int> have;

int main () 
{
    #ifdef DEBUG
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    #endif

    scanf("%d", &t);
    for (int test = 0; test < t; test++) {
    	have.clear();
    	scanf("%d%d", &we, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", a + i);
		sort(a, a + n);
		for (int i = 0; i < n; i++) 
			if (a[i] < we)
				we += a[i];
			else
				have.push_back(a[i]);

		sort(have.begin(), have.end());
		int res = sz(have);
		for (int i = 1, j = 0; we > 1 && j < sz(have); i++) {
			we += we - 1;
			while (j < sz(have) && have[j] < we)
				we += have[j++];
			
			res = min(res, i + sz(have) - j);						
		}										

		printf("Case #%d: %d\n", test + 1, res);
	}
    
    return 0; 
}

