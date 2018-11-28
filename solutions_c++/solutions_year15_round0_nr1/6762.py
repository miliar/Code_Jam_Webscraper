// Copyright Arek Sredzki 2015

#include <iostream>
#include <fstream>

using namespace std;

ifstream inFile ("ovation.in");

ofstream outFile ("ovation.out");

void solve_ovation() {
  int S_max;
  inFile >> S_max;
  inFile.get();

  long people_needed = 0;
  long total_people = 0;

  // int shyness[S_max];

  for (int i = 0; i <= S_max; i++) {
    // shyness[i] = inFile.get() - '0';
    int people = inFile.get() - '0';

    if (total_people < i && people != 0) {
      people_needed += i - total_people;
      total_people = i;
    }

    total_people += people;
  }
  inFile.get();

  outFile << people_needed;

}

int main() {

  int T;
  inFile >> T;

  for (int i = 0; i < T; i++) {
    outFile << "Case #" << i+1 << ": ";
    solve_ovation();
    outFile << endl;
  }

}
