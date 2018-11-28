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

int no;
int A[1002];
int N;
int pos[1002];
vector<int >X;
int P[1002],T[10000];

int calc() {
  int ret=0;
  int p =0;
  for(int i=0;i<N;++i)
    if(P[i] == N-1) p = i;
  for(int i=p-1;i>=0;--i)
    if(P[i] > P[i + 1]) return -1;
  for(int i=p+1;i<N;++i)
    if(P[i] > P[i - 1]) return -1;
  for(int i=0;i<N;++i)T[i]=A[i];
  for(int i=0;i<N;++i) {
    if(T[i]==P[i]) continue;
    for(int j=i+1;j<N;++j){
      if(T[j]==P[i]){
        ret +=j - i;
        for(int k=j;k>i;--k)
          swap(T[k],T[k-1]);
        break;
      }
    }
  }
  return ret;
}

int run() {
  scanf("%d", &N);
  X.clear();
  for(int i=0;i<N;++i) {
    scanf("%d",A+i);
    X.push_back(A[i]);
  }
  sort(X.begin(), X.end());
  for(int i=0;i<N;++i) {
    A[i] =lower_bound(X.begin(), X.end(), A[i]) - X.begin();
    pos[A[i]] = i;
  }
  if(N <= 2) return 0;
  for(int i=0;i<N;++i)
    P[i]=i;
  int ans = 987654321;
  do {
    int tmp = calc();
    if(tmp < 0) continue;
    if(tmp<ans)ans=tmp;
  } while(next_permutation(P,P+N));
  return ans;
}

int main() {
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  
  int test;
  scanf("%d", &test);
  for(no=1;no<=test;++no)
    printf("Case #%d: %d\n", no, run());
}
