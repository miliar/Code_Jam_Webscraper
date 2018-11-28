#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int c;
  cin >> c;
  string s;
  getline(cin, s);
  for(int i = 0; i < c; i++) {
    getline(cin, s);
    int length = s.length();
    istringstream iss(s);
    char word[length*2];
    int front = length;
    int back = length;
    iss >> word[front];
    char temp;
    while(iss >> temp) {
      if(temp >= word[front]) {
        front--;
        word[front] = temp;
      }else {
        back++;
        word[back] = temp;
      }
    }
    cout << "Case #" << i+1 << ": ";
    for(int j = front; j <= back; j++) {
      cout << word[j];
    }
    cout << endl;
  }
}
