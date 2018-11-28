#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <queue>

using namespace std;

int main(){
  int T,res;
  char c;
  queue<pair<vector<bool>, int> > pancakes;
  pair<vector<bool>, int> curr, new_curr;
  set<vector<bool> > seen;
  bool ok;

  scanf("%d",&T);

  for (int t=1; t<=T; t++) {
    while (!pancakes.empty()) {
      pancakes.pop();
    }
    seen.clear();

    c=getchar();
    while (c!='-' && c!='+') {
      c=getchar();
    }

    curr.first.clear();
    curr.second = 0;
    while (c=='-' || c=='+') {
      if (c=='+') {
        curr.first.push_back(1);
      } else {
        curr.first.push_back(0);
      }
      c=getchar();
    }

    pancakes.push(curr);

    res = -1;
    while (res == -1) {
      curr = pancakes.front();
      pancakes.pop();

      /*for (int i=0; i<curr.first.size(); i++) {
        printf("%c",curr.first[i]?'+':'-');
      } printf("\n");*/

      ok = 1;
      for (int i=0; i<curr.first.size(); i++) {
        if (!curr.first[i]) {
          ok=0;
        }
      }
      if (ok) {
        res = curr.second;
        break;
      }

      for (int i=0; i<curr.first.size(); i++) {
        new_curr.second = curr.second+1;
        new_curr.first.resize(curr.first.size());
        for (int k=0; k<new_curr.first.size(); k++) {
          if (k <= i) {
            new_curr.first[k] = !curr.first[i-k];
          } else {
            new_curr.first[k] = curr.first[k];
          }
        }
        if (seen.find(new_curr.first) == seen.end()) {
          seen.insert(new_curr.first);
          pancakes.push(new_curr);
        }
      }
    }

    printf("Case #%d: %d\n",t,res);
  }

  return 0;
}
