#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <deque>
#include <queue>
#include <ctime>
#include <cstring>
#include <iomanip>

#define SZ(x) ((int)x.size())
#define X first
#define Y second 
#define PB push_back 
#define MP make_pair 

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<pii, int> piii;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("output", "w", stdout);
	int T;
	bool f, g;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		string s;
		cin >> s;
		f = (s[0] == '+');
		int cnt = 1;
		for(int i = 1; i < SZ(s); ++i){	
			g = (s[i] == '+');
			if(f != g){
				f = g;
				cnt ++;
			}
		}
		if(s.back() == '+') cnt --;
		cout << "Case #" << t << ": " << cnt << "\n";;
	}
	return 0;
}
