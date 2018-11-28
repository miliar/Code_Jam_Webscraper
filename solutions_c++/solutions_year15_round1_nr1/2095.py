#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <exception>
#include <iomanip>

using namespace std;

string trimString(const string& input, char delim = ' ')
{
  const string emptyString;
  size_t startPos = input.find_first_not_of(delim);
  if (startPos == string::npos) return emptyString;
  size_t endPos = input.find_last_not_of(delim);

  return input.substr(startPos, endPos - startPos + 1);
}

vector<string> splitString(const string& input, char delim = ' ')
{
  vector<string> splits;
  string trimmedInput = trimString(input);
  size_t startPos = 0, endPos, len;
  while (startPos < trimmedInput.length())
  {
    endPos = trimmedInput.find_first_of(delim, startPos);
    len = (endPos == string::npos ? endPos : endPos - startPos) ;
    splits.push_back(trimmedInput.substr(startPos, len));
    if (endPos == string::npos) break;

    startPos = trimmedInput.find_first_not_of(delim, endPos);
  }
  return splits;
}

size_t maxEatRate = 0;

size_t methodA(const vector<size_t> intervalNums)
{
  if (intervalNums.empty()) return 0;
  size_t minMush = 0;
  size_t prev = intervalNums[0];
  for (size_t i = 1; i < intervalNums.size(); i++)
  {
    if (intervalNums[i] < prev)
      minMush += (prev - intervalNums[i]);

    if (prev > intervalNums[i] && ((prev - intervalNums[i]) > maxEatRate))
      maxEatRate = prev - intervalNums[i];

    prev = intervalNums[i];
  }
  return minMush;
}

size_t methodB(const vector<size_t> intervalNums)
{
  if (intervalNums.empty()) return 0;
  size_t minMush = 0;
  for (size_t i = 0; i+1 < intervalNums.size(); i++)
    if (intervalNums[i] <= maxEatRate) minMush += intervalNums[i];
    else minMush += maxEatRate;

  return minMush;
}

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

  for (size_t i = 0; i < numTestCases; i++)
  {
    maxEatRate = 0;
    size_t numIntervals;
    vector<size_t> intervalNums;
    inputFile >> numIntervals;
    for (size_t j = 0; j < numIntervals; j++)
    {
      size_t numMushrooms;
      inputFile >> numMushrooms;
      intervalNums.push_back(numMushrooms);
    }

    size_t method1 = methodA(intervalNums);
    size_t method2 = methodB(intervalNums);

    cout << "Case #" << i+1 << ": " << method1 << " " << method2 << endl;
  }

  return 0;
}
