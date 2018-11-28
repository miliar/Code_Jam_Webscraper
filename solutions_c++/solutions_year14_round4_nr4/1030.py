#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#define MOD 1000000007
using namespace std;

int testcase,K,N,best,ans;
string S[10];
set <string> trie[10];
int D[10];

int main () {
  freopen("D-small-attempt0.in","r",stdin);
  freopen("D.out","w",stdout);
  scanf ("%d",&testcase);
  for (int TC=1;TC<=testcase;++TC) {
    scanf("%d%d",&N,&K);
    for (int i=0;i<N;++i) cin >> S[i];
    best = ans = 0;
    memset(D,0,sizeof(D));
    do {
      ++D[0];
      for (int i=0;i<N;++i)
        if (D[i] == K) {
          D[i] = 0;
          D[i+1]++;
        }
      for (int i=0;i<K;++i) trie[i].clear(); 
      for (int j=0;j<N;++j) {
        int it = D[j];
        for (int i=1;i<=S[j].length();++i) {
          trie[it].insert(S[j].substr(0,i));
        }
      }
      bool ok = 1;
      for (int i=0;i<K;++i)
        if (trie[i].size() == 0) {
          ok = 0;
          break;
        }
      if (!ok) continue;
      int tmp = 0;
      for (int i=0;i<K;++i) tmp += trie[i].size();
      if (tmp > best) {
        best = tmp;
        ans = 1;
    //    printf("best = %d: ");
     //   for (int i=0;i<N;++i) printf("%d",D[i]); printf("\n");
      }
      else if (tmp == best) {
        ++ans;
        if (ans >= MOD) ans = 0;
     //   printf("best = %d: ");
     //   for (int i=0;i<N;++i) printf("%d",D[i]); printf("\n");
      }
    } while (D[N] == 0); 
    printf("Case #%d: %d %d\n",TC,best+K,ans);
  }
  //system("pause");
}
