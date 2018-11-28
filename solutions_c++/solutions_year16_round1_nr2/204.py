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

#define N 2510
int a[N];

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int n;
		cin>>n;
		memset(a, 0, sizeof(a));
		for(int i = 0; i < 2*n-1; i++){
			for(int j = 0; j < n; j++){
				int c;
				cin>>c;
				a[c]++;
			}
		}
		vector<int> res;
		res.reserve(n);
		for(int i = 0; i < N; i++){
			if(a[i]%2) res.push_back(i);
		}
		printf("Case #%d:", Case);
		for(int i = 0; i < n; i++) printf(" %d", res[i]);
		puts("");
	}
	return 0;
}

