#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <list>

using namespace std;


int main () {
  ifstream input;
  input.open("input");

  int ntest;
  input >> ntest;

  for (int k=0;k<ntest;k++) {
    int N;
    input >> N;

    vector<string> strings;
    string tmp;
    for (int i=0;i<N;i++) {
      input >> tmp;
      strings.push_back(tmp);
    }

    int modifs = 0;
    bool possible = true;
    bool done = false;
    vector<int> indices(N, 0);

    while (!done && possible) {
      list<int> repeats;

      char c = strings[0][indices[0]];
      for (int s=0;s<N;s++) {
        int i=indices[s];
        string ss = strings[s];
        if (i >= ss.size() || ss[i] != c) possible = false; // Encounter a missing character.
        else {
          for (;i<ss.size() && ss[i] == c; i++);
          repeats.push_front(i-indices[s]);
          indices[s] = i;
        }
      }

      // Select the average value.
      list<int>::iterator it;
      int avg = 0;
      for (it = repeats.begin();it != repeats.end(); it++) avg += *it;
      avg /= N;

      for (it = repeats.begin();it != repeats.end(); it++) {
        modifs += (*it < avg) ? (avg - *it) : (*it - avg);
      }

      // Termination.
      bool forall_end = true, exists_end = false;
      for (int s=0;s<N;s++) {
        if (indices[s] >= strings[s].size())
          exists_end = true;
        else
          forall_end = false;
      }

      if (forall_end) done = true;
      else if (exists_end) possible = false;
      
    }

    if (!possible)
      cout << "case #" << k+1 << ": Fegla Won" << endl;
    else
      cout << "case #" << k+1 << ": " << modifs << endl;
  }

  input.close();
  return 0;
}

