#include <my_epi/common.h>
#include <assert.h>
#include <sstream>

using namespace std;

unordered_map<char, int> remain;


string solve(priority_queue<pair<int, char>>& senators) {
  ostringstream output;
  while (!senators.empty()) {
    // always remove the top
    auto top = senators.top();
    senators.pop();
    output << " " << top.second;
    top.first--;

    // top.first was 1
    if (top.first == 0) {
      if (senators.size() % 2) {
        output << senators.top().second;
        senators.pop(); // the top will be 0
      }

      continue;
    }

    senators.emplace(top);

    // top.first was >= 2
    auto second_top = senators.top();
    if (second_top.first >= 2 || senators.size() % 2 == 1) {// if even senators remain, do nothing
      senators.pop();
      output << second_top.second;
      second_top.first--;
      if (second_top.first > 0)
        senators.emplace(second_top);
    }
  }

  return output.str();
}

void PerformTestCase(int test_case_num, ifstream *input_file, ofstream *output_file) {
  int num_parties;
  *input_file >> num_parties;
  priority_queue<pair<int, char>> senator_map;
  for (int i = 0; i < num_parties; ++i) {
    int num_senator;
    *input_file >> num_senator;
    cout << num_senator << endl;
    senator_map.emplace(num_senator, char('A' + i));
  }

  string output_line = "Case #" + to_string(test_case_num) + ":";
  string result = solve(senator_map);
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



    //for (auto it = senator_map.rbegin(); it != senator_map.rend(); ++it) {
      //output += to_string(it->second) + ":" + to_string(it->first) + " ";
