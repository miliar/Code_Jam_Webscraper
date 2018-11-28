#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <cmath>

int INF = 2147483647;
double INFD = 2147483647;

double PI = 3.14159265359;

using namespace std;

bool IsHappy(string& str) {
  int i = 0;
  while(i < str.size()) {
    if(str[i] == '-') {
      return false;
    }
    i++;
  }
  return true;
}

void FlipFromLastBlank(string& str) {
  int j = str.size();
  while(j) {
    j--;
    if(str[j] == '-') {
      break;
    }
  }
  int i = 0;
  while(i <= j) {
    str[i] = (str[i] == '-') ? '+' : '-';
    i++;
  }
}

int main() {
  int i = 0, t = 0;
  cin >> t;
  while(i < t) {
    string str;
    cin >> str;
    int count = 0;
    while(!IsHappy(str)) {
      count++;
      FlipFromLastBlank(str);
    }
    cout << "Case #" << ++i << ": ";
    cout << count << endl;
  }


  return 0;
}
