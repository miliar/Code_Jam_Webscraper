/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |Author: WiYR
 |Created Time.: 2014/4/12 21:20:34
 |File Name: 1A.cpp
 |Description: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
typedef long long ll;
const double eps=1e-7;
const int inf=0x7FFFFFFF;
#define show(x) cout << x << endl
#define rep(i,n) for(int i=0;i<n;i++)
#define mset(a,i) memset(a,i,sizeof(a))
#define PB(i) push_back(i)

using namespace std;
bool hash[20];
int main() {
	int T, r, x;
	scanf("%d", &T);
	rep(cas, T) {
		scanf("%d", &r);
		mset(hash, false);
		for(int i = 1; i <= 4; i ++) 
			for(int j = 1; j <= 4; j ++) {
				scanf("%d", &x);
				if(i == r)
					hash[x] = true;
			}
		scanf("%d", &r);
		int ans = 0, k;
		for(int i = 1; i <= 4; i ++) 
			for(int j = 1; j <= 4; j ++) {
				scanf("%d", &x);
				if(i == r) {
					if(hash[x]) {
						ans ++;
						k = x;
					}
				}
			}			
		printf("Case #%d: ", cas + 1);
		if(ans == 0) {
			puts("Volunteer cheated!");
		} else if(ans == 1) {
			printf("%d\n", k);
		} else {
			puts("Bad magician!");
		}
	}
	return 0;
}

