#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
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
#include <bitset>
#include <iostream>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

string s;
void solve(){
	cin >> s;
	int cnt = 0;
	for(int i=0; i+1<s.size(); i++){
		if(s[i] != s[i+1]){
			reverse(s.begin(), s.begin()+i+1);
			for(int j=0; j<=i; j++){
				s[j] = '-' + '+' - s[j];
			}
			cnt++;
		}
	}
	if(s[0] == '-') cnt++;
	cout << cnt;
}
int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ", i);
		solve();
		puts("");
	}
}