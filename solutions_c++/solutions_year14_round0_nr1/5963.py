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

const int SIZE = 4;
typedef vector<vector<int> > Grid;

int findNumber(const Grid & grid1, const Grid & grid2, int r1, int r2);
void printGrid(const Grid & grid);

template <typename ElemType>
void readVector(string line, vector<ElemType> & x);


int main() {
  ifstream in;
  ofstream out;
  string line;

  int row1 = 0;
  int row2 = 0;

  in.open("A-small-attempt0.in");
  out.open("output.txt");

  getline(in, line);
  int tests = stoi(line);

  for (int i = 0; i < tests; ++i) {
    Grid grid1(SIZE);
    Grid grid2(SIZE);

    getline(in, line);
    row1 = stoi(line);
    for (int j = 0; j < SIZE; ++j) {
      getline(in, line);
      readVector(line, grid1[j]);
    }

    getline(in, line);
    row2 = stoi(line);
    for (int j = 0; j < SIZE; ++j) {
      getline(in, line);
      readVector(line, grid2[j]);
    }

    int result = findNumber(grid1, grid2, row1-1, row2-1);

    out << "Case #" << i+1 << ": ";
    switch (result) {
      case -1:
        out << "Bad Magician!" << endl;
        break;
      case 0:
        out << "Volunteer cheated!" << endl;
        break;
      default:
        out << result << endl;
        break;
    }

    grid1.clear();
    grid2.clear();
  }

  return 0;
}

int findNumber(const Grid & grid1, const Grid & grid2, int r1, int r2) {
  int result = 0;
  int count_numbers = 0;
  for (int i = 0; i < SIZE; ++i) {
    for (int j = 0; j < SIZE; ++j) {
      if (grid1[r1][i] == grid2[r2][j]) {
        ++count_numbers;
        result = grid1[r1][i];
        if (count_numbers > 1)
          result = -1;
      }
    }
  }

  return result;
}

template <typename ElemType>
void readVector(string line, vector<ElemType> & x) {
  string aux;

  for (int i = 0; i < line.length(); ++i) {
    if (line[i] != ' ') {
      aux += line[i];
    } else {
      x.push_back(stoi(aux));
      aux = "";
    }
  }

  if (aux.length()) x.push_back(stoi(aux));
}

//void printGrid(const Grid &grid) {
//  for (int i = 0; i < grid.size(); ++i) {
//    cout << "|";
//    for (int j = 0; j < grid[i].size(); ++j) {
//      cout << setw(3) << grid[i][j];
//      if (j < grid[i].size() - 1) cout << "  ";
//    }
//    cout << "|" << endl;
//  }
//}
