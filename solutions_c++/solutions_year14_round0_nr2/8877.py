#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const double inf = 10e10;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

int solution(int nTest) {
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	double res = inf;
	double rate = 2;
	double commonTime = 0;
	For(i, 0, x + 4) {
		double time = x / rate;
		res = min(res, commonTime + time);
		time = c / rate;
		commonTime += time;
		rate += f;
	}

	printf("%.7lf\n", res);


	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
