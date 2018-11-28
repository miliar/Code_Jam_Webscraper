#include <iostream>


class Kensaku {
public:
  Kensaku():first(true), count(0){}
  ~Kensaku(){}
  char target;
  bool first;
  static const char T = 'T';
  static const char X = 'X';
  static const char O = 'O';
  static const char dot = '.';
  int count;

  bool firstCompare(char value1, char value2) {
    if (value1 == value2 && value1 != dot) {
      target = value1;
      count = 2;
      return true;
    } else if (value1 == T && value2 != dot) {
      target = value2;
      count = 2;
      return true;
    } else if (value2 == T && value1 != dot) {
      target = value1;
      count = 2;
      return true;
    } else {
      return false;
    }
  }

  bool nextCompare(char value) {
    if (value == target) {
      count++;
      return true;
    } else if (value == T) {
      count++;
      return true;
    } else {
      return false;
    }
  }

  char win() {
    if (count == 4) {
      return target;
    } else {
      return dot;
    }
  }

};


int main() {

  int T;
  std::cin >> T;
  char map[5][5];
  
  int now = 0;
  while(now < T) {
    bool dot_count = false;
    char win_player = Kensaku::dot;
    // o—Í
    now++;
    std::cout << "Case #"
      << now
      << ": ";

    // “ü—Í
    for (int y = 0; y < 4; y++) {   
      std::cin >> map[y];
      if (!dot_count) {
        for (int x = 0; x < 4; x++) {
          if (Kensaku::dot == map[y][x]) {
            dot_count = true;
            break;
          }
        }
      }
    }

    // ˆ—
    for (int y = 0; y < 4; y++) {
      Kensaku kensaku;
      if (kensaku.firstCompare(map[y][0], map[y][1])) {
        if (kensaku.nextCompare(map[y][2])) {
          if(kensaku.nextCompare(map[y][3])) {
            win_player = kensaku.target;
            break;
          }
        }
      }
    }
    if (win_player == Kensaku::dot) {
      for (int x = 0; x < 4; x++) {
        Kensaku kensaku;
        if (kensaku.firstCompare(map[0][x], map[1][x])) {
          if (kensaku.nextCompare(map[2][x])) {
            if(kensaku.nextCompare(map[3][x])) {
              win_player = kensaku.target;
              break;
            }
          }
        }
      }
    }
    if (win_player == Kensaku::dot) {
      Kensaku kensaku;
      if (kensaku.firstCompare(map[0][0], map[1][1])) {
        if (kensaku.nextCompare(map[2][2])) {
          if(kensaku.nextCompare(map[3][3])) {
            win_player = kensaku.target;
          }
        }
      }
    }
    if (win_player == Kensaku::dot) {
      Kensaku kensaku;
      if (kensaku.firstCompare(map[3][0], map[2][1])) {
        if (kensaku.nextCompare(map[1][2])) {
          if(kensaku.nextCompare(map[0][3])) {
            win_player = kensaku.target;
          }
        }
      }
    }

    // o—Í
    if (win_player == Kensaku::X) {
      std::cout << "X won" << std::endl;
    } else if (win_player == Kensaku::O) {
      std::cout << "O won" << std::endl;
    } else if (dot_count) {
      std::cout << "Game has not completed" << std::endl;
    } else {
      std::cout << "Draw" << std::endl;
    }
  }
  return 0;
}