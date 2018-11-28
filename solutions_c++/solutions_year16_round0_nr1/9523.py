#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

int main() {
  //ifstream ifile("sheep.txt");
  //ofstream ofile("sheep.o");
  int buffer;
  int lines;
  cin >> lines;
  for (int k=1; k<=lines; k++) {
    cin >> buffer;
    int n = buffer;
    cout << "Case #" << k <<": ";
    set<int> digits;
    for(int i=1; i<=100; i++) {
      string number = to_string(n*i);
      for(int j=0; j<number.length(); j++) {
        digits.insert((int)(number[j]));
      }
      if (digits.size() == 10) {
        cout << n*i << endl;
        break;
      }
    }
    if (digits.size() < 10) {
      cout << "INSOMNIA" << endl;
    }
  }
}
