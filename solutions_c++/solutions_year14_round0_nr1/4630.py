#include <iostream>
#include <vector>

void solve() {
  int T, num;
  int line_number[2];
  int pos[16][2];
  int map[4][4];

  std::cin >> T;
  for (int i = 0; i < T; ++i) {
    for (int guess = 0; guess < 2; ++guess) {
      std::cin >> line_number[guess];
      for (int x = 0; x < 4; ++x) {
        for (int y = 0; y < 4; ++y) {
          std::cin >> num;
          --num;
          pos[num][guess] = x;
          map[x][y] = 0;
        }
      }
    }

    for (int num = 0; num < 16; ++num) {
      if (map[pos[num][0]][pos[num][1]] > 0) {
        map[pos[num][0]][pos[num][1]] = -1;
      } else if (map[pos[num][0]][pos[num][1]] == 0) {
        map[pos[num][0]][pos[num][1]] = num + 1;
      }
    }

    std::cout << "Case #" << i + 1 << ": ";
    int rst = map[line_number[0] - 1][line_number[1] - 1];

    if (rst > 0) {
      std::cout << rst << std::endl;
    } else if (rst == 0) {
      std::cout << "Volunteer cheated!\n";
    } else {
      std::cout << "Bad magician!\n";
    }
  }
}

int main() {
  solve();
  return 0;
}
