#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <map>
#include <set>
#include <sstream>
using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

unordered_set<char> vowels;
unordered_set<string> processedWords;

bool isVowel(char c)
{
   return vowels.find(c) != vowels.end();
}

bool isConsonant(char c)
{
   return !isVowel(c);
}

int gN;
int Yn;

int calcNumberOfCons(const string& name)
{
   int n = 0;
   int max = 0;
   for (int i = 0; i < name.size(); ++i)
   {
      if (isConsonant(name[i]))
      {
         n++;
         if (n >= max)
         {
            max = n;
         }
      }
      else
      {
         n = 0;
      }
   }
   return max;
}

void calculate(const string& name, int l)
{
   while (true)
   {
      for (int i = 0; i < name.size() - l + 1; ++i)
      {
        // cout << i << endl;
        // cout << name.substr(i, l) <<endl;
         if (calcNumberOfCons(name.substr(i, l)) >= gN)
         {
            Yn++;
           // std::cout << Yn << endl;
         }
      }
      l = l - 1;
      if (l < gN)
         break;
   }
}

int processTestCase(const string& name, int n)
{
   gN = n;
   Yn = 0;
   calculate(name, (int)name.size());
   return Yn;
}

int _tmain(int argc, _TCHAR* argv[])
{
   vowels.insert('a');
   vowels.insert('e');
   vowels.insert('i');
   vowels.insert('o');
   vowels.insert('u');
   cout << calcNumberOfCons("ololalulidolelelelelele");
   //cout << calcNumberOfCons("loldoaaaa");
   //cout << calcNumberOfCons("");
   //cout << isConsonant('a') << isConsonant('o') << isConsonant('e') << isConsonant('i') << isConsonant('u');
   fstream inputFile("input.txt", fstream::in);
   fstream outputFile("output.txt", fstream::out);
   std::string line;
   getline(inputFile, line);
   int testCasesQty = atoi( line.c_str() );
   int testCasesProcessed = 0;
   while (true)
   {
      string name;
      int n;
      inputFile >> name >> n;
      //std::cout << name << n << endl;
      outputFile << "Case #" << ++testCasesProcessed << ": " << processTestCase(name,n);
      if (testCasesProcessed == testCasesQty)
         break;
      else
         outputFile  << '\n';
   }
   return 0;
}

