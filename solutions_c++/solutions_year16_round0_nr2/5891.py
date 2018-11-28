#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<bool> getPancakes(string pancakes) {
  vector<bool> p;
  for (unsigned int i = 0; i < pancakes.length(); i++) {
    if (pancakes[i] == '+') {
      p.push_back(true);
    } else {
      p.push_back(false);
    }
  }
  return p;
}

void flipPancakes(unsigned int top, vector<bool> &pancakes) {
  for (unsigned int i = 0; i < top / 2; i++) {
    bool temp = pancakes[i];
    pancakes[i] = pancakes[top - 1 - i];
    pancakes[top - 1 - i] = temp;
  }
  for (unsigned int i = 0; i < top; i++) {
    pancakes[i] = !pancakes[i];
  }
}

unsigned int countPancakes(vector<bool> pancakes, bool objective) {
  unsigned int cont = 0;
  for (unsigned int i = 0; i < pancakes.size(); i++) {
    if (pancakes[i] == objective) cont++;
  }
  return cont;
}

void printPancakes(vector<bool> pancakes) {
  for (unsigned int k = 0; k < pancakes.size(); k++) {
    cout<<pancakes[k];
  }
  cout<<endl;
}

int main() {
  int t;
  cin>>t;

  for (int i = 0; i < t; i++) {

    string input;
    cin>>input;
    vector<bool> pancakes = getPancakes(input);

    bool objective = pancakes.back(); // get last pancake position (flip)

    int flips = 0;
    int pos1 = 0;
    int pos2 = pancakes.size()-1;

    for (unsigned int k = 0; k < pancakes.size(); k++) {
      if (pancakes[k] == objective) pos1 = k;
      else break;
    }

    for (unsigned int k = pos2; k > 0; k--) {
      if (pancakes[k] == objective) pos2 = k;
      else break;
    }

    unsigned int cont = countPancakes(pancakes, objective);
    if (cont == pancakes.size()) {
      pos1 = pos2+1;
    }

    // printPancakes(pancakes);

    while(pos1 <= pos2) {
      // cout<<"-----"<<endl;
      // cout<<"pos1: "<<pos1<<" pos2: "<<pos2<<endl;
      if (pancakes[pos1] == objective) {
        flipPancakes(pos1+1, pancakes);
        flips++;
        // printPancakes(pancakes);
      }

      unsigned int cont = countPancakes(pancakes, objective);
      if (cont == pancakes.size()) break;

      flipPancakes(pos2, pancakes);
      flips++;
      // printPancakes(pancakes);

      cont = countPancakes(pancakes, objective);
      if (cont == pancakes.size()) break;

      for (unsigned int k = 0; k < pancakes.size(); k++) {
        if (pancakes[k] == objective) pos1 = k;
        else break;
      }
      for (unsigned int k = pos2; k > 0; k--) {
        if (pancakes[k] == objective) pos2 = k;
        else break;
      }
      // cout<<"pos1: "<<pos1<<" pos2: "<<pos2<<endl;
    }
    // cout<<"pos1: "<<pos1<<" pos2: "<<pos2<<endl;
    if (!objective) flips++;
    cout << "Case #" << (i+1) << ": " << flips << endl;
  }

  return 0;
}
