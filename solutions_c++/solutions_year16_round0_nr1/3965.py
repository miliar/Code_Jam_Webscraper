#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int n;

int cal(int k) {
  int ans = -1;
  int m[10] = {0};
  int mp = 1;

  if(k == 0) return -1;

  for(int i = 0; i < 10; i++) {
    m[i] = 0;
  }

  while(true) {
    int newK = k * mp;

    while(newK > 0) {
      m[newK % 10] = 1;
      newK /= 10;
      cout << k << "," << newK << endl;
    }

    bool found = true;
    for(int i = 0; i < 10; i++) {
      if(m[i] == 0) {
        found = false;
        break;
      }
    }

    if(found) return k * mp;

    mp += 1;
  }
}

int main() {
  //ifstream in("in.txt");
  //ifstream in("A-small-attempt0.in");
  ifstream in("A-large.in");
  ofstream out("out.txt");
  in >> n;
  //cin >> n;

  int k;
  for(int i = 0; i < n; i++) {
    in >> k;
    //cin >> k;

    int ans = cal(k);
    if(ans < 0) {
      out << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
      //cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
    } else {
      out << "Case #" << i + 1 << ": " << ans << endl;
      //cout << "Case #" << i + 1 << ": " << ans << endl;
    }
  }

  return 0;
}