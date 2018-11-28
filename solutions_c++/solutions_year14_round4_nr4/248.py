#include <bits/stdc++.h>
using namespace std;
const int limit = 1000 + 5;
string s[limit];
int d[limit];
int m,n;
int kq,cnt;

void check(){
	set<string> trie[10];
	for(int i = 1; i <= m; ++i){
		int k = d[i];
		for(int j = 1; j <= (int)s[i].size();++j)
			trie[k].insert( s[i].substr(0,j) );
	}
	
	int t = 0;
	for(int i = 1; i <= n; ++i) {
		t += trie[i].size() + 1;
		if (trie[i].empty()) return;
	}
	if (kq < t){
		kq = t;
		cnt = 1;
	}
	else if (kq == t) cnt++;
}

void attempt(int k = 1){
	if (k > m) check(); else
	for(int i = 1; i <= n; ++i){
		d[k] = i;
		attempt(k+1);		
	}
}

int main(){
	freopen("file.inp","r",stdin);
	freopen("data.txt","w",stdout);
	int test; scanf("%d",&test);
	for(int T = 1; T <= test; ++T){
		printf("Case #%d: ",T);
		
		
		scanf("%d%d\n",&m,&n);
		
		for(int i = 1; i <= m; ++i) getline(cin,s[i]);		
		kq = 0, cnt = 0;
		attempt();
		printf("%d %d\n",kq,cnt);
		
		
	}

}