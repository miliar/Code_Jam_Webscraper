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

int War(vector<double> &a, vector<double> b){
	int n = a.size();
	int res = 0;
	for(int i = 0; i < n; i++){
		int p = -1;
		for(int j = 0; j <= n; j++){
			if(j==n){
				b[p] = -2.0;
				res++;
			}
			else if(a[i]<b[j]){
				b[j] = -2.0;
				break;
			}else if(p < 0 && b[j]>0.0){
				p = j;
			}
		}
	}
	return res;

}

bool check(vector<double> &a, vector<double> &b, int c){
	int n = a.size();
	for(int i = 0; i < c; i++){
		if(a[n-c+i]<b[i]) return false;
	}
	return true;
}


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int n;
		cin>>n;
		vector<double> a(n),b(n);
		for(int i = 0; i < n; i++){
			cin>>a[i];
		}
		for(int i = 0; i < n; i++){
			cin>>b[i];
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		int res2 = War(a,b);
		int lb = res2, ub = n+1;
		while(ub-lb>1){
			int md = (lb+ub)/2;
			if(check(a,b,md)) lb = md;
			else ub = md;
		}
		printf("Case #%d: %d %d\n", Case, lb, res2);
	}
	return 0;
}

