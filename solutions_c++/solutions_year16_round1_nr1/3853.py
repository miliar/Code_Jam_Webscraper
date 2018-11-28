#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>
#include <memory.h>
using namespace std;
typedef long long ll;
int t;
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		string s,r;
		cin >> s;
		r += s[0];
		for (int i = 1; i < s.size(); ++i){
			if (s[i] >= r[0])
				r = s[i] + r;
			else r += s[i];
		}
		printf("Case #%d: ", k);
		cout << r << endl;
	}
}