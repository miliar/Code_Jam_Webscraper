//
//  MagicTrick.cc
//  Google Code Jam Test
//
//  Created by Rafael Rabelo de Carvalho on 4/11/14.
//  Copyright (c) 2014 Rafael Rabelo de Carvalho. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
using namespace std;

template <typename ElemType>
void readVector(string line, vector<ElemType> & x);

template <typename ElemType>
void printGrid(const vector<ElemType> & x);


int main() {
  ifstream in;
  ofstream out;
  string line;

  double c = 0.0;
  double f = 0.0;
  double x = 0.0;
  double time = 0.0;

  in.open("B-large.in");
  out.open("output.txt");

  getline(in, line);
  int tests = stoi(line);

  for (int i = 0; i < tests; ++i) {
    vector<double> input;
    int count = 0;

    getline(in, line);
    readVector(line, input);
    c = input[0];
    f = input[1];
    x = input[2];
    time = x / 2;

    while (true) {
      double time2 = 0.0;
      for (int i = 0; i <= count; ++i) {
        time2 += c / (2 + i*f);
      }
      time2 += x / (2 + (count + 1) * f);

      if (time2 <= time)
        time = time2;
      else
        break;
      ++count;
    }

    double precision = time;
    count = 0;
    while (precision > 1) {
      precision /= 10;
      count += 1;
    }
    cout << "Case #" << i + 1 << ": " << setprecision(7+count) << time << endl;

  }
  return 0;
}

template <typename ElemType>
void readVector(string line, vector<ElemType> & x) {
  string aux;

  for (int i = 0; i < line.length(); ++i) {
    if (line[i] != ' ') {
      aux += line[i];
    } else {
      x.push_back(stod(aux));
      aux = "";
    }
  }

  if (aux.length()) x.push_back(stod(aux));
}

template <typename ElemType>
void printGrid(const vector<ElemType> & v) {
  cout << "[";
  for (int i = 0; i < v.size(); ++i) {
    cout << v[i];
    if (i < v.size()-1) cout << ", ";
  }
  cout << "]";
}