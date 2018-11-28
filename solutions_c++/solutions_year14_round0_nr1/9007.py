#include <iostream>
#include <set>
#include <vector>
#include <iostream>
#include <sstream>

std::vector<int> intersection(std::set<int> &a, std::set<int> &b) {
  std::vector<int> vec;
  std::set<int>::iterator a_it = a.begin();
  for (int i = 0; i < 4; i++) {
    if (b.find(*a_it) != b.end()) {
      vec.push_back(*a_it);
    }
    a_it++;
  }
  return vec;
}

void check(int a[][4], int b[][4], int x, int y, int case_num) {
  std::set<int> a_set; 
  std::set<int> b_set;

  for (int i = 0; i < 4; i++) {
    a_set.insert(a[x][i]);
    b_set.insert(b[y][i]);
  }

  std::vector<int> vec = intersection(a_set, b_set);
  if (vec.size() == 0) {
    std::cout << "Case #" << case_num << ": Volunteer cheated!" << std::endl;
  } else if (vec.size() == 1) {
    std::cout << "Case #" << case_num << ": " << vec[0] << std::endl;
  } else {
    std::cout << "Case #" << case_num << ": Bad magician!" << std::endl;
  }
}

int main(int argc, char** argv) {
  int cases = 0;

  std::string line;
  std::getline(std::cin, line);
  std::istringstream iss(line);
  iss >> cases;

  for (int case_id = 1; case_id < cases + 1; case_id++) {
    int x = 0;
    int y = 0;
    int a[4][4];
    int b[4][4];

    std::getline(std::cin, line);
    std::istringstream iss_a(line);
    iss_a >> x;
    for (int i = 0; i < 4; i++) {
      std::string line;
      std::getline(std::cin, line);
      std::istringstream iss(line);
      for (int j = 0; j < 4; j++) {
        iss >> a[i][j];
      }

    }

    std::getline(std::cin, line);
    std::istringstream iss_b(line);
    iss_b >> y;
    for (int i = 0; i < 4; i++) {
      std::string line;
      std::getline(std::cin, line);
      std::istringstream iss(line);
      for (int j = 0; j < 4; j++) {
        iss >> b[i][j];
      }
    }
    check(a, b, x - 1, y - 1, case_id);
  }
}
