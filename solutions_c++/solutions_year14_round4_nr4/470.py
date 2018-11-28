										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int n, k, sd[10];
int worst, cnt;
string str[10];
set <string> st;

void bt(int idx){
	if(idx == n){
		int sum = 0;
		for(int i = 0; i < k; i++){
			st.clear();
			for(int j = 0; j < n; j++){
				if(sd[j] != i) continue;
				for(int l = 1; l <= str[j].length(); l++)
					st.insert(str[j].substr(0, l));
			}
			if(st.empty())
				return;
			sum += st.size() + 1;
		}
		if(sum > worst){
			worst = sum;
			cnt = 0;
		}
		if(sum == worst)
			cnt++;
		return;
	}

	for(int i = 0; i < k; i++){
		sd[idx] = i;
		bt(idx + 1);
	}
}

int main(){
	freopen("D_Trie Sharding.in", "r", stdin);
	freopen("D_Trie Sharding.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> k;
		for(int i = 0; i < n; i++)
			cin >> str[i];
		worst = cnt = 0;
		bt(0);
		cout << "Case #" << ++ test << ": " << worst << " " << cnt << endl;
	}
	return 0;
}
