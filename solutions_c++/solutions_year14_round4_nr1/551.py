#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;
#define MAX_N 10000

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int N,X;
		cin>>N>>X;
		vector<int> S(N);
		for(int i = 0; i < N; i++){
			cin>>S[i];
		}
		sort(S.rbegin(),S.rend());
		int res = 0;
		for(int i = 0; i < N; i++){
			if(S[i]+S[N-1]<=X){
				N--;
				res++;
			}else res++;
		}
		printf("Case #%d: %d\n", Case, res);
	}
	return 0;
}

