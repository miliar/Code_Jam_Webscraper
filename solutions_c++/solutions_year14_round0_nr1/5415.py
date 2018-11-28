#include <iostream>
#include <vector>
#include <set>


using namespace std;

int main(void) {
  int T, p;
  cin >> T;
  for(int t=1; t <= T; t++) {
    int l;
    cin >> l;
    set<int> a, b;
    for(int i=0;i < 4;i++) {
      for(int j=0; j < 4; j++) {
	cin >> p;
	if(i+1==l) {
	  a.insert(p);
	}
      }
    }
    
    cin >> l;
    for(int i=0;i < 4;i++) {
      for(int j=0; j < 4; j++) {
	cin >> p;
	if(i+1==l) {
	  if(a.find(p) != a.end()) b.insert(p);
	}
      }
    }
    cout << "Case #" << t << ": ";
    if(b.size() == 1) {
      cout << *b.begin() << endl;
    }
    if(b.size() > 1) {
      cout << "Bad magician!" << endl;
    }
    if(b.size() == 0) {
      cout << "Volunteer cheated!" << endl; 
    }
    
  }
}