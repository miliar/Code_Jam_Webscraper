#include <my_epi/common.h>
#include <assert.h>

using namespace std;

string solve(const string& str) {
  string result;
  result += str[0];
  for (int i = 1; i < str.length(); ++i) {
    if (str[i] >= result[0])
      result = str[i] + result;
    else
      result += str[i];
  }
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
