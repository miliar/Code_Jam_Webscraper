/* Opgave: C */
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
#include <cstdint>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;
int N;
std::unordered_map<std::string, int> words;


std::set<int> ReadSentence() {
  std::string line, word;
  std::getline(cin, line);
  std::istringstream iss(line);
  std::set<int> ret;
  while(iss >> word) {
    auto it = words.find(word);
    if(it == words.end()) {
      int idx = words.size();
      words[word] = idx;
      ret.insert(idx);
    } else
      ret.insert(it->second);
  }
  return ret;
}

vector<vector<int>> eEdges, fEdges;
vector<int> eMatch, fMatch;
vector<int> fPrev;

void AddEdge(int e, int f) {
  bool eContains = false;
  for(auto v : eEdges[e])
    if(v == f)
      eContains = true;
  if(!eContains)  {
   // std::cerr << " add " << e << " " << f << "\n";
    eEdges[e].push_back(f);
    fEdges[f].push_back(e);
  }
}


bool Search(int& out) {
  for(auto& f : fPrev)
    f = -1;
  std::vector<bool> done(fMatch.size());
  
  std::queue<int> q;
  for(unsigned i = 0; i < eMatch.size(); ++i)
    if(eMatch[i] == -1)
      q.push(i);
  while(!q.empty()) {
    auto e = q.front();
    q.pop();
    for(auto f : eEdges[e]) {
      if(done[f])
        continue;
      done[f] = true;
      fPrev[f] = e;
      if(fMatch[f] < 0) {
        out = f;
        return true;
      }
      q.push(fMatch[f]);
    }
  }
  return false;
}
void doit(int testcase) {
  cin >> N;
  cin.get();
  words.clear();
  auto english = ReadSentence();
  auto french = ReadSentence();
  std::vector<set<int>> sentences;
  for(int i = 2; i < N; ++i)
    sentences.push_back(ReadSentence());
  
  eEdges.clear();
  fEdges.clear();
  eEdges.resize(words.size() + 2 * french.size());
  fEdges.resize(words.size() + 2 * english.size());
  
  int idx = 0;
  for(auto e : english) {
    AddEdge(e, words.size() + 2 * idx);
    AddEdge(e, words.size() + 2 * idx + 1);
    idx++;
  }
  idx = 0;
  for(auto f : french) {
    AddEdge(words.size() + 2 * idx, f);
    AddEdge(words.size() + 2 * idx + 1, f);
    idx++;
  }
  for(auto&& s : sentences) {
    for(auto e : s)
      for(auto f : s)
        AddEdge(e, f);
  }
  for(auto v : words)
    AddEdge(v.second, v.second);
  
  eMatch.clear();
  fMatch.clear();
  fPrev.clear();
  eMatch.resize(eEdges.size(), -1);
  fMatch.resize(fEdges.size(), -1);
  fPrev.resize(fEdges.size(), -1);
  
  int size = 0;
  for(;;) {
    int out;
    bool b = Search(out);
    if(!b)
      break;
    ++size;
   // std::cout << "match:\n";
    while(out >= 0) {
     // auto f = out;
      auto e = fPrev[out];
      //std::cout <<  " " << e << " " << f << "\n";
      fMatch[out] = e;
      auto outPrev = eMatch[e];
      eMatch[e] = out;
      out = outPrev;
    }
  }
  
  cout << "Case #" << testcase << ": " << (size - words.size()) << "\n";
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
    doit(i);
  return 0;
}
/* Opgave: C */
