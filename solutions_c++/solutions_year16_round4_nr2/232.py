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

double solve(vector<double> &d, int a, int b, int n){
	vector<double> c(n+2, 0.0);
	c[0] = 1.0;
	for(int i = 0; i < d.size(); i++){
		if(a<=i&&i<b) continue;
		vector<double> c2(c);
		c = vector<double>(n+2, 0.0);
		for(int j = 0; j <= n; j++){
			c[j] += c2[j]*(1-d[i]);
			c[j+1] += c2[j]*d[i];
		}
	}
	return c[n];
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int n, m;
		cin>>n>>m;
		vector<double> d(n);
		for(int i = 0; i < n; i++) cin>>d[i];
		sort(d.begin(), d.end());
		double res = 0.0;
		for(int i = 0; i <= m; i++){
			double r = solve(d, i, n-m+i, m/2);
			res = max(res, r);
		}
		printf("Case #%d: %.9lf\n", Case, res);
	}
	return 0;
}

