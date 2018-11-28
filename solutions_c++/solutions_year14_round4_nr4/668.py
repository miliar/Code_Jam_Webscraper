#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<list>
#include<deque>
using namespace std;
#define MOD 1000000007

int ans, t, n, h1, h2, m;

struct trie
{
	trie* sm[26];
} tm[10000];

int tp = 0;

trie* new_node(){
	memset(tm[tp].sm, 0, sizeof(tm[tp].sm));
	return &tm[tp ++];
}

bool de = 0;

void insert(trie* p, char* s){
	if(*s == 0) return ;
	
	if((p -> sm[(*s) - 'A']) == 0){
		p -> sm[(*s) - 'A'] = new_node();
	}
	p = (p -> sm[(*s) - 'A']);
	insert(p, s+1);
}

vector<int> vs[4];
char sm[10][100];
int mxtp;

void dfs(int idx){
	//cout<<idx<<' '<<m<<endl;
	if(idx == m){
		trie* trm[4];
		tp = 0;
		for(int fh1 = 0 ; fh1 < n ; fh1 ++)
			trm[fh1] = new_node();
		int z = 0;
		for(int fh1 = 0 ; fh1 < n ; fh1 ++)
		{
			if(vs[fh1].size() == 0) z ++;
			for(int fh2 = 0 ; fh2 < vs[fh1].size() ; fh2 ++)
			{
				insert(trm[fh1], sm[vs[fh1][fh2]]);
			}
		}
		tp -= z;
		if(tp > mxtp){
			mxtp = tp;
			ans = 1;
		}
		else if(tp == mxtp){
			(ans += 1) %= MOD;
		}
		return ;
	}
	for(int i = 0 ; i < n ; i ++){
		vs[i].push_back(idx);
		dfs(idx + 1);
		vs[i].pop_back();
	}

}

int main(int argc, const char *argv[])
{
	int cc = 0;
	cin>>t;
	while(t--){
		tp = 0;
		cin>> m >> n;

		for(h1 = 0 ; h1 < m ; h1 ++){
			cin>>sm[h1];
		}

		mxtp = -1;
		ans = 0;
		dfs(0);

		printf("Case #%d: %d %d\n", ++cc, mxtp, ans);
	}
	return 0;
}
