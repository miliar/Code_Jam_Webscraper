//#include<bits/stdc++.h>
#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<deque>
#include<cmath>
#include<climits>
#include<list>
#include<utility>
#include<memory>
#include<cstddef>
#include<iterator>
#include<iomanip>
using namespace std;
typedef long long LL;
typedef long double LD;
const double pi = acos(-1.0);
///////////////////////////////







///////////////////////////////
int main(int argc, char**argv) {
	//ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	////////////////////////////

	int n;
	cin >> n;
	for (int k = 1; k <= n; k++) {
		char st[107];
		scanf("%s", st);
		int len = strlen(st);
		int cnt = 0;
		for (int i = 0; i <= len-1; i++) {
			if (st[i] == '+') {
				if (st[i + 1] == '-') cnt++;
			}
			if (st[i] == '-') {
				cnt++;
				if ( st[i + 1] == '-') {
					cnt--;
				}
				//if (st[i + 1] == '+') {
				//	cnt++;
				//}
			}
		}
		cout << "Case #" << k << ": " << cnt << endl;
	}

	

	////////////////////////////
	//system("pause");
	return 0;
}

//END
