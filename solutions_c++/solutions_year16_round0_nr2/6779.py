#include <my_epi/common.h>
#include <assert.h>

// return 0 if cannot have all the digits
int countNumFlips(const string& pancakes) {
  int i = 0;
  int num_flips = 0;
  if (pancakes[0] == '-') {
    ++num_flips;
    while (i < pancakes.length() && pancakes[i] == '-')
      ++i;
  }

  while (i < pancakes.length()) {
    while (i < pancakes.length() && pancakes[i] == '+')
      ++i;
    if (i == pancakes.length())
      break;
    num_flips += 2;
    while (i < pancakes.length() && pancakes[i] == '-')
      ++i;
    cout << num_flips << endl;
  }

  return num_flips;
}

void PerformTestCase(int test_case_num, ifstream *input_file, ofstream *output_file) {
  string pancakes;
  *input_file >> pancakes;

  string output_line = "Case #" + to_string(test_case_num) + ": ";
  output_line += to_string(countNumFlips(pancakes)) + "\n";

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
