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
#define N 1010
int n;
int b[N];
int step[N];
int two[N];

int cyc(int u){
	memset(step, 0, sizeof(step));
	int v = u;
	for(int i = 1; i < n+2; i++){
		if(step[v]){
			int res = i-step[v];
			if(res==2){
				two[v] = max(two[v], i-2);
			}
			//cerr<<u<<": "<<i<<" "<<step[v]<<" "<<v<<endl;
			return res;
		}
		step[v] = i;
		v = b[v];
	}
	return 0;
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		memset(two, 0, sizeof(two));
		cin>>n;
		for(int i = 0; i < n; i++) cin>>b[i];
		for(int i = 0; i < n; i++) b[i]--;
		int res = -1;
		for(int i = 0; i < n; i++) res = max(res, cyc(i));
		int res2 = 0;
		for(int i = 0; i < n; i++) res2 += two[i];
		printf("Case #%d: %d\n", Case, max(res, res2));
	}
	return 0;
}

