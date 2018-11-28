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


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int n;
		cin>>n;
		vector<int> d(n);
		for(int i = 0; i < n; i++) cin>>d[i];
		int res1 = 0;
		for(int i = 0; i < n-1; i++) res1 += max(0, d[i]-d[i+1]);
		int df = 0;
		for(int i = 0; i < n-1; i++) df = max(df, d[i]-d[i+1]);
		int res2 = 0;
		bool st = false;
		for(int i = n-2; i >= 0; i--){
			res2 += min(df, d[i]);
		}
		printf("Case #%d: %d %d\n", Case, res1, res2);
	}
	return 0;
}

