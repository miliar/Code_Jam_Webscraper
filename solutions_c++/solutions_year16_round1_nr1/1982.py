#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#define  _SCL_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstring>
#include <queue>
#include <stack>
#include <math.h>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <iostream> 
#include<map>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
using namespace std;
#define REP(a,b) for(long long a = 0;a < b;++a)
int main() {
	int t;
	cin >> t;
	for (int i = 0;i < t;++i) {
		string S;
		cin >> S;
		cout << "Case #" << i + 1 << ": ";
		string ans;
		ans.push_back(S[0]);
		for (int q = 1;q < S.length();++q) {
			if (S[q] >= ans[0]) {
				string hoge;
				hoge.push_back(S[q]);
				ans.insert(0, hoge);
			}
			else {
				ans.push_back(S[q]);
			}
		ok:;
		}
		cout << ans << endl;
	}
}
//thank you for reading!