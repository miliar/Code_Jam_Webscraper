#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int T;

int z,t;
int main() {
  cin >> T;
  for (int i=1; i<=T; i++) {
    vector <int> a, b;
    cin >> z;
    for (int q=1; q<=4; q++) {
      for (int w=0; w<4; w++) {
	cin >> t;
	if (q==z) a.push_back(t);
      }
    }
    cin >> z;
    for (int q=1; q<=4; q++) {
      for (int w=0; w<4; w++) {
	cin >> t;
	if (q==z) b.push_back(t);
      }
    }
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    vector<int> v(9);
    vector<int>::iterator it;
    it=std::set_intersection (a.begin(), a.end(), b.begin(), b.end(), v.begin());
   
    v.resize(it-v.begin());
    cout << "Case #"<< i << ": ";
    if (v.size()==0) {
      cout << "Volunteer cheated!" << endl;
    } else if (v.size()==1) {
      cout << v[0] << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}
