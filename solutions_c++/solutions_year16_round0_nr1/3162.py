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
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	////////////////////////////

	int n;
	while (cin >> n) {
		int cnt = 1;
		while (n--) {
			int t;
			cin >> t;
			set<int>st;
			int mem=-1;
			for (int i = 1; i <= 303; i++) {
				int here = i*t;
				while (1) {
					int p = here % 10;
					st.insert(p);

					int q = here / 10;
					here = q;
					if (q == 0) break;
				}
				if (st.size() == 10) {
					mem = i;
					break;
				}
			}
			if (mem != -1)
				cout << "Case #" << cnt++ << ": " << mem*t << endl;
			else
				cout << "Case #" << cnt++ << ": " << "INSOMNIA" << endl;





		}
	}


	

	////////////////////////////
	//system("pause");
	return 0;
}

//END
