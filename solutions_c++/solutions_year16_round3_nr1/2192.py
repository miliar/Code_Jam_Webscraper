#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stack>
#include <fstream>
#include <unordered_map>

using namespace std;

int max_index(vector<int> v) {
  int index = 0;
  for (int i = 0; i < v.size(); i++) {
    if (v[i] > v[index])
      index = i;
  }
  return index;
}

bool isZero(vector<int> v) {
  for (int i = 0; i < v.size(); i++) {
    if (v[i] > 0)
      return false;
  }
  return true;
}

int find_sum(vector<int> v) {
  int sum = 0;
  for (int i = 0; i < v.size(); i++) {
    sum += v[i];
  }
  return sum;
}

void ans(vector<int> v) {
  if (isZero(v)) {
    cout << "";
    return;
  }
  while (!isZero(v)) {
    int max1 = max_index(v);
    v[max1]--;
    cout << (char)(max1 + 'A');
    if (isZero(v)) {
      return;
    }
    if (find_sum(v) != 2) {
      int max2 = max_index(v);
      v[max2]--;
      cout << (char)(max2 + 'A');
      if (isZero(v)) {
        return;
      }
    }

    cout << " ";
  }

}

int main() {
  ifstream cin("/Users/qasimzeeshan/Desktop/A-small-attempt1.in.txt");
  int T;
  cin >> T;
  int i = 1;
  while (T--)
  {
    vector<int> v;
    int n;
    cin >> n;
    while (n--) {
      int k;
      cin >> k;
      v.push_back(k);
    }
    cout << "Case #" << i << ":" << " ";
    ans(v);
    cout << endl;
    i ++;
  }
}
