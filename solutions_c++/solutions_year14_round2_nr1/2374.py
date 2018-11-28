#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <bitset>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <fstream>
#include <tuple>
#include <set>
#include <functional> 
#include <string.h>
//#include <assert.h>
//#include <typeinfo.h>
#include <time.h>

#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define FOR(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define REP(i, a, n) for(int (i) = (a); (i) < (n); ++(i))
typedef long long ll;
typedef std::pair<int, int> pii;
typedef std::pair<ll, ll > pll;
using namespace std;

const int INIT_SIZE_MAX = (1 << 29) + 10;
const int INIT_SIZE_MIN = -(1 << 29) - 10;
const int INIT_SIZE = 0;
const int MAX = 8;
const int DIR_SIZE = 12;
const double PI = 3.1415926535897932384;

template<class T, class U>
void convert(T &t, U &u){
	stringstream ss;
	ss << t;
	ss >> u;
}

int main(){
	int n; cin >> n;

	for (int i = 1; i <= n; ++i){
		int m; cin >> m;

		vector<pair<char, int> > all_char;
		vector<vector<pair<char, int> > > input;
		vector<pair<char, int> > prevs;
		bool f = true;
		FOR(j, m){
			string s; cin >> s;
			vector<pair<char, int> > tmp;
			char prev = ' ';
			int cnt = 0;
			FOR(k, s.size()){
				if (!k){
					prev = s[k];
					++cnt;
				}
				else{
					if (s[k] != prev){
						tmp.push_back(MP(prev, cnt));

						prev = s[k];
						cnt = 1;
					}
					else{
						++cnt;
					}
				}

				if (all_char.size() <= tmp.size()){
					all_char.push_back(MP(prev, cnt));
				}
				else{
					++all_char[tmp.size()].second;
				}
			}
			tmp.push_back(MP(prev, cnt));

			input.push_back(tmp);

			if (!j){
				prevs = tmp;
			}
			else{
				if (tmp.size() != prevs.size()) f = false;
				else{
					FOR(k, tmp.size()){
						if (prevs[k].first != tmp[k].first){
							f = false;
							break;
						}
					}
				}
			}

			if (!f) break;
		}

		if (!f){
			cout << "Case #" << i << ": Fegla Won" << endl;
			continue;
		}
		
		vector<pair<char, int> > opt_str;
		for (auto j : all_char){
			opt_str.push_back(MP(j.first, j.second / m));
		}

		int ans = 0;
		FOR(j, input.size()){
			FOR(k, input[j].size()){
				ans += abs(opt_str[k].second - input[j][k].second);
			}
		}

		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}