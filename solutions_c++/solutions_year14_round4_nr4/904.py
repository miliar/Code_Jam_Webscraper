#include <map>
#include <set>
#include <queue>
#include <ctime>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define all(a) a.begin(),a.end()
#define clr(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VII;

const double eps = 1e-8;
const double pi = acos(-1.0);

#include <cstdio>
#include <cstring>
//儿子个数
#define CHILD_NUM 26
//结点个数：string length*string num
#define MAX_NODE 100
using namespace std;

struct Trie{
    int fail[MAX_NODE];
    int val[MAX_NODE];
	bool vis[MAX_NODE];
    int q[MAX_NODE];
    int chd[MAX_NODE][CHILD_NUM];
    int ID[128];
    int sz;

    Trie(){
        fail[0] = 0;
        for (int i = 0; i < 26; i++)
        ID[i+'A'] = i;
    }

    void reset(){
        memset(chd[0], 0, sizeof(chd[0]));
        memset(val, 0, sizeof(val));
        sz = 1;
    }

    void insert(char *s){
        int nid = 0, j;
        for ( ; *s; s ++){
            j = ID[*s];
            if(!chd[nid][j]){
                memset(chd[sz], 0, sizeof(chd[sz]));
                chd[nid][j] = sz++;
            }
            nid = chd[nid][j];
        }
    }
}trie;


int m, n;
vector<int> vec[10];
int ans, ansc;
char s[10][20];
void dfs(int u){
	if(u == m+1){
		int i, j;
		for(i=1;i<=n;++i) if(vec[i].empty()) return ;
		int tot = 0;
		for(i=1;i<=n;++i){
			trie.reset();
			for(j=0;j<vec[i].size();++j)
			trie.insert(s[vec[i][j]]);
			tot += trie.sz;
		}
		if(tot > ans) ans = tot, ansc=1;
		else if(tot==ans) ansc++;
		return ;
	}
	for(int i=1;i<=n;++i){
		vec[i].push_back(u);
		dfs(u+1);
		vec[i].pop_back();
	}
}

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	for(int cal = 1; cal <= tt; ++cal){
		scanf("%d%d",&m,&n);
		for(int i=1;i<=m;++i) scanf("%s",s[i]);
		ans = 0;
		dfs(1);
		printf("Case #%d: %d %d\n", cal, ans, ansc);
	}
    return 0;
}

