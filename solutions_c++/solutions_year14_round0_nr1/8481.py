#include <iostream>
#include <set>

#define ROWS 4
#define COLS 4

int main(int argc, char* argv[]) {
  int test_cases = 0;
  std::cin >> test_cases;
  for (int t = 0;t < test_cases;t++) {
    int a1 = 0, a2 = 0;
    int* c1 = new int[ROWS * COLS];
    int* c2 = new int[ROWS * COLS];
    std::cin >> a1; a1--;
    for (int i = 0;i < ROWS * COLS;i++) std::cin >> c1[i];
    std::cin >> a2; a2--;
    for (int i = 0;i < ROWS * COLS;i++) std::cin >> c2[i];
    std::set<int> s1, s2;
    for (int i = 0;i < COLS;i++) s1.insert(c1[a1 * COLS + i]);
    for (int i = 0;i < COLS;i++) s2.insert(c2[a2 * COLS + i]);
    std::set<int> s;
    set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(), std::inserter(s,s.begin()));
    std::cout << "Case #" << (t+1) << ": ";
    if (s.size() == 0) std::cout << "Volunteer cheated!";
    if (s.size() == 1) std::cout << *s.begin();
    if (s.size() >  1) std::cout << "Bad magician!";
    std::cout << std::endl;
    delete [] c1;
    delete [] c2;
  }
}

