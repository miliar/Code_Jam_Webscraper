/*
 *	Category: CodeJam
 *  Problem: D.DeceitfulWar.cpp
 *  Status: 
 * 	Date: Apr 12, 2014
 * 	Start: 6:59:31 AM	End: 		Duration: 
 * 	Author: Hossam Yousef
 */

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

#define OO (int)1e9
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define mems(s,v) memset(s,v,sizeof(s))

deque<int> n, nn, kk, k;

int main() {
	freopen("test.txt", "rt", stdin);
	freopen("o.txt", "wt", stdout);
	int t = 0, tc, N;
	double temp;
	cin >> tc;
	while(tc--){
		n.clear();
		nn.clear();
		k.clear();
		kk.clear();
		cout << "Case #" << ++t << ": ";
		cin >> N;
		for(int i = 0; i < N; i++){
			cin >> temp;
			n.push_back((temp+1e-6)*100000);
		}
		for(int i = 0; i < N; i++){
			cin >> temp;
			k.push_back((temp + 1e-6)*100000);
		}
		sort(all(n));
		sort(all(k));
		nn = n;
		kk = k;
		int cntN = 0, cntK = 0;
		while(sz(nn)){
			if(nn.front() < kk.front()){
				nn.pop_front();
				kk.pop_back();
			}else{
				nn.pop_front();
				kk.pop_front();
				cntK++;
			}
		}
		cout << cntK << " ";
		while(sz(n)){
			if(n.back() > k.back()){
				cntN++;
				n.pop_back();
				k.pop_front();
			}else{
				n.pop_back();
				k.pop_back();
			}
		}
		cout << cntN << endl;
	}
	
	return 0;
}
