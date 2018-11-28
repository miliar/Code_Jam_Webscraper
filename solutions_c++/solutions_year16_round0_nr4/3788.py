/*
 * p4.cpp
 *
 *  Created on: 10 Apr 2016
 *      Author: Clem
 */
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <set>
#include <queue>
#include <climits>
#include <list>
#include <utility>
#include <cstdio>

using namespace std;

int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, K, C, S;
	cin>>T;

	for (int i = 1; i <= T; ++i) {
		cin>>K>>C>>S;
		cout<<"Case #"<<i<<":";

		for (int j = 1; j <= S; ++j) {
			cout<<' '<<j;
		}
		cout<<endl;
	}

	return 0;
}



