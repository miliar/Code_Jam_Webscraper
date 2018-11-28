#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;

long N, D;
long S[1000000], M[1000000];

struct Node {
  int parent;
  vector<Node*> children;
  int s;
  int idx;
  bool root;
  bool selected; // 現在有劫なノードか
  bool accessed;
  int memo;
};

int result =0 ;
int to[1000000];
bool operator<(const Node &a, const Node &b) {
  return a.s < b.s;
}
Node G[1000000];
bool check(Node &n, int first, int second) {
  if(n.selected) return true;
  if(n.accessed) return false;
  if(n.memo >= 0) return n.memo;
  if(!(first <= n.s && n.s <= second)) return false;
  return n.memo = check(G[to[n.parent]], first, second);
}
void dfs(Node &n, int first, int second) {
  if(n.selected) return ;
  if(first <= n.s && n.s <= second) {
    n.selected = n.accessed = true;
    result++;
    for(Node *m: n.children) {
      dfs(*m, first, second);
    }
  }
}

void clear(Node &n) {
  if(n.selected == false) return; // 選択されていなければ関係ない
  result--;
  n.selected = false;
  for(Node *m: n.children) {
    clear(*m);
  }
}

int check2(Node &n, int first, int second, bool ok = true) {
  ok &= first <= n.s && n.s <= second;
  if(ok != n.selected) {
    cout << n.idx << "," << first << "," << second << "," << n.selected << endl;
    cout << "FAILED" << endl;
    return false;
  }
  int cnt = 0;
  for(Node *m: n.children) {
    cnt += check2(*m, first, second, ok);
  }
  return cnt + ok;
}

int main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; tc++) {
    cin >> N >> D;
    long A_s, C_s, R_s;
    cin >> S[0] >> A_s >> C_s >> R_s;
    G[0].s = S[0];
    for(int i = 0; i <N; i++) {
      G[i].selected = false;
      G[i].children.clear();
      G[i].idx = i;
      G[i].accessed = false;
      G[i].memo = -1;
    }
    for(int i = 1; i < N; i++) {
      S[i] = ((long long)S[i - 1] * A_s + C_s) % R_s;
      G[i].s = S[i];
    }
    long A_m, C_m, R_m;
    cin >> M[0] >> A_m >> C_m >> R_m;
    for(int i = 1; i < N; i++) {
      M[i] = ((long long)M[i - 1] * A_m + C_m) % R_m;
    }
    for(int i = 1; i < N; i++) {
      M[i] %= i;
      G[i].parent = M[i];
    }
    for(int i = 1; i < N; i++) {
      G[i].root = false;
    }

    result = 0;
    G[0].root = true;
    sort(G, G + N);
    int root;
    for(int i = 0; i < N; i++) if(G[i].root) root = i;
    for(int i = 0; i < N; i++) S[i] = G[i].s;
    for(int i = 0; i < N; i++) {
    }
    for(int i = 0; i < N; i++) {
      to[G[i].idx] = i;
    }
    for(int i = 0; i < N; i++) {
      if(G[i].root) continue;
      G[to[G[i].parent]].children.push_back(&G[i]);
    }
    int answer = 0;
    int s2 = 0, f2 = 0;
    for(long first = G[root].s - D; first <= G[root].s; first++) {
      if(first == G[root].s - D) {
        // 初期設定
        dfs(G[root], first, first + D);
    
      }else {
        // 消えるものを探す
        for(;f2 < N && G[f2].s <= first - 1; f2++)
          if(G[f2].s == first - 1)clear(G[f2]);
        // 増えるものを探す
        for(;s2 < N && G[s2].s <= first + D; s2++){
          if(G[s2].selected == false && G[s2].s == first + D)
            if(check(G[s2], first, first + D)) {
              dfs(G[s2], first, first + D);
            }
        }
      }
      answer = max(answer, result);
 //     assert(check2(G[root],first, first + D) == result);
    }
    cout << "Case #" << tc << ": " << answer << endl;
  }

}
