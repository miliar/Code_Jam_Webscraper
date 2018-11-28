#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef struct {
  vector<bool> bs;
  // int depth;
} node;

bool all(vector<bool>* bs) {
  for (int i = 0; i < (*bs).size(); i++) {
    if ((*bs)[i] == false) {
      return false;
    }
  }
  return true;
}

int sum(vector<bool>* bs) {
  int total = 0;
  for (int i = 0; i < (*bs).size(); i++) {
    total += (*bs)[i];
  }
  return total;
}

unsigned long long toULL(vector<bool>* bs) {
  unsigned long long total = 0;
  for (int i = 0; i < (*bs).size(); i++) {
    total |= (*bs)[i] << ((*bs).size() - i - 1);
  }
  cout << total << endl;
}

vector<bool>* flip(int n, vector<bool>* bs, vector<bool>* ds) {
  for (int i = 0; i < n; i++) {
    (*ds).push_back(!(*bs)[i]);
  }
  reverse((*ds).begin(), (*ds).end());
  for (int i = n; i < (*bs).size(); i++) {
    (*ds).push_back((*bs)[i]);
  }
  return ds;
}

void output(vector<bool>* bs) {
  for (int i = 0; i < (*bs).size(); i++) {
    cout << (*bs)[i];
  }
  cout << endl;
}

// int solve(vector<bool>* bs, vector< vector<bool> >* reached, int depth) {
//   if (all(bs)) return 0;
//   // if (depth > 2*(*bs).size() + 5) return 100;
//   vector< vector<bool> > dss;
//   vector<int> sizes;
//   for (int i = 1; i <= (*bs).size(); i++) {
//     vector<bool> ds;
//     flip(i, bs, &ds);
//     if (all(&ds)) return 1;
//     if (((find((*fss)).begin(), (*fss)).end(), ds) == (*fss)).end()))) {
//       output(&ds);
//       (*fss)).push_back(ds);
//       sizes.push_back(solve(&ds, fss, depth + 1));
//     }
//   }
//   if (sizes.empty()) return 100 ;
//   else return 1 + *min_element(sizes.begin(), sizes.end());
// }

int main() {
  ios::sync_with_stdio(false);

  int k;
  cin >> k;
  int m = k;

  cin.get();

  while (k--) {

    vector<bool> bs;

    char c;

    while ((c = cin.get()) != '\n') {
      if (c == '+') {
        bs.push_back(true);
      } else {
        bs.push_back(false);
      }
    }
    // vector<bool> ds;

    vector< vector<bool> > fss;
    fss.push_back(bs);

    bool found = false;
    // toULL(&bs);
    queue<vector<bool> > bss;
    bss.push(bs);

    int depth = 0;

    if (all(&bs)) {
      cout << "Case #" << m - k << ": 0\n";
      continue;
    }

    while (!found) {
      depth++;
      int l = bss.size();
      for (int i = 0; i < l; i++) {
        for (int i = 1; i <= bs.size(); i++) {
          vector<bool> ds;
          flip(i, &bss.front(), &ds);
          if (find(fss.begin(), fss.end(), ds) == fss.end()) {
            // output(&ds);
            if (all(&ds)) {
              cout << "Case #" << m - k << ": " << depth << endl;
              found = true;
              break;
            }
            fss.push_back(ds);
            // sizes.push_back(solve(&ds, fss, depth + 1));
            bss.push(ds);
          }
          if (found) break;
        }
        bss.pop();
      }
    }

  }
}
