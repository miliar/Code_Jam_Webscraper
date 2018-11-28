/** Revenge of Pancakes
 * Author: Don Vo
 * Solution to Google Jam's Problem B
 * Google Coding Jam 2016
 * Problem B: Revenge of Pancakes
 */
#include <stdlib.h>
#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

bool const HAPPY = true;
bool const BLANK = false;

int const FLIPPING_HAPPY = 0;
int const FLIPPING_BLANK = 1;
int const DONE_FLIPPING = 2;

int const BASE = 10;

void print(vector<bool>& pancakes);


int main(void) {

  // Keep a stack of pancakes;
  vector<bool> pancakes;
  string input;
  getline(cin, input);
  int numCases = atoi(input.c_str());
  bool flipMethod = BLANK;
  int state;
  bool done;
  int numFlips;
  bool allHappy;


  // Run for each case
  for (int i = 0; i < numCases; i++) {

    numFlips = 0;

    // Get the next line and parse it
    getline(cin, input);
    pancakes.clear();
    for (int c = input.size() - 1; c >= 0; c--) {
      if(input[c] == '+') {
	pancakes.push_back(HAPPY);
      } else {
	pancakes.push_back(BLANK);
      }
    }

    done = false;
    while (!done) {
      state = FLIPPING_HAPPY;
      // Determine the algorithm depending on the side of the top pancake
      if (pancakes[pancakes.size() - 1] == HAPPY) {
	flipMethod = HAPPY;
      } else {
	flipMethod = BLANK;
      }

      // Exit if all pancakes faced up
      allHappy = true;
      for (int p = 0; p < pancakes.size(); p++) {
        if (pancakes[p] == BLANK) {
	  allHappy = false;
	  break;
	}
      }

      if (allHappy) break;

      // Flip the pancakes
      if (flipMethod == HAPPY) {
	for (int p = pancakes.size() - 1; p >= 0; p--) {
	  if (state == FLIPPING_HAPPY && pancakes[p] == BLANK) {
            state++;
	  } else if (state == FLIPPING_BLANK && pancakes[p] == HAPPY) {
            break;
	  }
	  pancakes[p] = !pancakes[p];
	}
      } else {
	for (int p = pancakes.size() - 1; p >= 0; p--) {
	  if (pancakes[p] == HAPPY) {
	    break;
	  } else {
	    pancakes[p] = HAPPY;
	  }
	}
      }
      numFlips++;
    }

    cout << "Case #" << i + 1 << ": "<<  numFlips << "\n";
  }
}

void print(vector<bool>& pancakes) {
      cout << "[ ";
      for (int g = pancakes.size() - 1; g >= 0; g--) {
        if (pancakes[g] == true)
          cout << "+ ";
	else 
	  cout << "- ";
      }
      cout << "]\n";
  

}
