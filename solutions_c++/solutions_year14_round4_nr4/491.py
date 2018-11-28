#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;

int n,m;

int check2(vector<string>& s){
	set<string> st;
	st.insert("");
	for(int i = 0; i < s.size(); i++){
		for(int j = 0; j < s[i].size(); j++){
			for(int k = 1; j+k <= s[i].size(); k++){
				st.insert(s[i].substr(j,k));
			}
			break;
		}
	}
	/*for(set<string>::iterator it = st.begin(); it!=st.end(); ++it){
		cout<<*it<<endl;
	}*/
	return st.size();
}

int check(vector<vector<string> >& t){
	int res = 0;
	for(int i = 0; i < m; i++){
		res += check2(t[i]);
	}
	return res;
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		cin>>n>>m;
		vector<string> s(n);
		for(int i = 0; i < n; i++){
			cin>>s[i];
		}
		int c = 0;
		map<int,int> d;
		while(true){
			vector<vector<string> > t(m);
			int c2 = c++;
			for(int i = 0; i < n-1; i++){
				t[c2%m].push_back(s[i]);
				c2 /= m;
			}
			if(c2) break;
			t[0].push_back(s[n-1]);
			bool flag = true;
			for(int i = 0; i < m; i++){
				if(t[i].empty()){
					flag = false;
					break;
				}
			}
			if(!flag) continue;
			++d[check(t)];
		}
		int res = 0;
		for(map<int,int>::iterator it = d.begin(); it!=d.end(); ++it){
			res = max(res,(*it).first);
		}
		int res2 = d[res]*m;
		printf("Case #%d: %d %d\n", Case, res, res2);
	}
	return 0;
}

