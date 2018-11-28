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
		int n;
		cin >> n;
		vector<double> first(n);
		vector<double> second(n);
		REP(i, n) cin >> first[i];
		REP(i, n) cin >> second[i];
		SORT(first);
		SORT(second);
		int answer2 = 0;
		REP(i, n) {
			if (second[i] > first[answer2]) {
				++answer2;
			}
		}
		int answer1 = 0;
		REP(i, n) {
			if (first[i] > second[answer1]) {
				++answer1;
			} 
		}

		cout << "Case #" << nowCase << ": " << answer1 << " " << n - answer2 << endl;
	}

	return 0;
}