#include<bits/stdc++.h>
using namespace std;
void rd(int &x){
  int k, m=0;
  x=0;
  for(;;){
    k = getchar_unlocked();
    if(k=='-'){
      m=1;
      break;
    }
    if('0'<=k&&k<='9'){
      x=k-'0';
      break;
    }
  }
  for(;;){
    k = getchar_unlocked();
    if(k<'0'||k>'9'){
      break;
    }
    x=x*10+k-'0';
  }
  if(m){
    x=-x;
  }
}
void rd(char c[]){
  int i, sz=0;
  for(;;){
    i = getchar_unlocked();
    if(i!=' '&&i!='\n'&&i!='\r'&&i!='\t'&&i!=EOF){
      break;
    }
  }
  c[sz++] = i;
  for(;;){
    i = getchar_unlocked();
    if(i==' '||i=='\n'||i=='\r'||i=='\t'||i==EOF){
      break;
    }
    c[sz++] = i;
  }
  c[sz]='\0';
}
void wt_L(int x){
  char f[10];
  int m=0, s=0;
  if(x<0){
    m=1;
    x=-x;
  }
  while(x){
    f[s++]=x%10;
    x/=10;
  }
  if(!s){
    f[s++]=0;
  }
  if(m){
    putchar_unlocked('-');
  }
  while(s--){
    putchar_unlocked(f[s]+'0');
  }
}
void wt_L(const char c[]){
  int i=0;
  for(i=0;c[i]!='\0';i++){
    putchar_unlocked(c[i]);
  }
}
int main(){
  int TEST, test=0;
  rd(TEST);
  while(TEST--){
    char S[1111];
    int K, c, i, n, r=0;
    printf("Case #%d: ", ++test);
    fprintf(stderr, "r=%d\n", TEST);
    rd(S);
    rd(K);
    n = strlen(S);
    {
      int Lj4PdHRW;
      for(Lj4PdHRW= 0;Lj4PdHRW< (n-1) + 1;Lj4PdHRW++){
        S[Lj4PdHRW] = (S[Lj4PdHRW]=='-')?0:1;
      }
    }
    for(i=0;i<n-K+1;i++){
      if(S[i]==0){
        {
          int KL2GvlyY;
          for(KL2GvlyY= i;KL2GvlyY< (i+K-1) + 1;KL2GvlyY++){
            S[KL2GvlyY] ^= 1;
          }
        }
        r++;
      }
    }
    c = 0;
    for(i=0;i<n;i++){
      c += S[i];
    }
    if(c==n){
      wt_L(r);
      putchar_unlocked('\n');
    }
    else{
      wt_L("IMPOSSIBLE");
      putchar_unlocked('\n');
    }
  }
  return 0;
}
// cLay varsion 20170408-2

// --- original code ---
// {
//   int test = 0, TEST;
//   rd(TEST);
//   while(TEST--){
//     printf("Case #%d: ", ++test);
//     fprintf(stderr, "r=%d\n", TEST);
// 
//     int K;
//     char S[1111];
// 
//     int i, c, n, r = 0;
// 
//     rd(S, K);
//     n = strlen(S);
// 
//     S[0..n-1] = (S[0..]=='-')?0:1;
//     rep(i,n-K+1) if(S[i]==0) S[i..i+K-1] ^= 1, r++;
// 
//     c = 0;
//     rep(i,n) c += S[i];
//     if(c==n) wt(r); else wt("IMPOSSIBLE");
//   }
// }
