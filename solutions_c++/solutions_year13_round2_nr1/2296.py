/*
 * =====================================================================================
 *
 *       Filename:  tic-tac.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 13 April 2013 10:08:01  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:   (), 
 *        Company:  
 *
 * =====================================================================================
 */
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
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

typedef long long ll;

int A, N;
vector<int> v;
int cache[10000][100];
int cal(int cur, int i){
	//cout << "cal " << cur << ", i=" << i << endl;
	if(i == N) return 0;
	if(cache[cur][i] != -1) return cache[cur][i];
	int res;
	if(cur > v[i]) res = cal(cur+v[i], i+1);
	else if (cur > 1){
		int r1 = cal(cur + cur-1, i) + 1;
		int r2 = cal(cur, i+1) + 1;
		res = min(r1, r2);
	} else if(cur == 1){
		res = cal(cur, i+1) + 1;
	}
	return cache[cur][i] = res;
}
int main(){
	ll T;
	cin >> T;
	for(int test=0;test<T;test++){
		cin >> A >> N;
		v.clear();
		memset(cache, -1, sizeof(cache));
		for(int i=0;i<N;i++){ int t; cin >> t; v.push_back(t); }
		int res = 0;
		sort(v.begin(), v.end());
		res = cal(A, 0);
		cout << "Case #" << test+1 << ": " << res << endl;
	}
	return 0;
}
