/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <bitset>
#include <iomanip>
#include <utility>

using namespace std;

typedef long long LL;
typedef complex<double> point;
typedef long double ldb;
typedef pair<int,int> pii;

int n,me;
int a[1<<20];

inline void main2(){
	cin >> me >> n;
	for (int i=0; i<n; i++)
		cin >> a[i];
	sort(a, a+n);
	if (me==1){
		cout << n << endl;
		return;
	}
	LL cur = me;
	int ret = n, add = 0;
	for (int i=0; i<n; i++){
		while (cur<=a[i]){
			cur = 2*cur-1;
			add++;
		}
		cur+=a[i];
		ret = min(ret, add + n-i-1);
	}
	cout << ret << endl;
	return;
}

int main(){
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
