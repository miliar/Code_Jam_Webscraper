#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <utility>
#include <set>
#include <functional>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <ctime>
using namespace std;

#define FOR(_i,_n) for(int (_i)=0;(_i)<(_n);(_i)++)
#define iss istringstream
#define oss ostringstream
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pi 3.141592653589793
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int,int> Pair;

int res = 0;

void f(int idx, int N, int energy, int R, int score, int v[], int E) {
	energy += R;
	if(energy > E) {
		energy = E;
	}
	if(idx == N) {
		res = max(score, res);
	} else {
		for(int e=0;e<=energy;e++) {
			f(idx + 1, N, energy - e, R, score + v[idx] * e, v, E);
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for(int tt=1;tt<=T;tt++) {
		res = 0;
		int E, R, N;
		cin >> E >> R >> N;
		int v[N];
		for(int i=0;i<N;i++) cin >> v[i];
		f(0, N, E, R, 0, v, E);
		cout << "Case #" << tt << ": " << res << endl;
	}
	
	return 0;
}
