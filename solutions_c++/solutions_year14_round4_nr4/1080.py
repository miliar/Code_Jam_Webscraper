#include <bits/stdc++.h>
using namespace std;

struct Node {
  int next[26];
  Node() {
    fill(next, next+26, -1);
  }
};

int getTrie(const vector<string> &v) {
  vector<Node> nodes;
  nodes.push_back(Node());
  int root = 0;
  for(int i = 0; i < v.size(); ++i) {
    int p = root;
    for(int j = 0; j < v[i].size(); ++j) {
      if(nodes[p].next[v[i][j]-'A'] == -1) {
        nodes[p].next[v[i][j]-'A'] = nodes.size();
        nodes.push_back(Node());
      }
      p = nodes[p].next[v[i][j]-'A'];
    }
  }
  return nodes.size();
}

int maxi, num;

void rec(vector<string> &S, int k, vector<vector<string> > &v) {
  if(k == S.size()) {
    int sum = 0;
    for(int i = 0; i < v.size(); ++i) {
      if(v[i].empty()) return;
      sum += getTrie(v[i]);
    }
    if(sum == maxi) {
      ++num;
    } else if(sum > maxi) {
      maxi = sum;
      num = 1;
    }
    return;
  }
  for(int i = 0; i < v.size(); ++i) {
    v[i].push_back(S[k]);
    rec(S, k+1, v);
    v[i].pop_back();
  }
}

int main() {
  for(int Tc, tc = (bool)(cin >> Tc); tc <= Tc; ++tc) {
    cout << "Case #" << tc << ": ";
    int N, M;
    cin >> M >> N;
    vector<string> S(M);
    for(int i = 0; i < M; ++i) cin >> S[i];
    vector<vector<string> > v(N);
    maxi = -1;
    rec(S, 0, v);
    cout << maxi << " " << num << endl;
  }
  return 0;
}
