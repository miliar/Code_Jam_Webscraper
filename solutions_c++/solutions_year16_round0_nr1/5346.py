#include <array>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

template <typename T>
void format(int caseId, T &&str) {
  cout << "Case #" << ++caseId << ": " << str << endl;
}

bool cond(array<bool, 10> &data) {
  for (auto b : data)
    if (!b)
      return false;
  return true;
}

void update(array<bool, 10> &data, unsigned long num) {
  while (num) {
    data[num % 10] = true;
    num /= 10;
  }
}

void play(int caseId, unsigned long num) {
  array<bool, 10> data;
  for (auto &a : data)
    a = false;
  if (num == 0) {
    format(caseId, "INSOMNIA");
    return;
  }
  unsigned idx = 0;
  while (!cond(data)) {
    idx++;
    update(data, num * idx);
  }
  format(caseId, num * idx);
}
int main(int argc, char *argv[]) {
  if (argc == 1)
    return 1;
  ifstream f(argv[1]);

  int nLines;
  f >> nLines;
  for (int i = 0; i < nLines; ++i) {
    int num;
    f >> num;
    play(i, num);
  }
}
