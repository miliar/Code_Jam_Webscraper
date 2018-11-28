#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <functional>
#include <numeric>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
#include <stdio.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

int n, par[105];
char wd[105];
string obj[10];

vector<int> gph[105];
int cnt[10], tried[10];

string random_traversal(int x){
	vector<string> v;
	int cur = 0;
	for(auto &i : gph[x]){
		string t = random_traversal(i);
		cur += t.size();
		reverse(t.begin(), t.end());
		v.push_back(t);
	}
	string ret;
	if(x) ret.push_back(wd[x]);
	while(cur > 0){
		int t = rand() % cur;
		for(int j=0; j<v.size(); j++){
			if(t < v[j].size()){
				ret.push_back(v[j].back());
				v[j].pop_back();
				break;
			}
			t -= v[j].size();
		}
		cur--;
	}
	return ret;
}

int main(){
	srand(time(0));
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d:", i);
		cin >> n;
		for(int i=1; i<=n; i++){
			cin >> par[i];
			gph[par[i]].push_back(i);
		}
		cin >> (wd + 1);
		int q;
		cin >> q;
		for(int i=1; i<=q; i++){
			cnt[i] = tried[i] = 0;
			cin >> obj[i];
		}
		for(int i=1; i<=3000; i++){
			string ok = random_traversal(0);
			for(int j=1; j<=q; j++){
				tried[j]++;
				if(ok.find(obj[j]) != string::npos){
					cnt[j]++;
				}
			}
		}
		for(int i=1; i<=q; i++){
			printf(" %.10f",1.0 * cnt[i] / tried[i]);
		}
		for(int i=0; i<=n; i++){
			gph[i].clear();
		}
		puts("");
	}
}