#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;

#define INF (int)1e9
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int) (x).size())
#define iter(x) __typeof(x.begin())
#define REP(i,x) for(iter(x)i=x.begin();i!=x.end();i++)
#define pr(x) printf("Case #%d: %0.7lf\n",Case,x);

int main() {
	
	int TotalCases;
	scanf("%d", &TotalCases);


	for ( int Case = 1; Case <= TotalCases; Case++ ) {
		double C, F, X;
		scanf("%lf%lf%lf",&C, &F, &X);
		double arr[100010];
		double start = 2.0;
		for ( int i = 1; i < 100010; i++ ) {
			arr[i] = arr[i-1] + C/start;
			start += F;
		}
		double mini = 1e9;
		for ( int i = 0; i * C < X; i++ ) {
			double rate = 2.0 + (i*F);
			double ans = arr[i] + (X/rate);
			mini = min ( mini, ans );
		}
		pr(mini);	
	}

	return 0;
}
