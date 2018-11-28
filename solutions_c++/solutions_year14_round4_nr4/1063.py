#include <iostream>
#include <stdlib.h>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

int worst;
int counted;

struct Trie {
  int nodes;
  Trie() : nodes(1) {}
  void add(const char* s, map<char, void*>* node = NULL) {
    if (!*s) return;
    if (node == NULL) node = &root;
    map<char, void*>::iterator it = node->find(*s);
    if (it == node->end()) {
      (*node)[*s] = new map<char, void*>();
      it = node->find(*s);
      if (*s != '?') nodes++;
    }
    add(s + 1, (map<char,void*>*)it->second);
  }
  bool del(const char* s, map<char, void*>* node = NULL) {
    if (!*s) return node->size() == 0;
    if (node == NULL) node = &root;
    map<char, void*>::iterator it = node->find(*s);
    bool remove = del(s + 1, (map<char,void*>*)it->second);
    if (remove) {
      node->erase(it);
      if (*s != '?') nodes--;
    }
    return node->size() == 0;
  }
  int getNodes() { return (nodes == 1) ? 0 : nodes; }
  map<char, void*> root;
};

Trie* tries;

void solve(int M, int N, vector<string>& s, int level = 0) {
  if (level == s.size()) {
    int total = 0;
    for (int i = 0;i < N;i++) total += tries[i].getNodes();
    if (worst < total) {
      worst = total;
      counted = 0;
    }
    if (worst == total) counted++;
    return;
  }
  for (int i = 0;i < N;i++) {
     tries[i].add(s[level].c_str());
     solve(M, N, s, level + 1);
     tries[i].del(s[level].c_str());
  }
}


int main(int argc, char* argv[]) {
  int T;
  std::cin >> T;
  std::string s;
  for (int t = 0;t < T;t++) {
    int M, N;
    cin >> M >> N;
    tries = new Trie[N];
    std::vector<string> s;
    for (int i = 0;i < M;i++) { string st; std::cin >> st; st += '?'; s.push_back(st); }
    worst = 0;
    counted = 0;
    solve(M, N, s);
    cout << "Case #" << (t+1) << ": ";
    cout << worst << " " << counted;
    std::cout << endl;
  }
  return 0;
}

