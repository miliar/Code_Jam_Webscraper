#define NDEBUG
#include <cstdio>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;


int nstr, nservers;
vector<string> str;
vector<int> which;
int maxnodes, combs;

int count_nodes() {
  vector<set<string> > all_servers_prefixes(nservers);
  for (int i=0; i<nstr; ++i) {
    set<string> &prefixes = all_servers_prefixes[which[i]];
    for (int j=0; j<=(int)str[i].size(); ++j) {
      prefixes.insert(str[i].substr(0, j));
    }
  }

  int ans = 0;
  for (auto &S : all_servers_prefixes) {
    ans += S.size();
  }
  return ans;
}

void rek(int pos) {
  if (pos == nstr) {
    int nnodes = count_nodes();
    if (nnodes > maxnodes) {
      maxnodes = nnodes;
      combs = 1;
    } else if (nnodes == maxnodes) {
      ++combs;
    }
    return;
  }

  for (int i=0; i<nservers; ++i) {
    which[pos] = i;
    rek(pos+1);
  }
}

void solve1() {
  cin >> nstr >> nservers;
  str.resize(nstr);
  which.resize(nstr);
  for (string& s : str) {
    cin >> s;
  }
  maxnodes = 0;
  combs = 0;
  rek(0);
  printf("%d %d\n", maxnodes, combs);
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: ", tt);
    solve1();
  }
}
