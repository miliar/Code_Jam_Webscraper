#include <stdio.h>
#include <vector>
#define MOD 1000000007

using namespace std;

struct SH{
  int h1, h2;
};
vector<SH> vec[12];

char kal[12][12];
int assg[12];
int N, M;
int ans, ctans;

void Count(){
  for(int i=0; i<N; i++){
    bool found = false;
    for(int j=0; j<M; j++){
      if(assg[j] == i) found = true;
    }
    if(!found) return;
  }
  for(int i=0; i<N; i++) vec[i].clear();
  int sum = 0;
  
  SH h;
  for(int i=0; i<M; i++){
    h.h1 = h.h2 = 0;
    for(int j=0; kal[i][j]!='\0'; j++){
      h.h1 *= 31;
      h.h2 *= 41;
      h.h1 += (kal[i][j]-64);
      h.h2 += (kal[i][j]-64);
      h.h1 %= MOD;
      h.h2 %= MOD;
      
      bool add = true;
      for(vector<SH>::iterator k=vec[assg[i]].begin(); k!=vec[assg[i]].end(); k++){
        if(((k->h1)==h.h1)&&((k->h2)==h.h2)){
          add = false;
          break;
        }
      }
      if(add){
        vec[assg[i]].push_back(h);
        sum++;
      }
    }
  }
  
  if(sum > ans){
    ans = sum;
    ctans = 1;
  }
  else if(sum == ans) ctans++;
}

void Assign(int lv){
  if(lv == M){
    Count();
    return;
  }
  
  for(int i=0; i<N; i++){
    assg[lv] = i;
    Assign(lv+1);
  }
}

int main(){
  int jcase;
  
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("D-small-attempt0.out", "w", stdout);
  
  scanf("%d", &jcase);
  for(int icase=0; icase<jcase; icase++){
    scanf("%d %d", &M, &N);
    for(int i=0; i<M; i++) scanf("%s", kal[i]);
    
    ans = ctans = 0;
    Assign(0);
    printf("Case #%d: %d %d\n", icase+1, ans+N, ctans);
  }
  
  return 0;
}
