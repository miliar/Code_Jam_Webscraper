#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

int main(){
	int T;
	cin >> T;
	REP(testCase, T){
		int N, S;
		cin >> N >> S;
		vector<int> X(N);
		REP(i, N)cin >> X[i];
		sort(ALL(X));
		reverse(ALL(X));
		vector<bool> used(N, false);
		int res = 0;
		REP(i, N){
			if (!used[i]){
				used[i] = true;
				res++;
				for (int j = i + 1; j < N; j++){
					if (!used[j] && X[i] + X[j] <= S){
						used[j] = true;
						break;
					}
				}
			}
		}
		cout << "Case #" << testCase + 1 << ": " << res << endl;
	}
	return 0;
}