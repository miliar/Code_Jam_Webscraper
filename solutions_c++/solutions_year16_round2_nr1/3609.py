#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <climits>
#include <cstring>
#include <cfloat>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stdexcept>
#include <sstream>
#include <cctype> //isdigit isalpha isalnum

using namespace std;

#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ULL unsigned long long
#define LL long long
#define REP(i,n) for(int i=0;i<(n);i++)
#define feq(x,y) (fabs(x-y) <= DBL_EPSILON)

#define MAXN 33000

#define MOD 1000000007

typedef pair<int,int> ii;
#define mp make_pair


#define sq(x) ((x)*(x))


string words[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

char table[26] = {0};

bool dfs(int k, vector<int> &ans) {
	if(k >= 10) {
		for(int i=0;i<26;i++) {
			if(table[i] > 0) 
				return false;
		}
		return true;
	}
	bool good = true;
	for(int nn=0;good;nn++) {
		char ztable[26] ={0};
		for(int i=0;i<words[k].size();i++) {
			ztable[words[k][i]-'A'] += nn;
		}
		for(int i=0;i<26;i++) {
			if(ztable[i] > table[i]) {
				good = false;
				break;
			}
		}
		if(good) {
			for(int i=0;i<words[k].size();i++) {
				table[words[k][i]-'A'] -= nn;
			}
			if(dfs(k+1, ans)) {
				for(int j=0;j<nn;j++)
					ans.push_back(k);
				return true;
			}
			for(int i=0;i<words[k].size();i++) {
				table[words[k][i]-'A'] += nn;
			}
		}
	}
	return false;
}

vector<int> solve(string str) {

	vector<int> ans;
	for(int i=0;i<26;i++)
		table[i] = 0;
	for(int i=0;i<str.size();i++) {
		table[str[i] - 'A'] += 1;
	}
	dfs(0, ans);

	sort(ans.begin(), ans.end());
	return ans;
}


//#define ONLINE_JUDGE
int main() {

#ifndef ONLINE_JUDGE
	//freopen("std", "r", stdin);
	freopen("small1", "r", stdin);
	freopen("out", "w+", stdout);
#endif

	int ts = 0;
	cin >> ts;
	for(int t=1;t<=ts;t++) {
		string str;
		cin >> str;
		vector<int> ans = solve(str);
		cout<<"Case #"<<t<<": ";
		for(int i=0;i<ans.size();i++) {
			cout<<ans[i];
		}
		cout<<endl;
	}

	return 0;
}
