#include <bits/stdc++.h>
using namespace std;

bool mark[1<<20];
int n;
int s[1<<20],m[1<<20],where[1<<20],L[1<<20],H[1<<20];
vector<int> add[1<<20], del[1<<20], child[1<<20];

bool cmp (const int &a, const int &b){
	return s[a] < s[b];	
}

void dfs (int v, int lo, int hi){
	L[v] = min(lo, where[v]);
	H[v] = max(hi, where[v]);
	for (int i=0; i<(int)child[v].size(); i++)
		dfs(child[v][i], L[v], H[v]);
}

void main2(){
	int D;
	cin >> n >> D;
	int as,cs,rs;
	int am,cm,rm;
	cin >> s[0] >> as >> cs >> rs;
	cin >> m[0] >> am >> cm >> rm;
	for (int i=0; i<n; i++)
		mark[i] = false;
	for (int i=1; i<n; i++){
		s[i] = ((long long)s[i-1] * as + cs) % rs;
		m[i] = ((long long)m[i-1] * am + cm) % rm; 
	}
	for (int i=0; i<n; i++)
		child[i].clear();
	for (int i=1; i<n; i++){
		m[i] %= i;
		child[m[i]].push_back(i);
	}
	vector<int> p(n);
	for (int i=0; i<n; i++) p[i] = i;
	sort(p.begin(), p.end(), cmp);
	for (int i=0; i<n; i++)
		where[p[i]] = i;
	dfs(0,where[0],where[0]);
	for (int i=0; i<=n; i++){
		add[i].clear();
		del[i].clear();
	}
	for (int i=0; i<n; i++){
		del[L[i]].push_back(i);
		add[H[i]].push_back(i);
	}
	int pnt = 0;
	int cnt = 0, ans = 0;
	for (int i=0; i<n; i++){
		while (pnt<n && s[p[pnt]]-s[p[i]]<=D){
			for (int j=0; j<(int)add[pnt].size(); j++){
				int temp = add[pnt][j];
				if (i <= L[temp]){
					cnt++;
					mark[temp] = true;
				}
			}
			pnt++;
		}
		ans = max(ans, cnt);
		for (int j=0; j<(int)del[i].size(); j++) if (mark[del[i][j]]){
			mark[del[i][j]] = false;
			cnt--;
		}
	}	
	cout << ans << endl;
}

int main(){
	int t; cin >> t;
	for (int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		main2();
	}
	return 0;
}
