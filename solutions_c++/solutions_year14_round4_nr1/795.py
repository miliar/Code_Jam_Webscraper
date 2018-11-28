
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdlib>
#include <set>
#include <string>
#include <vector>
#include <cmath>
#define MAX 100005
const double EPS = 1e-9;
int cmp( double a, double b = 0){
	return a + EPS < b ? -1 : a - EPS > b ? 1 : 0;
}

typedef long long Int;
using namespace std;
//vector<int> g[MAX];
//int usd[MAX];
int freq[10005],a[10005];
void solve(){
	int n , m;
	scanf("%d%d",&n,&m);
	memset( freq, 0, sizeof freq);
	for( int i = 0; i < n; i++) scanf("%d",a+i), freq[a[i]]++;
	int res = 0;
	for( int i = 1000; i>= 1; i--){
		while( freq[i] ){
			freq[i]--;
			bool cagao = false;
			for( int j = m - i; j >= 1; j--){
				if ( freq[j] ) {
					freq[j]--;
					break;
				}
			}
			res++;
		}
	}
	printf("%d\n",res);
}
int main(){

	int runs;
	scanf("%d",&runs);
	for( int r = 1; r <= runs; r++){
		printf("Case #%d: ",r);
		solve();
	}

	return 0;
}
