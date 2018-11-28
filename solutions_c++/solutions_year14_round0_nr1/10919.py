#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime> 
using namespace std;

int main() {
	int t; cin>>t;
	for (int c=1; c<=t; c++) {
		int ret=0;

		int a,b; cin>>a;
		int x[4][4], y[4][4];
		for (int i=0; i<4; i++) for (int j=0; j<4; j++) cin>>x[i][j];

		cin>>b;
		for (int i=0; i<4; i++) for (int j=0; j<4; j++) cin>>y[i][j];

		map<int,int> mp;
		for (int i=0; i<4; i++) {
//			cout << x[a-1][i] << " " << y[i][b-1] << endl;

			mp[x[a-1][i]]++;
			mp[y[b-1][i]]++;
		}

		set<int> st;
		for (map<int,int>::iterator it=mp.begin(); it!=mp.end(); it++)
			if((*it).second==2) {
				int cur=(*it).first;
				st.insert(cur);
				ret=cur;
			}
	
		int sz=st.size();

		cout << "Case #" << c << ": ";
		if(sz>1) cout << "Bad magician!" << endl;
		else if(!sz) cout << "Volunteer cheated!" << endl;
		else cout << ret << endl;
	}
	return 0;
}
