#include <iostream>
#include <limits.h>
#include <utility>
#include <fstream>
#include <string>
#include <string.h>
#include <functional>
#include <queue>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>

typedef long long ll;
using namespace std;

int main(){
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

#endif
	int t;
	int caseNumber = 0;
	cin >> t;
	while (t--){
		int m;
		ll ans = 0;
		ll sum = 0;
		string str;
		cin >> m;
		cin >> str;
		for (int i = 0; i <=m; i++){
			if (sum >= i)
				sum += str[i] - '0';
			else{
				ans += i - sum;
				sum = i + str[i] -'0';
			}
		}
		printf("Case #%d: %lld\n", ++caseNumber, ans);
	}
}