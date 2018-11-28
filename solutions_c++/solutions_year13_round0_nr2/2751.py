#include <iostream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define pb push_back
#define FOREACH(x,y) for(typeof(y.begin()) x = y.begin() ; x != y.end() ; x++)

#define LL long long

LL MOD = 1000000007;

int arr[102][102];

bool check(int m, int n, int r, int c, int num) {
	bool f1,f2;
	f1 = f2 = true;
	for(int i = 1 ; i < n ; i++) {
		if(arr[r][i-1] != arr[r][i]) {
			f1 = false;
		}
	}
	for(int i = 1 ; i < m ; i++) {
		if(arr[i-1][c] != arr[i][c]) {
			f2 = false;
		}
	}
	return f1 || f2;
}

void setValue(int m, int n, int r, int c, int num) {
	for(int i = 0 ; i < n ; i++) {
		arr[r][i] = num;
	}
	for(int i = 0 ; i < m ; i++) {
		arr[i][c] = num;
	}
}

bool find(int m, int n, int a, int b) {
	for(int i = 0 ; i < m ; i++) {
		for(int j = 0 ; j < n ; j++) {
			if(arr[i][j] == a) {
				if(!check(m,n,i,j,b)) {
					return false;
				}
			}
		}
	}
	for(int i = 0 ; i < m ; i++) {
		for(int j = 0 ; j < n ; j++) {
			if(arr[i][j] == a) {
				setValue(m,n,i,j,b);
			}
		}
	}
	return true;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	cin >> tc;
	for(int t = 1 ; t <= tc ; t++) {
		int m,n;
		bool flag = true;
		vector <int> v;
		cin >> m >> n;
		for(int i = 0 ; i < m ; i++) {
			for(int j = 0 ; j < n ; j++) {
				cin >> arr[i][j];
				v.push_back(arr[i][j]);
			}
		}
		sort(v.begin(), v.end());
		vector <int>::iterator it = unique(v.begin(),v.end());
		v.resize(it - v.begin());
		for(int i = 0 ; i < (int)v.size() - 1 ; i++) {
			if(!find(m,n,v[i],v[i+1])) {
				flag = false;
				break;
			}
		}
		if(flag) {
			cout << "Case #" << t << ": YES" << endl;
		} else {
			cout << "Case #" << t << ": NO" << endl;
		}
	}
	return (0);
}