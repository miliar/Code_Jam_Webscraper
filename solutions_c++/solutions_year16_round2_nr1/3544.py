#include <my_epi/common.h>
#include <assert.h>

using namespace std;

unordered_map<char, int> remain;

bool Exists(string digit_str) {
  for (char digit : digit_str) {
    if (remain[digit] == 0) {
      return false;
    }
  }
  return true;
}

void Reduce(string digit_str) {
  for (char digit : digit_str) {
    remain[digit]--;
    if (remain[digit] == 0)
      remain.erase(digit);
  }
}

unordered_map<string, string> kDigits{
  {"ZERO", "0"},
  {"ONE", "1"},
  {"TWO", "2"},
  {"THREE", "3"},
  {"FOUR", "4"},
  {"FIVE", "5"},
  {"SIX", "6"},
  {"SEVEN", "7"},
  {"EIGHT", "8"},
  {"NINE", "9"}
};

string solve(const string& str) {
  string result;
  remain.clear();
  for (char d : str)
    remain[d]++;

  for (auto it = kDigits.begin(); it != kDigits.end() && remain.size() > 0;) {
    string digit = it->first;
    printf("%s\n", digit.c_str());
    if (Exists(digit)) {
      Reduce(digit);
      result.append(it->second);
    } else {
      ++it;
    }
  }

  sort(result.begin(), result.end());

  return result;
}

void PerformTestCase(int test_case_num, ifstream *input_file, ofstream *output_file) {
  string str;
  *input_file >> str;

  string output_line = "Case #" + to_string(test_case_num) + ": ";
  string result = solve(str);
  output_line += result + "\n";

  *output_file << output_line;
  cout << output_line;
}

void ProcessInput(const string& input_file_name) {
  ifstream input_file(input_file_name);
  ofstream output_file(input_file_name + ".out");
  int num_test_cases;
  input_file >> num_test_cases;

  // skip the end of first line
  string tmp;
  getline(input_file, tmp);

  for (int i = 1; i <= num_test_cases; ++i)
    PerformTestCase(i, &input_file, &output_file);
  input_file.close();
  output_file.close();
}


int main(int argc, char **argv) {
  if (argc == 2)
    ProcessInput(string(argv[1]));
  else
    cout << "Please provide the input file" << endl;

	return 0;
}
