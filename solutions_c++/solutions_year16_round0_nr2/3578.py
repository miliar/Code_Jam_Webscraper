#include<iostream>
#include<fstream>
#include<algorithm>

using namespace std;

const char PLUS = '+';
const char MINUS = '-';

void flip_substack(string & pancakes, int length) {
  reverse(pancakes.begin(), pancakes.begin() + length);
  for (int i = 0; i < length; i++) {
    if (pancakes[i] == PLUS)
      pancakes[i] = MINUS;
    else // if (pancakes[i] == MINUS)
      pancakes[i] = PLUS;
  }  
}

int main() {

  ifstream fin("B-large.in");
  ofstream fout("B-large.out");
  
  int T;
  fin >> T;

  for (int t = 1; t <= T; t++) {
    int count_flips = 0;

    string pancakes;
    fin >> pancakes;

    int n_pancakes = pancakes.size();
    int perfect_pancakes = 0;
    for (int i = n_pancakes - 1; i >= 0 && pancakes[i] == PLUS; i--)
      perfect_pancakes++;      
    
    while (perfect_pancakes != n_pancakes) {
      int count = 0;
      if (pancakes[0] == PLUS) {
    	while (pancakes[count] == PLUS)
    	  count++;
    	flip_substack(pancakes, count);
    	count_flips++;
      }
      while (pancakes[count] == MINUS)
    	count++;

      int non_perfect_pancakes = n_pancakes - perfect_pancakes;
      flip_substack(pancakes, non_perfect_pancakes);
      count_flips++;
      perfect_pancakes += count;
    }
    
    fout << "Case #" << t << ": " << count_flips << endl;
  }

  return 0;
}
