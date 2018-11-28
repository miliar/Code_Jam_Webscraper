#include <iostream>
#include <string>
#include <sstream>
#include <vector>

typedef std::string testcase_t;
typedef std::vector<testcase_t> testcase_container_t;

int char_parse_int(char c) {
  int num;
  std::istringstream iss(std::string(1, c));
  iss >> num;
  return num;
}

int minimum_invites(std::string in) {
  int people_standing = 0;
  int invites = 0;
  for (int i = 0; i < in.size(); ++i) {
    int current_shy_people = char_parse_int(in[i]);
    int invited = 0;
    if (people_standing < i) {
      invited = i - people_standing;
      invites += invited;
    }
    people_standing += invited + current_shy_people;
  }
  return invites;
}

// Program uses stdin to read test cases
// So we can just throw out the indicator for max shyness
testcase_container_t collect_test_cases() {
  int testcase_count;
  testcase_container_t testcases;
  testcase_t testcase;
  std::cin >> testcase_count;
  for (int i = 0; i < testcase_count; ++i) {
    std::cin >> testcase >> testcase; // throw out indicator for max shyness
    testcases.push_back(testcase);
  }
  return testcases;
}

void run_testcases(testcase_container_t testcases) {
  for (int i = 0; i < testcases.size(); ++i) {
    std::cout << "Case #" << i + 1 << ": "
              << minimum_invites(testcases[i])
              << std::endl;
  }
}

int main() {
  testcase_container_t testcases = collect_test_cases();
  run_testcases(testcases);
}
