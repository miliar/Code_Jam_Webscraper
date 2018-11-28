#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>

#define REP(i, N) for (int i = 0; i < (int)N; i++)
using namespace std;
typedef long long LL;


void solve(int caseCnt) {
  int N, X;
  cin >> N >> X;
  int first = 0, last = N - 1;
  vector<int> S;
  REP(i, N) {
    int s;
    cin >> s;
    S.push_back(s);
  }
  sort(S.begin(), S.end());
  int res = 0;
  while (first <= last) {
    if (S[first] + S[last] <= X) {
      first++, last--;
    } else {
      last--;
    }
    res++;
  }
  printf("Case #%d: %d\n", caseCnt, res);
}


int main(){
	int TestCase;
  cin >> TestCase;
	for(int caseCnt=1; caseCnt <= TestCase; caseCnt++){
		//solve_small(caseCnt);
		solve(caseCnt);
	}
	return 0;
}
