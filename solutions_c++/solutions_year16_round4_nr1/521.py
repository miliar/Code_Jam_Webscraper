#include <iostream>
#include <string>

std::string solve(int n, int r, int p, int s) {
  if (n == 0) {
    if (r != 0) {
      return "R";
    } else if (p != 0) {
      return "P";
    } else {
      return "S";
    }
  }
  int a2 = p + r - s;
  int b2 = p - r + s;
  int c2 = r + s - p;
  if (a2 % 2 != 0 || b2 % 2 != 0 || c2 % 2 != 0 ||
      a2 < 0 || b2 < 0 || c2 < 0) {
    return "";
  }
  int a = a2 / 2, b = b2 / 2, c = c2 / 2;
  std::string old_result = solve(n - 1, b, a, c);
  if (old_result.length() == 0) {
    return "";
  }
  std::string result(old_result.length() * 2, ' ');
  for (int i = 0; i < old_result.length(); ++i) {
    if (old_result[i] == 'R') {
      result[i * 2] = 'P';
      result[i * 2 + 1] = 'S';
    }
    if (old_result[i] == 'P') {
      result[i * 2] = 'P';
      result[i * 2 + 1] = 'R';
    }
    if (old_result[i] == 'S') {
      result[i * 2] = 'R';
      result[i * 2 + 1] = 'S';
    }
  }
  return result;
}

void sort(std::string& str, int left, int right, int level = 1) {
  if (left == right) {
    return;
  }
  int middle = (left + right) / 2;
  sort(str, left, middle, level + 1);
  sort(str, middle + 1, right, level + 1);
  bool swap = false;
  for (int i = left; i <= middle; ++i) {
    if (str[i] > str[middle + i - left]) {
      swap = true;
      break;
    } else if (str[i] < str[middle + i - left]) {
      break;
    }
  }
  if (swap) {
    for (int i = left; i <= middle; ++i) {
      std::swap(str[i], str[middle + i - left]);
    }
  }
}

int main() {
  int number_of_tests;
  std::cin >> number_of_tests;
  for (int test_index = 0; test_index < number_of_tests; ++test_index) {
    int n, r, p, s;
    std::cin >> n >> r >> p >> s;
    std::string result = solve(n, r, p, s);
    if (result.empty()) {
      result = "IMPOSSIBLE";
    } else {
      sort(result, 0, result.length() - 1);
    }
    std::cout << "Case #" << test_index + 1 << ": " << result << std::endl;
  }
  return 0;
}
