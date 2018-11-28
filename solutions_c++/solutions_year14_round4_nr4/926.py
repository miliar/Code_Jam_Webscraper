#include <bits/stdc++.h>
using namespace std;
#define fr(i,a,b) for(int i = a; i < b; ++i)
#define rep(i, n) fr(i,0,n)
#define _(n) rep(i, n)
#define mp make_pair
#define ft first
#define sd second
#define pb push_back
typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long hash;

vector<string> st;
int n;

struct No{
	map<char, int> adj;
	void init(){
		adj.clear();
	}
};

struct Trie{
	int prt;
	No nodes[10000];
	vector<string> aqui;

	void clear(){
		prt = 1;
		nodes[0].init();
		aqui.clear();
	}

	void insert(string& a){
		aqui.pb(a);
		int at = 0;

		rep(i, a.size()){
			if(nodes[at].adj.find(a[i]) == nodes[at].adj.end()){
				nodes[prt].init();
				nodes[at].adj[a[i]] = prt++;
			}
			at = nodes[at].adj[a[i]];
		}
	}

	int count(){
		return prt;
	}

	// void db(){
	// 	for(string x : aqui) cout << x << endl;
	// }


}tries[10];

int maior, occ;

void faz(int msk, int server){
	if(server == n){
		if(!msk){
			int cnt = 0;
			_(n) cnt += tries[i].count();
			if(cnt == maior){
				++occ;
				// printf("Maior %d\n", maior);
				// _(n) printf("\t %d\n", tries[i].count());
				// _(n) printf("%d\n", i), tries[i].db();
			}
			else if(cnt > maior){
				occ = 1;
				maior = cnt;
			}
		}
		return;
	}
	if(!msk) return;

	for(int m = msk; m > 0; m = msk & (m-1)) {
		tries[server].clear();

		_(st.size()) if(m&(1<<i)){
			tries[server].insert(st[i]);
		}
		faz(msk^m, server+1);
	}
}

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;

// cout << "ici " << tries[4].count() << endl;;
	for(int tt = 1; tt <= t; ++tt){
		st.clear();
		int m;
		cin >> m >> n;
		_(m){
			string tmp;
			cin >> tmp;
			st.pb(tmp);
		}
		maior = 0;
		faz((1<<m)-1, 0);



		cout << "Case #" << tt << ": " << maior << " " << occ << endl;
	}
}
