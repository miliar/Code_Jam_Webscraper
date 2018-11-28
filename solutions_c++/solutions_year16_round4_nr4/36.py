#include<bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define UPD(a,b) { a = a + (b); }

int cur_l = 0, cur_r = 0;
int A[55][55], vis[55];
int n;
void dfs(int i) {
	vis[i] = true;
	if (i <= n) {
		++cur_l;
		For(j,1,n) if (A[i][j] && !vis[n + j]) dfs(n + j);
	} else {
		++cur_r;
		For(j,1,n) if (A[j][i - n] && !vis[j]) dfs(j);
	}
}

const int MAXN = 10000000;
map< vector<int>, int > Map;
vector<int> vec[MAXN];
vector< pair<int, int> > items;
pair<int,int> List[55];
int id = 0;
int num[55], rec[55];
void dfs(int now, int cl, int cr) {
	if (now > id) {
		vector<int> tmp(rec + 1, rec + now);
		if (!Map.count(tmp)) {
			vec[Map[tmp] = Map.size()] = tmp;
		}
		if (cl == cr) {
			items.emplace_back(Map[tmp], cl * cr);
		}
		return ;
	}
	For(j,0,num[now]) {
		rec[now] = j;
		dfs(now + 1, cl + List[now].first * j, cr + List[now].second * j);
	}
}

int f[MAXN], calc[MAXN];
pair<int,int> pre[MAXN];
int dp(int now) {
	if (calc[now]) return f[now];
	calc[now] = true;
	if (now == 1) return 0;
	f[now] = 100000000;
	vector<int> tmp = vec[now];
	for (auto &arr : items) {
		//if (arr.first > now) continue ;
		bool gg = false;
		int who = arr.first;
		For(j,0,id - 1) if (tmp[j] < vec[who][j]) {
			gg = true;
			break ;
		}
		if (gg) continue ;
		For(j,0,id - 1) tmp[j] -= vec[who][j];
		int t = dp(Map[tmp]) + arr.second;
		if (t < f[now]) {
			f[now] = t;
			pre[now] = make_pair(who, Map[tmp]);
		}
		For(j,0,id - 1) tmp[j] += vec[who][j];
	}
	return f[now];
};

char str[55][55];
int have[55][55];
int tag[55][55];
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		cin >> n;
		int cnt = 0;
		For(i,1,n) scanf("%s", str[i] + 1);
		For(i,1,n) For(j,1,n) {
			A[i][j] = str[i][j] - '0';
			cnt += A[i][j];
		}
		memset(vis, 0, sizeof vis);
		id = 0;
		memset(have, 0, sizeof have);
		memset(tag, 0, sizeof tag);
		For(i,1,n + n) if (!vis[i]) {
			cur_l = 0, cur_r = 0;
			dfs(i);
			if (!tag[cur_l][cur_r]) {
				List[tag[cur_l][cur_r] = ++id] = make_pair(cur_l, cur_r);
			}
			++have[cur_l][cur_r];
		}
		For(i,1,id) num[i] = have[List[i].first][List[i].second];
		Map.clear();
		items.clear();
		dfs(1, 0, 0);
		memset(calc, 0, sizeof calc);
		int S = Map.size();
		cout << dp(S) - cnt << endl;
		//while (S > 1) {
		//	int x = pre[S].first;
		//	for (auto y: vec[x]) printf("%d ", y); puts("");
		//	S = pre[S].second;
		//}
	}
	return 0;
}
