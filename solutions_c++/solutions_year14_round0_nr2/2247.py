#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

int main() {
	int T;
	cin >> T;
	for (int nowCase = 1; nowCase <= T; ++nowCase) {
		double c, f, x;
		cin >> c >> f >> x;
		double currentRate = 2.0;
		double currentTime = 0.0;
		double answer = 1e50;
		for (int i = 0; i <= 100000; ++i) {
			answer = min(answer, currentTime + x / currentRate);
			currentTime += c / currentRate;
			currentRate += f;
		}

		printf("Case #%d: %.10f\n", nowCase, answer);
	}

	return 0;
}