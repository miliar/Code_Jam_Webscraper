#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#include <map>
#include <iostream>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

vector<string> s;
vector<map<string, int> > server;

int worst = 0;
int cnt = 0;

int getNum(){
  int ret = 0;
  REP(i,server.size()){
    // printf("server%d: ", i);
    FOR(it, server[i]){
      // if(it->second > 0) printf("\"%s\" ", it->first.c_str());
      if(it->second > 0) ret++;
    }
    // puts("");
  }
  //printf("=> %d\n", ret);
  // puts("");
  return ret;
}

void solve(int pos){
  if(pos == (int)s.size()){
    const int num = getNum();
    if(num > worst){
      worst = num;
      cnt = 0;
    }
    if(num == worst) cnt++;
  }else{
    REP(i,server.size()){
      const string &str = s[pos];

      REP(j,str.size()+1)
	server[i][str.substr(0, j)]++;

      solve(pos + 1);

      REP(j,str.size()+1)
	server[i][str.substr(0, j)]--;
    }
  }
}

int main(){
  const int T = getInt();

  REP(cc, T){
    const int m = getInt();
    const int n = getInt();

    s = vector<string>(m);
    server = vector<map<string, int> >(n);

    REP(i,m) cin >> s[i];

    worst = -1;
    cnt = 0;

    solve(0);
    printf("Case #%d: %d %d\n", cc + 1, worst, cnt);
  }
}
