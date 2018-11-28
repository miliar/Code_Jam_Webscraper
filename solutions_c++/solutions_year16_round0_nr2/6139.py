#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>

namespace TaskA {

  std::set<int> set_of_digits;

  void add_digits(long long number) {
    while (number > 0) {
      set_of_digits.insert(number % 10);
      number /= 10;
    }
  }

  void taskA() {

    int t = 0;
    std::cin >> t;

    for (int i = 0; i < t; ++i) {
      set_of_digits.clear();

      int num = 0;
      std::cin >> num;

      bool f = false;

      for (int j = 1; j < 2000000; ++j) {
        add_digits(static_cast<long long>(j) * static_cast<long long>(num));

        if (set_of_digits.size() == 10) {
          f = true;
          std::cout << "Case #" << (i + 1) << ": " << static_cast<long long>(j) * static_cast<long long>(num) << std::endl;
          break;
        }
      }

      if (!f) {
        std::cout << "Case #" << (i + 1) << ": " << "INSOMNIA" << std::endl;
      }
    }

  }

}

namespace TaskB {

  const int INF = static_cast<int>(1e9);

  void makeBinary(std::string *s) {
    for (int i = 0; i < s->length(); ++i) {
      if ((*s)[i] == '-') {
        (*s)[i] = '0';
      } else if ((*s)[i] == '+') {
        (*s)[i] = '1';
      }
    }
  }

  int binaryToInteger(const std::string& s) {
    int res = 0;

    for (int i = 0; i < s.length(); ++i) {
      res = 2 * res + (s[i] - '0');
    }

    return res;
  }

  std::string integerToBinary(int num, unsigned long size) {
    std::string res = "";
    int it = 0;
    while (num > 0) {
      res += (num % 2 + '0');
      num /= 2;
      it++;
    }

    while (it < size) {
      res += '0';
      it++;
    }

    std::reverse(res.begin(), res.end());
    return res;
  }

  int pow(int a, unsigned long n) {
    if (n == 0) {
      return 1;
    } else if (n % 2 == 1) {
      return a * pow(a, n - 1);
    } else {
      int d = pow(a, n / 2);
      return d * d;
    }
  }

  void next(const std::string& example, std::string *s, int shift) {
    *s = example;

    char left = '0', right = '1';
    for (int i = 0; i < shift / 2; ++i) {
      left = (*s)[i];
      right = (*s)[shift - 1 - i];

      (*s)[i] = (right == '0') ? '1' : '0';
      (*s)[shift - 1 - i] = (left == '1') ? '0' : '1';
    }

    if (shift % 2 == 1) {
      (*s)[shift / 2] = (*s)[shift / 2] == '1' ? '0' : '1';
    }
  }

  std::string get_ans(unsigned long size) {
    return std::string(size, '1');
  }

  int bfs(const std::string& s) {

    std::vector<int> dist(pow(2, s.length()), INF);
    std::queue<int> queue;

    int start = binaryToInteger(s);
    dist[start] = 0;
    queue.push(start);

    std::string ans = get_ans(s.length());

    while (!queue.empty()) {

      int curr_num = queue.front();
      queue.pop();

      std::string curr = integerToBinary(curr_num, s.length());

      if (curr == ans) {
        return dist[curr_num];
      }

      int tmp_num = 0;
      std::string tmp = "";
      for (int i = 1; i <= s.size(); ++i) {
        next(curr, &tmp, i);

        tmp_num = binaryToInteger(tmp);
        if (dist[tmp_num] != INF) {
          continue;
        }

        dist[tmp_num] = dist[curr_num] + 1;
        queue.push(tmp_num);
      }
    }

  }

  void taskB() {

    int t = 0;
    std::cin >> t;

    std::string s = "";       // will be override
    for (int i = 0; i < t; ++i) {
      std::cin >> s;
      makeBinary(&s);
      std::cout << "Case #" << (i + 1) << ": " <<  bfs(s) << std::endl;
    }
  }
}


int main() {
  TaskB::taskB();
  return 0;
}