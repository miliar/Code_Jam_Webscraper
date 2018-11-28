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

bool isPalindrome(LL n) {
	char str[102];
	int l = 0;
	while(n > 0) {
		str[l++] = n % 10;
		n = n / 10;
	}
	for(int i = 0 ; i < l ; i++) {
		if(str[i] != str[l-i-1]) {
			return false;
		}
	}
	return true;
}

int binSearch(vector <LL> v, LL n, bool &flag) {
	int lb = 0;
	int ub = (int)v.size() - 1;
	int mid = (lb + ub) / 2;
	while(lb <= ub) {
		int mid = (lb + ub) / 2;
		if(v[mid] <= n) {
			if(mid+1 <= ub) {
				if(v[mid+1] > n) {
					if(v[mid] == n) flag = true;
					return mid;
				} else {
					lb = mid + 1;
				}
			}
			else {
				return mid;
			}
		} else {
			if(mid-1 >= lb) {
				if(v[mid-1] <= n) {
					if(v[mid-1] == n) flag = true;
					return mid - 1;
				} else {
					ub = mid - 1;
				}
			}
			else {
				return mid;
			}
		}
	}
	return mid;
}

void preprocess(vector <LL> &v) {
	for(LL i = 1 ; i < 10000002 ; i++) {
		if(isPalindrome(i) && isPalindrome(i*i)) {
			v.push_back(i*i);
		}
	}
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	cin >> tc;
	vector <LL> v;
	preprocess(v);
	for(int t = 1 ; t <= tc ; t++) {
		LL a, b;
		cin >> a >> b;
		bool flag = false;
		int ans = binSearch(v,b,flag);
		flag = false;
		ans = ans - binSearch(v,a,flag);
		if(flag) ans = ans + 1;
		cout << "Case #" << t << ": " << ans << endl;
	}
	return (0);
}