#include <iostream>

using namespace std;

int totalCase;
int results[100];

void readInput() {
  cin >> totalCase;
}

void process() {
  for (int i = 0; i < totalCase; ++i)
  {
    int smax;
    string people;
    cin >> smax >> people;

    int total = 0;
    int required = 0;
    for (int j = 0; j < people.length()-1; ++j)
    {
      int num = people[j] - '0';
      
      total += num;
      if (total < j+1)
      {
        required = required + j + 1 - total;
        total = j+1;
      }
    }
    results[i] = required;
  }
}

void printOutput() {
  for (int i = 0; i < totalCase; ++i)
  {
    cout << "Case #" << i+1 << ": " << results[i] << endl;
  }
}

int main () {
  readInput();
  process();
  printOutput();
  return 0;
}