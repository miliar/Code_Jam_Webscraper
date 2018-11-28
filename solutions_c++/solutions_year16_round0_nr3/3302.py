#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <cmath>
#include <algorithm>

#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long ll;

int mod(const int base, const int num, const int p, bool& exceed){
  int cur = 1;
  for(int i = 0; i < num; i++){
    cur *= base;
    if(cur >= p){
      exceed = true;
      cur %= p;
    }
  }
  return cur;
}

#define M (1<<14)
bool u[M];
//int s[128];
int ans[16];

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  memset(u, sizeof(u), 0);
  vector<int> primes;
  for(int i = 2; i < M; i++)
    if(!u[i]){
      if(i > 2)primes.push_back(i);
      for(int j = i + i ; j < M; j+=i)
        u[j] = true;
    }
  const int pn = (int)primes.size();
  //cout << pn << endl;

  srand(1);
  int T;
  cin >> T;
  for(int o = 1; o <= T; o++){
    printf("Case #%d:\n", o);
    int N, J;
    cin >> N >> J;
    vector<int> s(N);
    map< vector<int>, int > used;
    for(; J > 0;){
      s[0] = s[N-1] = 1;
      for(int i = 1; i < N - 1; i++)s[i] = rand() % 2;
      if(used.find(s) != used.end())
        continue;
      used[s] = 1;
      bool ok = true;
      for(int base = 2; base <= 10; base++){
        bool found = false;
        for(int i = 0; i < pn; i++){
          const int p = primes[i];
          int cur = 0;
          bool exceed = false;
          for(int i = N-1; i >= 0; i--){
            if(s[i] == 0)
              continue;
            cur += mod(base, N - i - 1, p, exceed);
            cur %= p;
          }
          if(cur == 0 && exceed){
            found = true;
            ans[base] = p;
          }
        }
        if(!found){
          ok = false;
          break;
        }
      }
      if(ok){
        J--;
        for(int i = 0; i < N; i++)
          printf("%d", s[i]);
        for(int b = 2; b <= 10; b++)
          printf(" %d", ans[b]);
        printf("\n");
      }
    }
  }

  return 0;
}
