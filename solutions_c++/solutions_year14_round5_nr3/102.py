#include <queue>
#include <numeric>
#include <cstring>
#include <iostream>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
#include <set>

inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int t[15];
int v[15];
int n;
const int E = 0;
const int L = 1;
multiset<int> a;
multiset<int> b;

int inf = 1000000;

template<class T>
void erase(multiset<T> &s, T v){
  s.erase(s.find(v));
}

template<class T>
void insert(multiset<T> &s, T v){
  s.insert(v);
}

int solve(int pos){
  /*
  printf("%d: ", pos);
  printf("("); for(int aa : a) printf("%d ", aa); printf(") ");
  printf("("); for(int bb : b) printf("%d ", bb); printf(")\n");
  */
  if(pos == n){
    return b.size();
  }

  const int p = v[pos];
  int ret = inf;
  if(t[pos] == E){
    if(p == 0){
      const set<int> cand(a.begin(), a.end());
      for(const int c : cand){
	erase(a, c);
	insert(b, c);
	ret = min(ret, solve(pos + 1));
	erase(b, c);
	insert(a, c);
      }
      insert(b, 0);
      ret = min(ret, solve(pos + 1));
      erase(b, 0);
    }else{
      if(b.count(p)) return inf;

      const bool f = a.count(p);
      if(f) erase(a, p);
      insert(b, p);
      ret = min(ret, solve(pos + 1));
      erase(b, p);
      if(f) insert(a, p);

      if(a.count(0)){
	erase(a, 0);
	insert(b, p);
	ret = min(ret, solve(pos + 1));
	erase(b, p);
        insert(a, 0);
      }
    }
  }else /* L */{
    if(p == 0){
      const set<int> cand(b.begin(), b.end());
      for(const int c : cand){
	erase(b, c);
	insert(a, c);
	ret = min(ret, solve(pos + 1));
	erase(a, c);
	insert(b, c);
      }
      insert(a, 0);
      ret = min(ret, solve(pos + 1));
      erase(a, 0);
    }else{
      if(a.count(p)) return inf;

      const bool f = b.count(p);
      if(f) erase(b, p);
      insert(a, p);
      ret = min(ret, solve(pos + 1));
      erase(a, p);
      if(f) insert(b, p);

      if(b.count(0)){
	erase(b, 0);
	insert(a, p);
	ret = min(ret, solve(pos + 1));
	erase(a, p);
        insert(b, 0);
      }
    }
  }

  return ret;
}

void process(){
  n = getInt();
  REP(i,n){
    char s[2];
    scanf("%s", s);
    t[i] = s[0] == 'E' ? E : L;
    v[i] = getInt();
  }

  a.clear();
  b.clear();
  const int ans = solve(0);

  if(ans == inf) puts("CRIME TIME");
  else printf("%d\n", ans);
}

int main(){
  const int t = getInt();
  REP(i,t){
    printf("Case %d: ", i + 1);
    process();
  }
  return 0;
}
