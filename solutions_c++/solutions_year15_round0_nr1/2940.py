#include <fstream>
#include <iostream>
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
  vector<size_t> arr;

  string input() {
    std::stringstream buf;
    buf << arr.size() - 1 << " ";
    for (auto i : arr) {
      buf << i;
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
  int num;
  fin >> num;

  vector<TestCase> res;
  for (int i = 0; i < num; ++i) {
    TestCase tc;
    tc.id = i+1;

    int max;
    fin >> max;
    char c;
    for (int j = 0; j <= max; ++j) {
      fin >> c;
      tc.arr.push_back(c - '0');
    }

    res.push_back(tc);
  }

  return res;
}

int solve(TestCase tc) {
  int res = 0;
  int standing = 0;
  for (int i = 0; i < tc.arr.size(); i++) {
    if (standing < i) {
      int dif = i - standing;
      res += dif;
      standing += dif;
    }
    standing += tc.arr[i];
  }
  return res;
}

int main() {
  cout << "Starting...\n";

  auto input = read();

  for (auto tc : input) {
    fout << tc.output(solve(tc)) << endl;
  }

  cout << "Done!\n";

  return 0;
}
