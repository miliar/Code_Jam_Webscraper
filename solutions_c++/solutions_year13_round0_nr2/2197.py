#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

unsigned int field[100][100];
unsigned __int64 N, M;

bool doable(int rIndex, int cIndex) {
  bool higherOnRow = false;
  bool higherOnColumn = false;

  // check column
  for (unsigned int r = 0;r<N;r++) {
    if (field[rIndex][cIndex] < field[r][cIndex]) {
      higherOnColumn = true;
      break;
    }
  }

  // check row
  for (unsigned int c = 0;c<M;c++) {
    if (field[rIndex][cIndex] < field[rIndex][c]) {
      higherOnRow = true;
      break;
    }
  }

  return !(higherOnRow && higherOnColumn);
}

int main (int argc, const char **argv) {
  unsigned __int64 noCases;
  
  if (argc != 2) {
    std::cout << "syntax: exe file" << std::endl;
    return 1;
  }

  std::ifstream input;
  input.open(argv[1]);
  if (!input.is_open()) {
    std::cout << "file not found" << std::endl;
    return 1;
  }

  std::string line;
  getline(input, line);
  std::stringstream ss(line);

  ss >> noCases;

  if (noCases > 100) {
    std::cout << "T exceeds 100" << std::endl;
  }

  std::ofstream output;
  output.open("result.txt");


  for (unsigned int i = 1;i<=noCases;i++) {
    output << "Case #" << i << ": ";
    std::cout << "Case #" << i << ": ";
    
    getline(input, line);
    ss = std::stringstream(line);
    ss >> N >> M;

    if (N > 100 || M > 100) {
      std::cout << "parsing incorrect" << std::endl;
      continue;
    }
    
    for (unsigned int r = 0;r<N;r++) {
      getline(input, line);
      ss = std::stringstream(line);
      for (unsigned int c = 0;c<M;c++) {
        ss >> field[r][c];
        if (field[r][c] < 1 || field[r][c] > 100) {
          std::cout << "parsing incorrect" << std::endl;
          continue;
        }
      }
    }

    // check if every field is the minimum in either row or column (or both)
    bool check = true;
    for (unsigned int r = 0;r<N;r++) {
      for (unsigned int c = 0;c<M;c++) {
        if (!doable(r, c)) {
          check = false;
          break;
        }
        if (!check)
          break;
      }
    }

    output << ((check) ? "YES" : "NO") << std::endl;
    std::cout << ((check) ? "YES" : "NO") << std::endl;
  }

  input.close();
  output.close();

  return 0;
}