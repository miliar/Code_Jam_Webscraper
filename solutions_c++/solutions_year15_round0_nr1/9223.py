#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <array>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef unsigned long long num;



int _tmain(int argc, _TCHAR* argv[])
{

  ifstream inputFile("test.txt");

  ofstream outputFile("test2.txt");

  int noOfTests;
  inputFile >> noOfTests;



  for (int test = 0; test < noOfTests; ++test)
  {
    int maxShyLevel;
    string people;
    inputFile >> maxShyLevel;
    inputFile >> people;

    vector<int> peopleWithShyness;

    for (int i = 0; i < people.length(); ++i)
      peopleWithShyness.push_back(people[i] - 48);

    int peopleClapping = 0;
    int peopleInvited = 0;
    for (int i = 0; i < peopleWithShyness.size(); ++i)
    {
      if (peopleClapping < i && peopleWithShyness[i] > 0)
      {
        peopleInvited += i - peopleClapping;
        peopleClapping += i - peopleClapping;
      }      
      peopleClapping += peopleWithShyness[i];
    }
    outputFile << "Case #" << test+1 <<": "<< peopleInvited << endl;
  }

  outputFile.close();

  return 0;
}

