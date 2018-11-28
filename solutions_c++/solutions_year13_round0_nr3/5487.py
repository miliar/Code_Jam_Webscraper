/*
 this code was written by Zanaty
 problem kind:
 */
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<set> 
#include<cmath>
#include<fstream>
#include<memory.h>
#include<map>
#include<sstream>
#include<climits>
#include<numeric>/*
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
*/
using namespace std;

#define rep(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define reps(i,x,n) for((i)=(x);(i)<(int)(n);(i)++)
#define repi(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define SZ(v) (int)v.size()
#define LEN(s) (int)s.length()
#define mp(x,y) make_pair(x,y)
#define ll long long
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define vi vector<int>
#define vvi vector<vi>

#define INF (int)10e8
#define MAX (int) 1000

bool isplain(int x) {
	string s = "", s2;
	while (x) {
		s += ((x % 10) + '0');
		x /= 10;
	}
	s2 = s;
	reverse(all(s2));
	return s == s2;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.txt", "r", stdin);
	freopen("out.txt","w",stdout);
#endif

	int test, tt = 1;
//	cout << isplain(3) << endl;
	scanf("%d", &test);
	while (test--) {
		int a, b;
		scanf("%d%d", &a, &b);
		int res = 0;
		for (int i = 1; i * i <= b; i++) {
			if (i * i >= a) {
				if (isplain(i) && isplain(i * i))
					res++;
			}
		}
		printf("Case #%d: %d\n", tt++, res);
	}

	return 0;
}
