#include <iostream>
#include <vector>
#include <queue>

struct Party {
  Party(int _party, int _members) :
      party(_party), members(_members) {}

  bool operator < (const Party& other) const {
    return members < other.members;
  }

  int party, members;
};

struct Answer {

  Answer() {}

  Answer(const std::vector<char>& _answer) : answer(_answer) {}

  std::vector<char> answer;
};

bool not_finish(const std::vector<int>& p) {
  for (int i = 0; i < p.size(); ++i) {
    if (p[i] > 0) {
      return true;
    }
  }

  return false;
}

bool one_senator(int pos, std::vector<int>& p) {
  int n = p.size();
  p[pos]--;

  int sum = 0;
  int max = 0;

  for (int i = 0; i < n; ++i) {
    sum += p[i];
    max = std::max(max, p[i]);
  }

  p[pos]++;
  return  (2 * max <= sum);
}

bool two_senators(int pos1, int pos2, std::vector<int>& p) {
  int n = p.size();
  p[pos1]--;
  p[pos2]--;

  int sum = 0;
  int max = 0;

  for (int i = 0; i < n; ++i) {
    sum += p[i];
    max = std::max(max, p[i]);
  }

  p[pos1]++;
  p[pos2]++;
  return  (2 * max <= sum);
}

void taskA() {
  int t = 0;
  std::cin >> t;

  for (int test = 0; test < t; ++test) {

    int n = 0;
    std::cin >> n;

    std::vector<int> p(n);
    for (int i = 0; i < n; ++i) {
      std::cin >> p[i];
    }

    std::vector<Answer> answer;

    while (not_finish(p)) {
      Answer current_answer;

      bool f = false;

      // One senator
      for (int i = 0; i < n; ++i) {
        if (one_senator(i, p)) {
          p[i]--;
          current_answer.answer.push_back((char)(i + 'A'));
          f = true;
          break;
        }
      }

      if (!f) {
        // Two senators
        for (int i = 0; i < n; ++i) {
          for (int j = i; j < n; ++j) {
            if (two_senators(i, j, p)) {
              p[i]--;
              p[j]--;
              current_answer.answer.push_back((char)(i + 'A'));
              current_answer.answer.push_back((char)(j + 'A'));
              break;
            }
          }
        }
      }

      answer.push_back(current_answer);
    }

    std::cout << "Case #" << (test + 1) << ": ";
    for (int i = 0; i < answer.size(); ++i) {
      for (int j = 0; j < answer[i].answer.size(); ++j) {
        std::cout << answer[i].answer[j];
      }
      std::cout << " ";
    }
    std::cout << std::endl;
  }
}

int main() {
  taskA();
  return 0;
}