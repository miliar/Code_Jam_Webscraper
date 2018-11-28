#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <queue>
#include <limits.h>
using namespace std;

void decode(string &s, int &a, int &b) {
	char prev = s[0];
	a= b = 0;
	for (size_t i = 1; i < s.length(); i++) {
		if (s[i] == prev)
			continue;
		if (prev == '-') {
			a++;
		} else {
			b++;
		}
		prev = s[i];
	}
	if(prev == '-')a++;
}

int dp[109][109];
int f(int a,int b){
	if(a == 0 && b == 0)return 0;
	if(dp[a][b]==0)dp[a][b] = f(b,a-1) + 1;
	return dp[a][b];
}

int main() {
	int t, a, b;
	cin >> t;
	string s;
	memset(dp,0,sizeof(dp));
	for (int i = 1; i <= t; i++) {
		cin >> s;
		decode(s,a,b);
		cout <<"Case #"<<i<<": "<< f(a,b) << endl;
	}

}

//Powered by [KawigiEdit] 2.0!
