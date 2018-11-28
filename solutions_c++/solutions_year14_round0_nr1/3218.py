#include <iostream>
#include <set>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int case_num = 1; case_num <= T; ++case_num) {
    int ch;
    set<int> ans;
    cin >> ch;
    for(int i = 1; i <= 4; ++i) {
      for(int j = 1; j <= 4; ++j) {
        int z;
        cin >> z;
        if(i == ch) ans.insert(z);
      }
    }

    cin >> ch;
    for(int i = 1; i <= 4; ++i) {
      for(int j = 1; j <= 4; ++j) {
        int z;
        cin >> z;
        if(i != ch) ans.erase(z);
      }
    }
    cout << "Case #" << case_num << ": ";
    switch( ans.size() ) {
      case 0:   cout << "Volunteer cheated!" << endl; break;
      case 1:   cout << *ans.begin() << endl; break;
      default:  cout << "Bad magician!" << endl; break;
    }
  }
  return 0;
}

