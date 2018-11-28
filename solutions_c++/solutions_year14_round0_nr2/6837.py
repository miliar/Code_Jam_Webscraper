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

long double processInput() {
  string var;
  cin >> var;
  long double C = stof(var);
  cin >> var;
  long double F = stof(var);
  cin >> var;
  long double X = stof(var);
  
  if (X <= C) {
    return X / 2.0;
  }
  
  long double cookie = 0.0;
  long double time = 0.0;
  long double rate = 2.0;
  while (cookie <= C) {
    time += (C - cookie) / rate;    
    cookie = C;
    if ((X - C) / rate > C / F) {
      rate += F;
      cookie = 0.0;
    } else {
      return time + (X - C) / rate;
    }
  }
}

int main() {
  string line;
  cin >> line;
  int cases = stoi(line);
  for (int i = 0; i < cases; ++i) {
    long double time = processInput();
    cout.precision(12);
    cout << "Case #" << i + 1 << ": " << time << endl;
  }
    
  return 0;
}