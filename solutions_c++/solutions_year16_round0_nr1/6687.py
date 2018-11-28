#include <my_epi/common.h>
#include <assert.h>

void addDigits(long long num, unordered_set<int> *digits) {
  while (num && digits->size() < 10) {
    digits->emplace(num % 10);
    num /= 10;
  }
}

// return 0 if cannot have all the digits
long long countingSheep(int first_num) {
  if (first_num == 0)
    return 0;

  unordered_set<int> digits;

  int multiplier = 1;
  long long last_num = first_num;
  addDigits(last_num, &digits);

  while (digits.size() < 10) {
    ++multiplier;
    last_num = first_num * multiplier;
    addDigits(last_num, &digits);
  }

  return last_num;
}

void PerformTestCase(int test_case_num, ifstream *input_file, ofstream *output_file) {
  int first_num;
  *input_file >> first_num;

  string output_line = "Case #" + to_string(test_case_num) + ": ";
  string last_num = to_string(countingSheep(first_num));
  if (last_num == "0") 
    last_num = "INSOMNIA";
  output_line += last_num + "\n";

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
