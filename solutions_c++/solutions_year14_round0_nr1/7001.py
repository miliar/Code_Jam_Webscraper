#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

#define FOR(i, n) for(int i = 0 ; i < n ; ++i)
#define FORE(i, n) for(int i = 0 ; i <= n ; ++i)

struct problem {
  vector< vector<int> > matrix1, matrix2;
  int row1, row2;
};

struct answer {
  bool success;
  int number;
  string message;
};

vector<problem> readProblem() {
  ifstream fin("A-small-attempt0.in");
  vector<problem> problems;
  vector<int> temp;
  int t, n;

  fin >> t;

  FOR(i, t) {
    problem p;
    fin >> p.row1;

    FOR(j, 4) {
      temp.clear();
      FOR(k, 4) {
        fin >> n;
        temp.push_back(n);
      }
      p.matrix1.push_back(temp);
    }

    fin >> p.row2;

    FOR(j, 4) {
      temp.clear();
      FOR(k, 4) {
        fin >> n;
        temp.push_back(n);
      }
      p.matrix2.push_back(temp);
    }

    problems.push_back(p);
  }

  fin.close();
  return problems;
}

answer solve(problem p) {
  answer a;
  a.success = false;
  int found = 0;
  int number = -1;

  vector<int> line1, line2;

  line1 = p.matrix1[p.row1 - 1];
  line2 = p.matrix2[p.row2 - 1];
  FOR(i, 4) {
    if(find(line2.begin(), line2.end(), line1[i]) != line2.end()) {
      number = line1[i];
      ++found;
    }
  }

  if(found == 1) {
    a.success = true;
    a.number = number;
  } else if(found == 0) {
    a.message = "Volunteer cheated!";
  } else {
    a.message = "Bad magician!";
  }

  return a;
}


int main() {
  vector<problem> problems = readProblem();
  int size = problems.size();
  ofstream fout("A-small-attempt0.out");
  
  answer a;
  FOR(i, size) {
    a = solve(problems[i]);
    fout << "Case #" << i + 1 << ": ";

    if(a.success) {
      fout << a.number;
    } else {
      fout << a.message;
    }

    fout << endl;
  }

  fout.close();
}