#include <iostream>
#include <string>
#include <sstream>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <list>
#include <bitset>
#include <numeric>
using namespace std;

#define ll long long
#define ull unsigned long long
#define INF 1e9
#define MOD 1000000007
#define getcx getchar_unlocked
#define putcx putchar_unlocked
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64

int main() {
	ios_base::sync_with_stdio(0);

	int T, d;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> d;
		vector<int> v(d);
		for (int i = 0; i < d; i++) {
			cin >> v[i];
		}
		int mn_time = *max_element(v.begin(), v.end());
		for(int i=1;i<mn_time;i++){
			int time = i;
			for(int j =0;j<v.size();j++){
				if(v[j]>i){
					time = time + v[j]/i;
					if(v[j]%i==0)
						time--;
				}
			}
			mn_time = min(mn_time,time);
		}
		cout << "Case #" << t << ": " << mn_time << endl;
	}

	return 0;
}