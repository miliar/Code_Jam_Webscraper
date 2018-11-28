/*
 *	Category: CodeJam
 *  Problem: A.MagicTrick.cpp
 *  Status: 
 * 	Date: Apr 12, 2014
 * 	Start: 1:43:58 AM	End: 		Duration: 
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

int main() {
#ifndef ONLINE_JUDGE 
	freopen("test.txt", "rt", stdin);
	freopen("o.txt", "wt", stdout);
#endif
	string fake[] = {"Volunteer cheated!\n", "Bad magician!\n"};
	int G1, G2, t = 0, tc, temp;
	set<int> match;
	cin >> tc;
	while(tc--){
		match.clear();
		cout << "Case #" << ++t << ": ";
		cin >> G1;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++){
				cin >> temp;
				if(i == G1)
					match.insert(temp);
			}
		cin >> G2;
		int cnt = 0, M;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++){
				cin >> temp;
				if(i == G2)
					if(match.find(temp) != match.end()){
						cnt++;
						M = temp;
					}
			}
		if(cnt == 0){
			cout << fake[0];
		}
		else if(cnt == 1){
			cout << M << "\n";
		}
		else
			cout << fake[1];
	}
	return 0;
}
