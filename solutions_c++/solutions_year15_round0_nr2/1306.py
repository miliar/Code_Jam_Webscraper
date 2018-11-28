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
const int INF = 1<<29;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;
#define N 1100
int a[N];

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		memset(a, 0, sizeof(a));
		int n;
		cin>>n;
		int m = 1;
		for(int i = 0; i < n; i++){
			int b;
			cin>>b;
			a[b]++;
			m = max(m, b);
		}
		ll res = m;
		for(int i = 2; i <= m; i++){
			ll r = i;
			for(int j = i+1; j <= m; j++){
				r += (j-1)/i*a[j];
			}
			res = min(res, r);
		}
		printf("Case #%d: %ld\n", Case, res);
	}
	return 0;
}

