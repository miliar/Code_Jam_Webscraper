#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <exception>
#include <cassert>

using namespace std;

map<string, map<string, string> > quarternions;

void build()
{
  quarternions.clear();
  quarternions["1"]["1"] = "1";
  quarternions["1"]["i"] = "i";
  quarternions["1"]["j"] = "j";
  quarternions["1"]["k"] = "k";

  quarternions["i"]["1"] = "i";
  quarternions["i"]["i"] = "-1";
  quarternions["i"]["j"] = "k";
  quarternions["i"]["k"] = "-j";

  quarternions["j"]["1"] = "j";
  quarternions["j"]["i"] = "-k";
  quarternions["j"]["j"] = "-1";
  quarternions["j"]["k"] = "i";

  quarternions["k"]["1"] = "k";
  quarternions["k"]["i"] = "j";
  quarternions["k"]["j"] = "-i";
  quarternions["k"]["k"] = "-1";
}

string word, wordValue;
size_t L, X, wordMinusCount;

void init()
{
  wordValue = "";
  wordMinusCount = 0;
}

void wordPower(size_t power, string powWord, size_t minusCount)
{
  string product = wordValue;
  size_t localMinusCount = 0;
  for (size_t j = 1; j < power; j++)
  {
    string result = quarternions[product][wordValue];
    if (result[0] == '-') localMinusCount++;
    product = result.back();
  }
  powWord = product;
  minusCount = localMinusCount + (wordMinusCount * power); 
}

void computeWordValue()
{
  wordValue = word[0];
  for (size_t i = 1; i < word.length(); i++)
  {
    char ch = word[i];
    string charStr;
    charStr.assign(1, ch);

    string result = quarternions[wordValue][charStr];
    if (result[0] == '-') wordMinusCount++;
    wordValue = result.back();
  }
}

bool QuickCheck()
{
  const size_t maxLen = L * X;
  const size_t wordLen = word.length();

  string local;
  size_t minusCount = 0, len = 0, wordIndex = 0;
  while (len < maxLen)
  {
    char ch = word[wordIndex % wordLen];
    string charStr;
    charStr.assign(1, ch);
    if (!local.empty())
    {
      string result = quarternions[local][charStr];
      if (result[0] == '-') minusCount++;
      local = result.back();
    }
    else
      local = charStr;

    wordIndex++;
    len++;
  }
  return (local == "1" && ((minusCount % 2) == 1));
}

string checkIfIJKNew()
{
  if (!QuickCheck()) return "NO";

  const size_t maxLen = L * X;
  const size_t wordLen = word.length();

  string ilocal;
  size_t iminusCount = 0, ilen = 0, iwordIndex = 0;
  while (ilen < maxLen)
  {
    char ich = word[iwordIndex % wordLen];
    string icharStr;
    icharStr.assign(1, ich);
    if (!ilocal.empty())
    {
      string iresult = quarternions[ilocal][icharStr];
      if (iresult[0] == '-') iminusCount++;
      ilocal = iresult.back();
    }
    else
      ilocal = icharStr;

    if (ilocal == "i")
    {
      string jlocal;
      size_t jminusCount = 0, jlen = ilen + 1, jwordIndex = iwordIndex + 1;
      while (jlen < maxLen)
      {
        char jch = word[jwordIndex % wordLen];
        string jcharStr;
        jcharStr.assign(1, jch);
        if (!jlocal.empty())
        {
          string jresult = quarternions[jlocal][jcharStr];
          if (jresult[0] == '-') jminusCount++;
          jlocal = jresult.back();
        }
        else
          jlocal = jcharStr;

        if (jlocal == "j")
        {
          string klocal;
          size_t kminusCount = 0, klen = jlen + 1, kwordIndex = jwordIndex + 1;
          while (klen < maxLen)
          {
            char kch = word[kwordIndex % wordLen];
            string kcharStr;
            kcharStr.assign(1, kch);
            if (!klocal.empty())
            {
              string kresult = quarternions[klocal][kcharStr];
              if (kresult[0] == '-') kminusCount++;
              klocal = kresult.back();
            }
            else
              klocal = kcharStr;

            kwordIndex++;
            klen++;
          }
          if (klocal == "k" && ((iminusCount + jminusCount + kminusCount) % 2 == 0)) return "YES";
        }

        jwordIndex++;
        jlen++;
      } // end of while jlen
    } // end of if ilocal
    iwordIndex++;
    ilen++;
  }
  return "NO";
}

int main(int argc, char** argv)
{
  if (argc < 2)
  {
    cout << "Usage: djikstra <input filename>" << endl;
    return 0;
  }

  ifstream inputFile(argv[1]);
  string line;
  getline(inputFile, line);
  stringstream strStream;
  strStream << line;
  size_t T;
  strStream >> T;
  strStream.clear();
  
  build();

  for (size_t i = 0; i < T; i++)
  {
    init();

    getline(inputFile, line);
    strStream << line;
    strStream >> L >> X;
    strStream.clear();

    getline(inputFile, line);
    strStream << line;
    strStream >> word;
    strStream.clear();

    cout << "Case #" << i+1 << ": " << checkIfIJKNew() << endl;
  }
  return 0;
}
