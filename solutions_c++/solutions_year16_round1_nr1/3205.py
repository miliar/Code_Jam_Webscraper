#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <exception>
#include <iomanip>
#include <cassert>
#include <algorithm>
#include <sstream>

using namespace std;

int main(int argc, char** argv)
{
  if (argc < 2)
  {
    cout << "Usage: problemA <input file name>" << endl;
    return 0;
  }

  ifstream inputFile(argv[1]);

  size_t numTestCases;
  inputFile >> numTestCases;

  for (size_t i = 1; i <= numTestCases; i++)
  {
    string word;
    inputFile >> word;

    string lastWord;
    lastWord.push_back(word[0]);

    for (size_t i = 1; i < word.length(); i++) {
      if (word[i] >= lastWord[0]) {
        // Prepend
        lastWord.insert(0, 1, word[i]);
        continue;
      }
      // append
      lastWord.push_back(word[i]);
    }

    cout << "Case #" << i << ": " << lastWord << endl;
  }

  return 0;
}
