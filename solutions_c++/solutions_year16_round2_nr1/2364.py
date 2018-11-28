#include <iostream>
#include <string>
#include <array>
#include <sstream>
#include <cassert>

using DigitHist = std::array<int, 10>;
using LetterHist = std::array<int, 26>;
using SpelledOut = std::array<std::string, 10>;

SpelledOut Numbers{ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

std::string getPhoneNumber(const std::string& s)
{
  DigitHist digitHist;
  digitHist.fill(0);
  
  LetterHist letterHist;
  letterHist.fill(0);
  
  for (char c : s) {
    ++letterHist[c - 'A'];

    if (c == 'Z') {
      ++digitHist[0];
    }
    else if (c == 'W') {
      ++digitHist[2];
    }
    else if (c == 'U') {
      ++digitHist[4];
    }
    else if (c == 'X') {
      ++digitHist[6];
    }
    else if (c == 'G') {
      ++digitHist[8];
    }
  }

  for (int i = 0; i < 10; i += 2) {
    const std::string& spNum = Numbers[i];

    for (int j = 0; j < digitHist[i]; ++j ) {
      for (char c : spNum) {
	assert (letterHist[c - 'A'] > 0);
	--letterHist[c - 'A'];
      }
    }
  }

  digitHist[1] = letterHist['O' - 'A'];

  assert (letterHist['R' - 'A'] == letterHist['T' - 'A']);
  assert (letterHist['R' - 'A'] == letterHist['H' - 'A']);

  digitHist[3] = letterHist['R' - 'A'];
  digitHist[5] = letterHist['F' - 'A'];
  digitHist[7] = letterHist['S' - 'A'];
  
  for (int i = 1; i < 10; i += 2) {
    const std::string& spNum = Numbers[i];

    for (int j = 0; j < digitHist[i]; ++j) {
      for (char c : spNum) {
	assert (letterHist[c - 'A'] > 0);
	--letterHist[c - 'A'];
      }
    }
  }

  assert (letterHist['N' - 'A'] == 2 * letterHist['I' - 'A']);
  assert (letterHist['N' - 'A'] == 2 *letterHist['E' - 'A']);

  digitHist[9] = letterHist['I' - 'A'];

  std::ostringstream oss;

  for (int i = 0; i < 10; ++i) {
    for (int j = 0; j < digitHist[i]; ++j) {
      oss << i;
    }
  }

  return oss.str();
}

int main()
{
  int cases = 0;
  std::cin >> cases;

  for (int i = 1; i <= cases; ++i) {
    std::string s;
    std::cin >> s;
    
    std::cout << "Case #" << i << ": " << getPhoneNumber(s) << std::endl;
  }
  
  return 0;
}
