#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

const char kInputFile[] = "input.txt";

string GetLine(ifstream& file) {
  string line;
  getline(file, line);
  return line;
}

int Solve(const vector<int>& shyness_info) {
  int num_standing = 0;
  int num_friend = 0;
  for (int shyness = 0; shyness < shyness_info.size(); ++shyness) {
    int new_friend = 0;
    if (shyness > num_standing) {
      new_friend = (shyness - num_standing);
    }
    num_friend += new_friend;
    num_standing += (shyness_info[shyness] + new_friend);
  }
  return num_friend;
}

int main() {
  ifstream infile(kInputFile);
  int total_test_cases = stoi(GetLine(infile));

  for (int num_test_cases = 0; num_test_cases < total_test_cases;
       ++num_test_cases) {
    stringstream ss(GetLine(infile));
    int max_shyness = 0;
    ss >> max_shyness;
    string shyness_info_in_string;
    ss >> shyness_info_in_string;
    vector<int> shyness_info(max_shyness + 1);
    for (int i = 0; i <= max_shyness; ++i) {
      shyness_info[i] = shyness_info_in_string.c_str()[i] - '0';
    }
    int num_new_friends = Solve(shyness_info);
    cout << "Case #" << num_test_cases + 1 << ": " << num_new_friends << endl;
  }

  infile.close();
  return 0;
}
