#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;
#define LL long long

int N, M;
char S[100][100];
int len[100];
int G[10];
int ans, way;

const int MaxNode = 123456;
struct Node {
  int nxt[26];
  int clear() {
    fill(nxt,nxt+26,-1);
  }
}T[MaxNode];
int tot, root;

void clear() {
  tot=0;
  root = tot ++;
  T[0].clear();
}

void ins(char *S, int l) {
  int p = root ;
  for(int i=0;i<l;++i)
  {
    if(T[p].nxt[S[i] - 'A'] < 0) {
      T[T[p].nxt[S[i] - 'A'] = tot ++].clear();
    }
    p = T[p].nxt[S[i] - 'A'];
  }
}

int calc() {
  int ret=0;
  for(int i=0;i<N;++i) {
    clear();
    for(int j=0;j<M;++j)
      if(G[j] == i)
        ins(S[j], len[j]);
    if(tot==1) continue;
    ret += tot;
  }
  return ret;
}
int cnt;
int dfs(int d) {
  if(d == M) {
    ++ cnt;
    int now = calc();
    if(now > ans) ans = now, way = 1;
    else
    if(now == ans) way ++;
    return 0;
  }
  for(G[d] = 0; G[d] < N; ++ G[d])
    dfs(d + 1);
}

int run() {
  scanf("%d %d", &M,&N);
  for(int i=0;i<M;++i) {
    scanf("%s", S[i]);
    len[i] = strlen(S[i]);
  }
  cnt=0;
  ans=way=0;
  dfs(0);
  cerr << ">>>> cnt = "<<cnt<<endl;
}

int main() {
  freopen("D.in","r",stdin);
  freopen("D.out","w",stdout);
  int test;
  scanf("%d", &test);
  for(int no=1;no<=test;++no) {
    printf("Case #%d:", no);
    run();
    printf(" %d %d\n", ans, way);
  }
}

