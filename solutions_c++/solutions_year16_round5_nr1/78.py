#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <numeric>
#include <deque>
#include <utility>
#include <bitset>
#include <iostream>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		int ret = 0;
		string s;
		cin >> s;
		stack<char> stk;
		for(auto &i : s){
			if(!stk.empty() && stk.top() == i){
				stk.pop();
				ret += 10;
			}
			else{
				stk.push(i);
			}
		}
		ret += 5 * (stk.size() / 2);
		printf("Case #%d: %d\n",i, ret);
	}
}