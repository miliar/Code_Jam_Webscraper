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

bool isPal (LL A){
	vector <int> Q;
	while (A){
		Q.push_back(A%10); A/=10;
	}
	for (int i=0, j=(int)Q.size()-1; i<=j; i++, j--) if (Q[i]!=Q[j])
		return false;
	return true;
}

int main(){
	vector <LL> Q;
	for (LL i=1; i<10000000; i++) if (isPal(i) && isPal(i*i))
		Q.push_back(i*i);
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		LL a, b; cin >> a >> b;
		int ans = 0;
		for (int i=0; i<(int)Q.size(); i++) if (Q[i]>=a && Q[i]<=b)
			ans++;
		cout << "Case #" << o << ": " << ans << endl; 
	}
	return 0;
}
