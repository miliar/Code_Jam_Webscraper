#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Party {
  char name;
  int number;
};

void print(vector<Party>& v) {
  cout << endl << "///";
  for(Party& p : v) {
    cout << p.name << p.number << " ";
  }
  cout << endl;
}

int main() {
  int T, N, Pi;
  cin >> T;

  auto cmp = [](Party left, Party right) { return left.number > right.number; };

  for(int k=1; k<=T; ++k) {
    vector<Party> v;
    cin >> N;
    for (int i=0; i<N; ++i) {
      cin >> Pi;
      v.push_back(Party { .name = (char)('A'+i), .number = Pi });
    }
    cout << "Case #" << k << ":";
    while(1) {
      sort(v.begin(), v.end(), cmp);
      if (v[0].number == 0) break;
      if (v.size() == 3 && all_of(v.cbegin(), v.cend(), [](const Party& p){ return p.number == 1; })) {
        cout << " " << v[0].name << " " << v[1].name << v[2].name;
        break;
      } else if (v[0].number == v[1].number) {
        v[0].number--;
        v[1].number--;
        cout << " " << v[0].name << v[1].name;
      } else {
        v[0].number--;
        cout << " " << v[0].name;
      }
      
      //print(v);
    }
    cout << endl;

  }
  return 0;
}
