#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <set>
#include <string>

using namespace std;

#define FOE(i, s, t) for (int i = s; i <= t; i++)

#define M 5000001

int min(int a, int b){
	if (a > b) return b; else return a;
}

int max(int a, int b){
	if (a < b) return b; else return a;
}

int nxt[M], dir[M], f[M], rev[M], h;
int S, T, n;

string zz;
int lvl[M], Q[M], top, tail;

bool BFS(){
	FOE(i, 0, T) lvl[i] = -1;
	lvl[S] = 0;
	top = tail = 0;
	Q[top++] = S;
	while (top > tail){
		int u = Q[tail++];
	//	printf("BFS %d\n", u);
		for (int po = nxt[u]; po > 0; po = nxt[po]) if (f[po] && lvl[dir[po]] == -1){
			lvl[dir[po]] = lvl[u] + 1;
			Q[top++] = dir[po];
		}
	}
	return (lvl[T] != -1);
}

int DFS(int u, int flow){
	if (flow == 0) return 0;
	if (u == T) return flow;
	int w = flow;
	for (int po = nxt[u]; po > 0; po = nxt[po]) if (f[po] > 0 && lvl[dir[po]] == lvl[u] + 1){
		int y = DFS(dir[po], min(w, f[po]));
	//	if (y > 0) printf("FLOW FROM %d to %d, %d\n", u, dir[po], y);
		w -= y;
		f[po] -= y;
		f[rev[po]] += y;
	}
	if (w == flow) lvl[u] = -90;
	return flow - w;
}

#define inf 100000000

int MaxFlow(){
	int ans = 0, p;
	while (BFS()){
		do{
			p = DFS(S, inf);
	//		printf("FLOW %d\n", p);
			ans += p;
		} while (p != 0);
	}
	return ans;
}

int insert(int a, int b, int c){
	//printf("INSERT %d->%d, %d\n", a, b, c);
	nxt[++h] = nxt[a]; nxt[a] = h; dir[h] = b; f[h] = c; rev[h] = h + 1;
	nxt[++h] = nxt[b]; nxt[b] = h; dir[h] = a; f[h] = 0; rev[h] = h - 1;
}

string word1[10001], word2[10001], sup1[10001], sup2[10001];
int c1[1001], c2[1001];
int cnt3, cnt4;

bool equal(string a, string b){
	if (a.length() != b.length()) return false;
	for (int i = 0; i < a.length(); i++) if (a[i] != b[i]) return false;
	for (int i = 0; i < a.length(); i++) if (a[i] == 'A') return false;
	return true;
}

int rep[1001][2], h2;

int my_id[301];
set<int> SS[3001];

int nxta[M][27];

void walk(int u, int p, int mine){
	//printf("WALK %d %d %d\n", u, p, mine);
	if (p == zz.length()){
		SS[u].insert(mine);
		return;
	}
	int id = (int)(zz[p] - 'a' + 1);
	if (nxta[u][id] == -1){
		nxta[u][id] = ++h2;
		FOE(i, 1, 26) nxta[h2][i] = -1;
		while (SS[h2].size()) SS[h2].erase(SS[h2].begin());
	}
	walk(nxta[u][id], p + 1, mine);
}

void walk2(int u){
	int v[3001],wyz = 0;
	for (set<int>::iterator it = SS[u].begin(); it != SS[u].end(); ++it){
		v[++wyz] = *it;
	}	
	//if (SS[u].size()) printf("%d\n", wyz);
	cnt3++;
	FOE(i, 1, wyz) {
		insert(v[i], cnt3, 1);
		insert(cnt3, v[i], 1);
	}
	for (int i = 1; i <= 26; i++) if (nxta[u][i] != -1) walk2(nxta[u][i]);
}

void solve(){
	int z = 0;
	h2 = 0;
	string w;
	scanf("%d", &n);
	FOE(i, 1, 26) nxta[0][i] = -1;
	S = 0;
	T = 3 * 10000 + 1;
	FOE(i, S, T) nxt[i] = -1;
	h = T + 1;
	cnt3 = 1;
	int ans = 0;
	getline(cin, w);
	getline(cin, w);
	int cnt1 = 1;
	word1[1] = "";
	FOE(i, 0, w.length() - 1){
		if (w[i] == ' '){
			cnt1++; word1[cnt1] = "";
		} else word1[cnt1] += w[i];
	}

	FOE(i, 1, n - 2) c1[i] = c2[i] = 0;

	getline(cin, w);
	int cnt2 = 1;
	word2[1] = "";
	FOE(i, 0, w.length() - 1){
		if (w[i] == ' '){
			cnt2++; word2[cnt2] = "";
		} else word2[cnt2] += w[i];
	}
	FOE(i, 1, 1000) sup1[i] = sup2[i] = "";
	FOE(i, 1, cnt1) FOE(j, 1, cnt1) if (i != j && equal(word1[i], word1[j])) {sup1[j] = word1[j]; word1[j] = "A";}
	FOE(i, 1, cnt2) FOE(j, 1, cnt2) if (i != j && equal(word2[i], word2[j])) {sup2[j] = word2[j]; word2[j] = "A";}
	FOE(i, 1, cnt1) FOE(j, 1, cnt2) if (equal(word1[i], word2[j])){
		sup1[i] = sup2[j] = word2[j];
		word1[i] = word2[j] = "A";
		ans++;
	}	
	FOE(i, 1, cnt1) if (word1[i][0] != 'A'){
		rep[i][0] = cnt3;
		insert(S, cnt3++, 1);
	}
	FOE(i, 1, cnt2) if (word2[i][0] != 'A'){
		rep[i][1] = cnt3;
		insert(cnt3++, T, 1);	
	}

	zz = "";

	FOE(q, 1, n - 2){
		getline(cin, w);
		cnt3++;
		int ok = 0;
		FOE(z, 0, w.length() - 1) if (w[z] == ' ') {
			ok = 0;
			FOE(i, 1, cnt1) if (equal(zz, word1[i])){
				//printf("MATCH %d %d 1\n", q, i);
				//insert(cnt3, rep[i][0], 10000);
				ok = 1;
				insert(rep[i][0], cnt3, 10000);
			}
			FOE(i, 1, cnt2) if (equal(zz, word2[i])){
			//	printf("MATCH %d %d 2\n", q, i);
				insert(cnt3, rep[i][1], 10000);
				//insert(rep[i][1], cnt3, 10000);
				ok = 1;
			} else if (equal(sup2[i], zz)) ok = 1;
			if (!ok){
			//	printf("NO %d %d\n", q, z);
				walk(0, 0, cnt3);
			}
			zz = "";
		}else {
			zz = zz + w[z];
		}
		ok = 0;
		FOE(i, 1, cnt1) if (equal(zz, word1[i])){
				//insert(cnt3, rep[i][0], 10000);
			insert(rep[i][0], cnt3, 10000);
			ok = 1;
		}
		FOE(i, 1, cnt2) if (equal(zz, word2[i])){
			insert(cnt3, rep[i][1], 10000);
			//insert(rep[i][1], cnt3, 10000);
			ok = 1;
		} else if (equal(sup2[i], zz)) ok = 1; 
		if (!ok){
			walk(0, 0, cnt3);
		}
		zz = "";
	}
	
	walk2(0);
	ans += MaxFlow();	

	printf("%d\n", ans);
//	getline(cin, w);
}

int main(){
	int t;
	scanf("%d", &t);
	for (int i = 1 ;i <= t; i ++){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
