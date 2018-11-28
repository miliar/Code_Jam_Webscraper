#include "cstdio"
#include "iostream"
#include "vector"
#include "algorithm"
#include "cstring"
#include "set"
#include "map"
#include "queue"
#define runtime() ((double)clock() / CLOCKS_PER_SEC)
#define rep(i, n) for(int i=0; i<n; i++)
#define repp(i, a, b) for(int i=a; i<a+b; i++)
using namespace std;
inline int getint(){
  char c = getchar();
  for(;c<'0'||c>'9';) c = getchar();
  int x = 0;
  for(;c>='0' && c<='9'; c = getchar()) x*=10, x+=c-'0';
  return x;
}
const int maxn = 2000;
int n,m;
char s[20][maxn];

int a[10];
std::vector<int> b[10];

struct node{
	node *ch[26];
}mem[10000], *C;

int tot;
node * clearnode(){
	C = &mem[0];
	tot = 0;
}
node * newnode(){
	tot++;
	memset(C->ch, 0, sizeof(C->ch));
	return C++;
}

int ans, ans2;
void dfs(int u){
	if(u==n){
		rep(i, m) b[i].clear();
		rep(i, n) b[a[i]].push_back(i);
		rep(i, m) if(!b[i].size()) return;
		int sum = 0;
		rep(i, m){
			clearnode();
			node *root = newnode();
			rep(j, b[i].size()){
				char *t = s[b[i][j]];
				int n = strlen(t);
				node *p = root;
				rep(k, n){
					int o = t[k] - 'A';
					if(!p->ch[o]) p->ch[o] = newnode();
					p = p->ch[o];
				}
			}
			sum += tot;
		}
		if(sum>ans){
			ans = sum;
			ans2 = 1;
		}else{
			if(sum==ans) ans2++;
		}
		return;
	}
	rep(j, m){
		a[u] = j;
		dfs(u+1);
	}
}
int main(int argc, char const *argv[])
{
	int cass;cin>>cass;
	repp(cas, 1, cass){
		n = getint(), m = getint();
		rep(i, n){
			scanf("%s", s[i]);
		}
		ans = ans2 = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", cas, ans, ans2);
	}

	return 0;
}