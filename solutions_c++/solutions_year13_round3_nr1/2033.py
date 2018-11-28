// mars.ma
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;


int main(void)
{
  int testcase;
  cin >> testcase;
  for (int tc = 1; tc <= testcase; tc++) {
    string name;
    cin >> name;
    int n;
    cin >> n;
    assert(0 < n);

    int nameSz = name.length();
    string::size_type found = name.find_first_of("aeiou");
    string::size_type head = 0;
    vector<pair<int, int> > cons;
    while (string::npos != found) {
      if (n <= found-head) {
        cons.push_back(pair<int, int>((int)head, (int)found-1));
      }

      head = found+1;
      found = name.find_first_of("aeiou", head);
    }

    if (n <= nameSz-head) {
      cons.push_back(pair<int, int>(head, nameSz-1));
    }


    long long result = 0;
    int conSz = cons.size();
/*
for (int c = 0; c < conSz; c++) {
cerr << name.substr(cons[c].first, cons[c].second-cons[c].first+1) << endl;
}
*/
    for (int i = 0; i <= nameSz-n; i++) {
      for (int j = i+n-1; j < nameSz; j++) {
        for (int c = 0; c < conSz; c++) {
          if (n <= min(cons[c].second, j)-max(cons[c].first, i)+1) {
            result++;
            break;
          }
        }
      }
    }

    cout << "Case #" << tc << ": " << result << endl;
  }

  return 0;
}

