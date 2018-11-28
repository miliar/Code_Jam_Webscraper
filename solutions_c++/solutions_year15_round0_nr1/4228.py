#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

#define For(Q,W) for(int Q=0; Q<W; Q++)

void solve(int T){
  int M;
  scanf("%d ",&M);
  vector<int> pom;
  For(i,M+1){
      char p;
      scanf(" %c ",&p);
      pom.push_back(p-'0');
  }
  int treba=0;
  int mam=0;
  
  For(i,M+1){
      if(mam<i){
          treba+=i-mam;
          mam+=i-mam;
      }
      mam+=pom[i];
  }
  
  printf("Case #%d: ",T+1);
  printf("%d\n",treba);
}

int main(){
  int T;
  scanf("%d ",&T);
  For(i,T) solve(i);
  return 0;
}

