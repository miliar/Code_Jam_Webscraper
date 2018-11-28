#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <exception>

using namespace std;

int main(int argc, char** argv)
{
  if (argc < 2)
  {
    cout << "Usage: standing_ovation <input filename>" << endl;
    return 0;
  }

  ifstream inputFile(argv[1]);
  string line;
  getline(inputFile, line);
  stringstream strStream;
  strStream << line;
  size_t numTestcases;
  strStream >> numTestcases;
  strStream.clear();

  for (size_t i = 0; i < numTestcases; i++)
  {
    getline(inputFile, line);
    strStream << line;
    size_t maxShyness;
    strStream >> maxShyness;
    string audience;
    strStream >> audience;
    strStream.clear();

    size_t numPeople = 0;
    size_t totalNumPeopleToInvite = 0;
    for (size_t j = 0; j < audience.length(); j++)
    {
      size_t numPeopleNeededToClap = j;
      if (numPeople < numPeopleNeededToClap)
      {
        size_t numPeopleToInvite = (numPeopleNeededToClap - numPeople);
        numPeople += numPeopleToInvite;
        totalNumPeopleToInvite += numPeopleToInvite;
      }
      numPeople += (audience[j] - '0');
    }
    cout << "Case #" << i+1 << ": " << totalNumPeopleToInvite << endl;
  }

  return 0;
}
