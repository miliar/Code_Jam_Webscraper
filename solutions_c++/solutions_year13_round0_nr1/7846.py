#include <fstream>
#include <iostream>
//#include <string>

void read_table(char table[], std::ifstream* input);
std::string check_table(char table[]);

int main() {
  using namespace std;

  ifstream input("input.txt", ios_base::in);
  ofstream output("output.txt", ios_base::out);

  int n;
  char table[16];
  
  input >> n;
  input.get();
  for (int i = 0; i < n; ++i) {
    read_table(table, &input);
    input.get();
    output << "Case #" << i + 1 << ": " << check_table(table) << endl;
  }
  
  if (input.is_open()) { input.close(); }
  if (output.is_open()) { output.close(); }
  
	return 0;
}

void read_table(char table[], std::ifstream* input)
{
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      input->get(table[i * 4 + j]);
    }
    input->get();
  }
}

std::string check_table(char table[])
{
  using namespace std;
  
  string x_won = "X won";
  string o_won = "O won";
  string draw = "Draw";
  string game_not_complited = "Game has not completed";
  int s;
  // rows
  for (int i = 0; i < 4; ++i) {
    s = table[i * 4] + table[i * 4 + 1] + table[i * 4 + 2] + table[i * 4 + 3];
    if (s == 352 || s == 348) {
      return x_won;
    } else if (s == 316 || s == 321) {
      return o_won;
    }
  }
  // columns
  for (int i = 0; i < 4; ++i) {
    s = table[i] + table[i + 4] + table[i + 8] + table[i + 12];
    if (s == 352 || s == 348) {
      return x_won;
    } else if (s == 316 || s == 321) {
      return o_won;
    }
  }
  // diagonals
  s = table[0] + table[5] + table[10] + table[15];
  if (s == 352 || s == 348) {
    return x_won;
  } else if (s == 316 || s == 321) {
    return o_won;
  }
  s = table[3] + table[6] + table[9] + table[12];
  if (s == 352 || s == 348) {
    return x_won;
  } else if (s == 316 || s == 321) {
    return o_won;
  }
  
  
  for (int i = 0; i < 16; ++i) {
    if (table[i] == '.') {
      return game_not_complited;
    }
  }
  
  return draw;
}
