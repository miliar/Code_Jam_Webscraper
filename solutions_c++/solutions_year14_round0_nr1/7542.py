/*
 Author : OmarEl-Mohandes
 PROG   : A
 LANG   : C++
 */
#include <map>
#include <string>
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
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)m;i++)
#define REP(i,k,m) for(int i=k;i<(int)m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)
int main() {
	freopen("test.in", "rt", stdin);
	freopen("A.out" , "wt" , stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		set<int> res;
		int r = 0, y = -1 , n;
		for (int j = 0; j < 2; j++) {
			scanf("%d", &n);
			for (int i = 0; i < 4; i++) {
				vi tem(4);
				for (int j = 0; j < 4; j++)
					scanf("%d", &tem[j]);
				if (i + 1 == n)
					for (int i = 0; i < 4; i++) {
						r += !res.insert(tem[i]).second;
						if (r > 0 && y == -1)
							y = tem[i];
					}
			}
		}
		printf("Case #%d: ", i + 1);
		if (r == 1)
			printf("%d\n", y);
		else if (r > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}

	return 0;
}

