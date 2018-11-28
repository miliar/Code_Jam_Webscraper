// Copyright 2016 Aleksandr Mikhailov

#include <bits/stdc++.h>

int LeftSon(int index) {
  return 2 * index + 1;
}

int RightSon(int index) {
  return 2 * index + 2;
}

int Parent(int index) {
  return (index - 1) / 2;
}

int Pow(int n) {
  return (2 << n);
}

std::vector<int> Build(int size, int init) {
  std::vector<int> a(Pow(size) - 1);
  a[0] = init;
  for (int i = 1; i < a.size(); ++i) {
    if (LeftSon(Parent(i)) == i) {
      if (a[Parent(i)] == 0 || a[Parent(i)] == 1) {
        a[i] = a[Parent(i)];
      } else {
        a[i] = (a[Parent(i)] + 1) % 3;
      }
    } else {
      if (a[Parent(i)] == 0 || a[Parent(i)] == 1) {
        a[i] = (a[Parent(i)] + 1) % 3;
      } else {
        a[i] = a[Parent(i)];
      }
    }
  }
  return a;
}

void sort(std::string & str) {
  for (int size = 2; size < 8192; size *= 2) {
    for (int i = 0; i + size <= str.size(); i += size) {
      if (str.substr(i, size / 2) > str.substr(i + size / 2, size / 2)) {
        for (int j = 0; j < size / 2; ++j) {
          std::swap(str[i + j], str[i + j + size / 2]);
        }
      }
    }
  } 
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int t;
  std::cin >> t;
  for (int x = 0; x < t; ++x) {
    int n, p, r, s;
    std::cin >> n >> r >> p >> s;
    std::cout << "Case #" << x + 1 << ": ";
    std::vector<std::string> ans;
    for (int i = 0; i < 3; ++i) {
      const auto a = Build(n, i);
      std::vector<int> count(3);
      for (int i = a.size() / 2; i < a.size(); ++i) {
        ++count[a[i]];
      }
      if (count[0] == p && count[1] == r && count[2] == s) {
        std::string str;
        for (int i = a.size() / 2; i < a.size(); ++i) {
          if (a[i] == 0) {
            str += "P";
          } else if (a[i] == 1) {
            str += "R";
          } else {
            str += "S";
          }
        }
        ans.push_back(str);
      }
    }
    if (ans.empty()) {
      std::cout << "IMPOSSIBLE" << std::endl;
      continue;
    }
    for (auto & str : ans) {
      sort(str);
    }
    std::cout << *std::min_element(ans.begin(), ans.end()) << std::endl;
  }
  return 0;
}

