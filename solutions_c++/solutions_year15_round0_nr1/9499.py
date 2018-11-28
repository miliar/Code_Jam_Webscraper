// CodeJam 2015
// Rodrigo Gonzalez del Cueto
// Problem A

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int get_helpers_needed( int shine_max, std::string shiness_str ) {
  int shiness_lvl = 0;
  int counter = 0;
  int helpers = 0;

  for ( char &c : shiness_str ) {

    if ( shine_max < counter ) {
      return helpers;
    }

    int new_helpers = 0;
    if (counter < shiness_lvl) {
      new_helpers = shiness_lvl - counter;
    }

    helpers += new_helpers;
    counter += (int)c - '0' + new_helpers;

    shiness_lvl++;
  }

  return helpers;
}

int find_space_token( std::string str ) {
  int place = 0;

  for( char &c : str ) {
    if ( c == ' ' ) {
      return place;
    }
    place++;
  }

  return -1;
}

int main() {
  std::vector<std::string> lines;

  // While stdin is not EOF, read lines.
  while( std::cin.good() ) {
    std::string s;
    std::getline(std::cin, s);
    lines.push_back(s);
  }

  int num_cases = std::stoi(lines[0]);

  for( auto i = 1; i <= num_cases; ++i ) {
    std::cout << "Case #" << i << ": ";

    int str_tok = find_space_token(lines[i]);
    int shiness_max = std::stoi(lines[i].substr(0, str_tok));

    std::cout << get_helpers_needed(shiness_max, lines[i].substr(str_tok + 1)) << std::endl;
  }

  return 0;
}
