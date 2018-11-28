#include <iostream>
#include <cstdio>
#include <ctime>
#include <cassert>
#include <cmath>
#include <stack>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

#ifdef WIN32
	#define lld "%I64d"
#else
	#define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;

const int M = 3 * 1e6;
const ll Q = 1e9 + 7;




vector<string> V, g[M];
vector<int> f[M];
int a[M][2];
map<string, int> ma;


void upd(int &cur, int i, int t){
	a[i][t]++;
	if (a[i][t] == 1 && a[i][1 - t])
		cur++;
}
void del(int i, int t){
	a[i][t]--;
}
int main(){
	srand(time(NULL));
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int tq = 1; tq <= t; tq++){


		
		int n;
		scanf("%d\n", &n);
		for (int i = 0; i < 3000; i++)
			a[i][0] = a[i][1] = 0;
		for (int i = 0; i < n; i++){
			g[i].resize(0);
			f[i].resize(0);
		}
		V.resize(0);
		for (int i = 0; i < n; i++){
			string h;
			getline(cin, h);
			h = h + " ";
			string cur = "";
			for (int j = 0; j < (int)h.size(); j++){
				if (h[j] == ' '){
					g[i].pb(cur);
				    V.pb(cur);
					cur = "";
				}	
				else
					cur += h[j];
			}
		}
		sort(V.begin(), V.end());
		int pos = 0;
		int cnt = 0;
		while (pos < (int)V.size()){
			int i = pos;
			while (i < (int)V.size() && V[i] == V[pos])
				i++;
			for (int j = pos; j < i; j++)
				ma[V[j]] = cnt;
			cnt++;
			pos = i;	
		}
		assert(cnt < 3000);

		for (int i = 0; i < n; i++){
			for (int j = 0; j < (int)g[i].size(); j++)
				f[i].pb(ma[g[i][j]]);
		}

	/*	for (int i = 0; i < n; i++){
			cout << i << ":" << endl;
			for (int j = 0; j < (int)g[i].size(); j++)
				cout << g[i][j] << " ";
			cout << endl;
			for (int j = 0; j < (int)g[i].size(); j++)
				cout << f[i][j] << " " ;
				cout << endl;	
		}   */


		int pr = 0;
		for (int i = 0; i < 2; i++){
			for (int j = 0; j < (int)g[i].size(); j++)
				upd(pr, f[i][j], i); 
		}

		int ans = Q;
		for (int mask = 0; mask < (1 << (n - 2)); mask++){
			int cur_ans = pr;
			for (int i = 2; i < n; i++){
				int col = ((mask >> (i - 2)) & 1);
				for (int j = 0; j < (int)g[i].size(); j++)
					upd(cur_ans, f[i][j], col);
			}
			ans = min(ans, cur_ans);
		
			for (int i = 2; i < n; i++){
				int col = ((mask >> (i - 2)) & 1);
				for (int j = 0; j < (int)g[i].size(); j++)
					del(f[i][j], col);
			}
		
		}


		
		cout << "Case #" << tq << ": ";
		printf("%d\n", ans);	
		cerr << tq << endl;	
	}


	return 0;
}	