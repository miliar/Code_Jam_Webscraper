#include<cstdio>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;
typedef long long ll;
#define M 122222
#define N 12
struct Trie{
  int g[M][26],tot;
  void init(){
    memset(g[0],0,sizeof(g[0]));
    tot=1;
  }
  void add(char *s){
    int p=0;
    for (;*s;s++){
      int i=*s-'A';
      if (!g[p][i]){
        g[p][i]=++tot;
        memset(g[tot],0,sizeof(g[tot]));
      }
      p=g[p][i];
    }
  }
}trie;
char a[N][N];
map<int,int> ans;
int n,m,mm;

void dfs(int k,int state,int s){
  if (k>=n-1){
    if (mm-1-state>0){
      int i=mm-1-state;
      trie.init();
      for (int j=0;j<m;++j)
        if ((i>>j)&1) trie.add(a[j]);
      ++ans[s+trie.tot];
    }
    return ;
  }
  for (int i=1;i<mm;++i)
    if ((state&i)==0){
      trie.init();
      for (int j=0;j<m;++j)
        if ((i>>j)&1) trie.add(a[j]);
      dfs(k+1,state+i,s+trie.tot);
    }
}

void solve(){
  int i,j,k;
  scanf("%d%d",&m,&n);
  for (i=0;i<m;++i) scanf("%s",a[i]);
  mm=1<<m;
  ans.clear();
  dfs(0,0,0);
  map<int,int>::iterator it=ans.end();
  --it;
  printf("%d %d\n",it->first,it->second);
}

int main(){
  int t,tt;
  freopen("1.txt","r",stdin);
  freopen("2.txt","w",stdout);
  scanf("%d",&t);
  for (tt=1;tt<=t;++tt){
    printf("Case #%d: ",tt);
    solve();
  }
  return 0;
}