#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>  
#include <climits>
#include <map>

using namespace std;

const char kInputFile[] = "input.txt";

string GetLine(ifstream& file) {
  string line;
  getline(file, line);
  return line;
}

map<vector<int>, int> solution_map;

vector<int> dynamic(const vector<int>& state, const int decision) {
  vector<int> next_state;
  if (decision < 1 || decision > state.back() - 1) {
    for (const int number : state) {
      if (number > 1) {
	next_state.emplace_back(number - 1);
      }
    }
  } else {
    for (int i = 0; i < state.size(); ++i) {
      if (i != state.size() - 1) {
	next_state.emplace_back(state[i]);
      } else {
	next_state.emplace_back(decision);
	next_state.emplace_back(state[i] - decision);
      }
    }
  }
  sort(next_state.begin(), next_state.end());
  return next_state;
}

int SolveImp(const vector<int>& state) {
  if (state.size() <= 0) return 0;
  if (solution_map.find(state) != solution_map.end()) {
    return solution_map[state];
  }
  int min = INT_MAX;
  for (int decision = 0 ; decision <= state.back() / 2; ++decision) {
    int current_result = SolveImp(dynamic(state, decision)) + 1;
    if (min > current_result) {
      min = current_result;
    }
  }
  solution_map[state] = min;
  return min;
}

int Solve(const vector<int>& initial_state) {
  solution_map.clear();
  return SolveImp(initial_state);
}

int main() {
  ifstream infile(kInputFile);
  int total_test_cases = stoi(GetLine(infile));

  for (int num_test_cases = 0; num_test_cases < total_test_cases;
       ++num_test_cases) {
    int num_non_empty_plate = 0;
    {
      stringstream ss(GetLine(infile));
      ss >> num_non_empty_plate;
    }

    vector<int> initial_state;
    {
      stringstream ss(GetLine(infile));
      for (int i = 0; i < num_non_empty_plate; ++i) {
	int number;
	ss >> number;
	initial_state.emplace_back(number);
      }
      sort(initial_state.begin(), initial_state.end());
    }

    int num_min = Solve(initial_state);
    cout << "Case #" << num_test_cases + 1 << ": " << num_min << endl;
  }

  infile.close();
  return 0;
}
