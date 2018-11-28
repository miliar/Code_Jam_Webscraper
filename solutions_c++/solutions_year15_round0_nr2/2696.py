#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("answer.out", "w", stdout);
	int T;
	cin>>T;
	for(int t = 1; t <= T; t++){
		int D,d[1000];
		int ans = 1000;
		cin>>D;
		int tmp = 0;
		for(int i = 0; i < D; i++)
			cin>>d[i];
		for(int ub = 3; ub <= 1000; ub++){
			int base = 0, sm = 0;
			for(int i = 0; i < D; i++){
				int ns = (d[i] - 1) / ub + 1;
				base = max(base, (d[i] - 1) / ns + 1);
				sm += ns - 1;
			}
			ans = min(ans,sm + base);
		}
		
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
