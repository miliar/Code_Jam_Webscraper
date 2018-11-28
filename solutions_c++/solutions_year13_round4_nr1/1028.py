#include <stdio.h>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

int T, N, M;
long long int P = 1000002013;
//queue<pair<int, long long int> > q;

struct bla {
  long long int o, e, p;
};

int sorto(const bla &a, const bla &b) {
  if(a.o < b.o) return 1;
  if(a.o == b.o) return a.e < b.e;
  return 0;
}

int sorte(const bla &a, const bla &b) {
  if(a.e < b.e) return 1;
  if(a.e == b.e) return a.o < b.o;
  return 0;
}

bla blao[1010];
bla blae[1010];

stack<bla> s;

long long int calc(long long int o, long long int e) {
  long long int d = e - o;
  long long int res = d * N;
  
  res -= ((d-1)*d) / 2;
  return res;
}

int main() {
  scanf(" %d",&T);
  for(int t=1; t<=T; t++) {
    scanf(" %d %d", &N, &M);
    
    for(int i=0; i<M; i++) {
      bla tmp;
      scanf(" %lld %lld %lld", &tmp.o, &tmp.e, &tmp.p);
      blao[i] = tmp;
      blae[i] = tmp;
    }
    
    sort(blao, blao+M, sorto);
    sort(blae, blae+M, sorte);
    long long int cost = 0;
    int ptr = 0;
    for(int i=0; i < M; i++) {
      while(blao[i].o > blae[ptr].e) {
        while(blae[ptr].p != 0) {
          if(s.top().p == 0) s.pop();
          
          long long int p = min(s.top().p, blae[ptr].p);
          s.top().p -= p;
          blae[ptr].p -= p;
        
          //printf("o: %lld, e: %lld, p: %lld\n", s.top().o, blae[ptr].e, p);
          cost = (cost + ((calc(blae[ptr].o, blae[ptr].e) - calc(s.top().o, blae[ptr].e))) % P * p) % P;
        }
        ptr++;
      }
      
      s.push(blao[i]);
      
      /*while(blao[i].o >= blae[ptr].e) {
        while(blae[ptr].p != 0) {
          if(s.top().p == 0) s.pop();
          
          long long int p = min(s.top().p, blae[ptr].p);
          s.top().p -= p;
          blae[ptr].p -= p;
        
          //printf("o: %lld, e: %lld, p: %lld\n", s.top().o, blae[ptr].e, p);
          cost = (cost + ((calc(blae[ptr].o, blae[ptr].e) - calc(s.top().o, blae[ptr].e))) % P * p) % P;
        }
        ptr++;
      }*/
    }
    while(ptr < M) {
      while(blae[ptr].p != 0) {
        if(s.top().p == 0) s.pop();
        long long int p = min(s.top().p, blae[ptr].p);
        s.top().p -= p;
        blae[ptr].p -= p;
      
        //printf("o: %lld, e: %lld, p: %lld\n", s.top().o, blae[ptr].e, p);
        cost = (cost + ((calc(blae[ptr].o, blae[ptr].e) - calc(s.top().o, blae[ptr].e))) % P * p) % P;
      }
      ptr++;
    }
    
    printf("Case #%d: %lld\n", t, cost);
  }
  
}
