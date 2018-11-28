
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <cassert>
#include <unordered_set>
#include <unordered_map>
#include <fstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)

int getIntVal(){
	string in;
	getline(cin, in);
	istringstream is(in);
	int v;
	is >> v;
	return v;
}

set<int> has_word[256];
pair<int,int> word_bridge[50000];
set<int> word_in_sentence[50000];
vector<bool> vis_n;
vector<bool> vis_w;
bool rek(int n){
	if(n == 1)return true;
	if(vis_n[n])return false;
	vis_n[n] = true;
	for(auto w: has_word[n]){
		if(vis_w[w])continue;
		if(word_bridge[w].first == word_bridge[w].second
				|| word_bridge[w].second == n){
			vis_w[w] = true;
			for(auto to: word_in_sentence[w]){
				if(rek(to)){
					if(word_bridge[w].first == word_bridge[w].second){
						word_bridge[w].first = n;
					}
					word_bridge[w].second = to;
					return true;
				}
			}
		} else {
			int to = word_bridge[w].first;
			if(rek(to)){
				word_bridge[w].first = n;
				return true;
			}
		}
	}
	return false;
}

void calc(){
	unordered_map<string, int> string_id;
	int S = 0;
	int N = getIntVal();
	FOR(i,0,N){
		has_word[i].clear();
		string in;
		getline(cin, in);
		istringstream is(in);
		while(is >> in){
			if(string_id.find(in) == string_id.end()){
				word_bridge[S] = pii (-1, -1);
				word_in_sentence[S].clear();
				string_id[in] = S++;
			}
			has_word[i].insert(string_id[in]);
			word_in_sentence[string_id[in]].insert(i);
		}
	}
	int res = 0;
	while(true){
		vis_n = vector<bool>(N, false);
		vis_w = vector<bool>(S, false);
		if(rek(0))++res;
		else break;
	}
	cout << res << endl;
}


int main() {
	int TC = getIntVal();
	FOR(tc, 1, TC + 1){
		cout << "Case #" << tc << ": ";
		calc();
	}
	return 0;
}
