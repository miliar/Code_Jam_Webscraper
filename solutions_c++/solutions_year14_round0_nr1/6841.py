//
//  Q1.cpp
//  
//
//  Created by Alan Long on 14-01-18.
//  Copyright 2014 UBC. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

int processInput() {
  string line;
  cin >> line;
  int first = stoi(line);
  int a[16];
  for (int i = 0; i < 16; ++i) {
    cin >> line;
    a[i] = stoi(line);
  }
  cin >> line;
  int second = stoi(line);
  int b[16];
  for (int i = 0; i < 16; ++i) {
    cin >> line;
    b[i] = stoi(line);
  }
  int a_start = 4 * (first - 1);
  int b_start = 4 * (second - 1);
  int dup = 0;
  int value = 0;
  for (int i = a_start; i < a_start + 4; ++i) {
    for (int j = b_start; j < b_start + 4; ++j) {
      if (a[i] == b[j]) {
        dup++;
        value = a[i];
      }
    }
  }
  if (dup == 1) {
    return value;
  } else if (dup == 0) {
    return -2;
  } else {
    return -1;
  }
}

int main() {
  string line;
  cin >> line;
  int cases = stoi(line);
  for (int i = 0; i < cases; ++i) {
    int code = processInput();
    switch (code) {
      case -1:
        cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
        break;
      case -2:
        cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
        break;
      default:
        cout << "Case #" << i + 1 << ": " << code << endl;
        break;
    }
  }
    
  return 0;
}