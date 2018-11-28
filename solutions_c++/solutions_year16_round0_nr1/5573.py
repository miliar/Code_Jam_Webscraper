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

bool mark[10];
int cnt;
		ll n; 

void doJob(int x){
	while(x){
		if(!mark[x % 10])
			mark[x % 10] = 1, cnt ++;
		x /= 10;
	}
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
//	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int T; cin >> T;
	for(int t = 1; t <= T; ++t){
		cin >> n;
		if(n == 0){
			cout << "Case #" << t << ": " << "INSOMNIA\n";
			continue;
		}
		memset(mark, 0, sizeof mark); 
		cnt = 0;
		ll m = 0;
		while(cnt < 10){
			m += n;
			doJob(m);
		}
		cout << "Case #" << t << ": " << m << "\n";
	}
	return 0;
}
