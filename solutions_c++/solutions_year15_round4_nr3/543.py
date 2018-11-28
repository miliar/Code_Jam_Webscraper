#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define pr(x) cout << #x << " = " << (x) << endl
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
#define FOR(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()

#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
const int INF = 1001001001;
const llint INFll = 9008007006005004003ll;

typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

vector<vector<string> > sents;
set<string> eng, fre;

char temp[12345];

bool addWord(const string &str, set<string> &ss) {
	if (ss.find(str) == ss.end()) {
		ss.insert(str);
		return true;
	}
	return false;
}
bool addWord(const string &str, bool engp) {
	return addWord(str, engp ? eng : fre);
}
bool removeWord(const string &str, set<string> &ss) {
	return ss.erase(str) > 0;
}
bool removeWord(const string &str, bool engp) {
	return removeWord(str, engp? eng : fre);
}

bool exists(const string &str, set<string> &ss) {
	return ss.find(str) != ss.end();
}
bool exists(const string &str, bool engp) {
	return exists(str, engp? eng: fre);
}

int ans;
int N;
typedef set<string>::iterator Itr;
void solve(int depth = 0, int count = 0) {
	if (depth == N) {
		/*
		Itr ei = eng.begin(), fi = fre.begin();
		int count = 0;
		while (ei != eng.end() && fi != fre.end()) {
			if (*ei < *fi) ei++;
			else if (*ei > *fi) fi++;
			else {
				count ++;
				ei++;
				fi++;
			}
		}
		*/
		if (count < ans) ans = count;
		return;
	}
	
	int siz = sents[depth].size();
	bool used[16];
	rep(k, 2) {
		int count2 = count;
		rep(i, siz) {
			used[i] = addWord(sents[depth][i], k==0);
			if (used[i] && exists(sents[depth][i], k!=0)) count2++;
		}
		solve(depth + 1, count2);
		rep(i,siz) if (used[i]) removeWord(sents[depth][i], k==0);
	}
}

int main() {
	int Test = in();
	for (int test = 1; test <= Test; test++) {
		cerr << test << endl;
		sents.clear();
		eng.clear();
		fre.clear();
		ans = INF;
		
		N = in();
		scanf(" ");
		int count = 0;
		rep(i,N) {
			sents.pb(vector<string>());
			gets(temp);
			int len = strlen(temp);
			temp[len] = 32;
			temp[len+1] = 0;
			size_t current = 0, found;
			string hoge = temp;
			while ((found = hoge.find_first_of(' ', current)) != string::npos) {
				sents[i].push_back(string(hoge, current, found - current));
				current = found + 1;
				if (i <= 1) {
					//pr(sents[i][sents[i].size() - 1]);
					if (addWord(sents[i][sents[i].size() - 1], i == 0)) {
						if (exists(sents[i][sents[i].size() - 1], i != 0)) count++;
					}
				}
			}
		}
		solve(2, count);
		
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
