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
		int N;
		cin >> N;
		vector<int> orig(N);
		REP(i, N)cin >> orig[i];
		vector<int> perm = orig;
		int mx = *max_element(ALL(orig));
		int res = 1000000000;
		sort(ALL(perm));
		do{
			int mxIdx = 0;
			REP(i, N)if (perm[i] == mx)mxIdx = i;
			vector<int> test = perm;
			sort(test.begin(), test.begin() + mxIdx);
			sort(test.begin() +mxIdx + 1, test.end());
			reverse(test.begin() + mxIdx + 1, test.end());
			if (test == perm){
				vector<int> tmp = orig;
				int s = 0;
				//REP(i, N)cout << test[i] << " ";
				//cout << endl;
				REP(i, N){
					for (int j = N-1; j > i; j--){
						if (perm[i] == tmp[j]){
							swap(tmp[j], tmp[j - 1]);
							s++;
						}
					}
				}
				//if (tmp != perm)cout << "!" << endl;
				res = min(res, s);
			}
			

		} while (next_permutation(ALL(perm)));
		cout << "Case #" << testCase + 1 << ": " << res << endl;
	}
	return 0;
}