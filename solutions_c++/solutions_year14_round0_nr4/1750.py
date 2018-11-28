#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdio>

using namespace std;

#define mp make_pair
typedef long long llong;
typedef unsigned long long ullong;
typedef pair<int, int> PI;
typedef pair<int, PI> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;

set<string> S1, S2;
int war(){
	set<string> s1 = S1;
	set<string> s2 = S2;
	int tot = 0;
	for(set<string>::iterator it = s1.begin(); it != s1.end(); ++it){
		set<string>::iterator up = s2.upper_bound(*it);
		if(up == s2.end()){
			tot++;
			s2.erase(*s2.begin());
		}else{
			s2.erase(*s2.upper_bound(*it));
		}
	}
	return tot;
}
int deceitfulWar(){
	vector<string> V1(S1.begin(), S1.end());
	vector<string> V2(S2.begin(), S2.end());
	int cur = 0;
	int tot = 0;
	for(int i = 0; i < V1.size(); ++i){
		if(V1[i] > V2[cur]){
			tot++;
			cur++;
		}
	}
	return tot;
}
int main()
{
	ios_base::sync_with_stdio(false);
	// freopen("input.txt", "r", stdin);
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int tc;
	cin >> tc;
	for(int t = 1; t <= tc; ++t){
		int N;
		cin >> N;
		S1.clear();
		S2.clear();
		for(int i = 0; i < N; ++i){
			string S;
			cin >> S;
			S1.insert(S);
		}
		for(int i = 0; i < N; ++i){
			string S;
			cin >> S;
			S2.insert(S);
		}
		cout << "Case #" << t << ": " << deceitfulWar() << ' ' << war() << endl;
	}
	return 0;
}


