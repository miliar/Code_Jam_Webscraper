#include <bits/stdc++.h>
// Print containers, pairs and tuples with ostream
#include "prettyprint.h"


using namespace std;
/*
map<char, map<char, bool> > comp;
bool comp(int N, char a, char b){
  if(N==0) return a<b;
  if(comp[a].count(b)) return comp[a][b];
  pair<char, char> a1, b1;
  for(int i=0;i<2;++i){
    if(a=='S') {
      a1 = make_pair('S', 'P');
    } else if(a=='R'){
      a1 = make_pair('R', 'S');

    } else if(a=='P'){
      a1 = make_pair('P', 'R');
    }
    if(!comp(N-1,a1.first, a1.second)) swap(a1.second, a1.first);
    swap(a, b);
    swap(a1, b1);
  }
  return a1.first==b1.first ? comp(N-1, a1.second, b1.second) : comp(N-1, a1.first, b1.first);
}*/
/*
string unfold(int N, string const &cur){
  if(N==0) return cur;
  string rec(2*cur.size(), ' ');
  for(int i=0;i<(int)cur.size();++i){
    if(cur[i] == 'P'){
      rec[2*i]='P';
      rec[2*i+1] = 'R';
    } else if(cur[i] == 'S'){
      rec[2*i] = 'P';
      rec[2*i+1] = 'S';
    } else {
        rec[2*i] = 'S';
        rec[2*i+1] = 'R';
    }
    if(!comp(N-1, rec[2*i], rec[2*i+1])){
      swap(rec[2*i], rec[2*i+1]);
    }
  }
  return unfold(N-1, rec);
}*/
map<int, map<string, string> > cache;
string unfold2(int N, string const &cur){
  if(N==0) return cur;
  if(cache[N].count(cur))return cache[N][cur];
  string rec(2, ' ');
    if(cur[0] == 'P'){
      rec[0]='P';
      rec[1] = 'R';
    } else if(cur[0] == 'S'){
      rec[0] = 'P';
      rec[1] = 'S';
    } else {
        rec[0] = 'S';
        rec[1] = 'R';
    }
  string a = unfold2(N-1, string(1, rec[0]));
  string b = unfold2(N-1, string(1, rec[1]));
  if(a>b) swap(a, b);
  return cache[N][cur] = a+b;
}


bool simulate(string const& cur){
  int N=cur.size();
  if(N==1) return true;
  string rec;
  for(int i=0;i<N;i+=2){
    if(cur[i] == cur[i+1]) return false;
    if((cur[i] == 'R' && cur[i+1] == 'S') || (cur[i] == 'S' && cur[i+1] == 'R')) rec.push_back('R');
    if((cur[i] == 'P' && cur[i+1] == 'S') || (cur[i] == 'S' && cur[i+1] == 'P')) rec.push_back('S');
    if((cur[i] == 'P' && cur[i+1] == 'R') || (cur[i] == 'R' && cur[i+1] == 'P')) rec.push_back('P');
  }
  return simulate(rec);
}

string brute(int P, int R, int S){
  string ret;
  for(int i=0;i<P;++i){
    ret.push_back('P');
  }
    for(int i=0;i<R;++i){
    ret.push_back('R');
  }
  for(int i=0;i<S;++i){
    ret.push_back('S');
  }
  do{
    if(simulate(ret)) return ret;
  } while(next_permutation(ret.begin(), ret.end()));
  return "IMPOSSIBLE";
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin.tie(0);
    int T;
    cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #"<<cas<<": ";
      int N, P, R, S;
      cin >> N >> R >> P >> S;
      string a[3] = { unfold2(N, "P"), unfold2(N, "S"), unfold2(N, "R")};
      sort(a, a+3);
      int i;
      for(i=0;i<3;++i){
        int ps=0, rs=0, ss=0;
        for(auto &e:a[i]){
          if(e=='P')++ps;
          if(e=='R')++rs;
          if(e=='S')++ss;
        }
        if(ps==P && rs==R && ss == S) break;
      }
      cerr << brute(P, R, S) << "\n";
      if(i==3) cout <<"IMPOSSIBLE\n";
      else cout << a[i] << "\n";

    }
    return 0;
}
