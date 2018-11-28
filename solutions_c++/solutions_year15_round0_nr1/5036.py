#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<algorithm>
#include<vector>
#include<queue>
#include<list>
#include<string>
#include<set>
#include<map>
#include<iomanip>
#include<sstream>
#include<functional>
#include<climits>
#define eps 1e-9
const int mod = 1000000007;
using namespace std;

int t, smax, ret, ss[1005];
char s[1005];
int main() {
  freopen("A-large.in", "r", stdin);
  freopen("problem1Large.txt", "w", stdout);
  scanf("%d", &t);
  for (int test = 1; test <= t; ++test) {
    ret = 0;
    scanf("%d %s", &smax, s);
    for (int i = 0; i <= smax; ++i) {
	ss[i] = s[i] - '0';
    }
    for (int i = 1; i <= smax; ++i) {
	int up = 0;
	for (int j = 0; j < i; ++j) {
	  up += ss[j];
	}
	if (up < i) {
	  ss[0] += (i - up);
	  ret += (i - up);
	}
    }
    printf("Case #%d: %d\n", test, ret);
  }
  return 0;
}