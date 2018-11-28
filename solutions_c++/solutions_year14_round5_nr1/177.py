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

int n,p,q,r,s; 
long long a[1<<20], sum[1<<20];

long long getVal (int a, int b){
	return sum[b+1] - sum[a];
}

long long get (int a, int b){
	if (b < a)
		b = a;
	b = min(b, n-1);
	long long ret = getVal(a,b);
	if (a > 0)
		ret = max(ret, getVal(0, a-1));
	if (b < n-1)
		ret = max(ret, getVal(b+1,n-1));
	return ret;
}

void main2(){
	cin >> n >> p >> q >> r >> s;
	sum[0] = 0;
	for (int i=0; i<n; i++){
		a[i] = (((long long)i * p + q) % r) + s;
		sum[i+1] = sum[i] + a[i];
	}
	long long ans = sum[n];
	for (int i=0; i<n; i++){
		//lef
		int pos = upper_bound(sum+i+1, sum+n+1, 2*sum[i]) - sum;
		ans = min(ans, get(i, pos+1));
		ans = min(ans, get(i, pos));
		ans = min(ans, get(i, pos-1));
		ans = min(ans, get(i, pos-2));
		//mid
		pos = upper_bound(sum+i+1, sum+n+1, sum[i] + max(sum[i], (sum[n]-sum[i])/2)) - sum;
		ans = min(ans, get(i, pos+1));
		ans = min(ans, get(i, pos));
		ans = min(ans, get(i, pos-1));
		//rig
		ans = min(ans, get(i, pos-2)); 
	}
	long double ret = (sum[n] - (long double)ans) / (long double)sum[n];
	cout << fixed << setprecision(12) << ret << endl;
}

int main(){
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
