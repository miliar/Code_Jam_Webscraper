#include <algorithm>
#include <fstream>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

const string fileName = "large";
ifstream fin (fileName + ".in");
ofstream fout(fileName + ".out");

struct TestCase {
  size_t id;
  vector<int> arr;

  string input() {
    std::stringstream buf;
    buf << arr.size() << endl;
    for (auto i : arr) {
      buf << i << " ";
    }
    buf << endl;
    return buf.str();
  }
  string output(int result) {
    std::stringstream buf;
    buf << "Case #" << id << ": " << result;
    return buf.str();
  }
};

vector<TestCase> read() {
  vector<TestCase> vec;

  // reads input
  int numTestCases;
  fin >> numTestCases;
  for (int i = 0; i < numTestCases; ++i) {
    TestCase tc;
    tc.id = i+1;

    int num;
    fin >> num;
    for (int j = 0; j < num; ++j) {
      int tmp;
      fin >> tmp;
      tc.arr.push_back(tmp);
    }

    vec.push_back(tc);
  }

  return vec;
}

int solve(TestCase& tc) {
  int nMin = 1;
  int nMax = std::numeric_limits<int>::min(); 
  for (int i = 0; i < tc.arr.size(); ++i) {
    nMax = std::max(nMax, tc.arr[i]);
  }

  int bestSol = std::numeric_limits<int>::max();

  for (int n = nMin; n <= nMax; n++) {
    int sol = n;
    for (int i = 0; i < tc.arr.size(); ++i) {
      if (tc.arr[i] > n) {
        int panToRemove = tc.arr[i] - n;
        int moves = panToRemove / n;
        if ((panToRemove % n) > 0) {
          moves++;
        }

        sol += moves;
      }
    }
    bestSol = std::min(bestSol, sol);
  }

  return bestSol;
}

int main() {
  // reads input
  auto vec = read();

  // outputs input (just to check).
//  for (auto& tc : vec) {
//    cout << tc.input();
//  }

  // solves and writes solution.
  for (auto& tc : vec) {
    int sol = solve(tc);
    fout << tc.output(sol) << endl;
  }

  return 0;
}
