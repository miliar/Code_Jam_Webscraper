#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int main(){
    ifstream input;
    input.open("input.in");
    ofstream output;
    output.open("output.out");
    int T;
    input >> T;
    for (int i = 1; i <= T; ++i) {
      vector<int> first;
      vector <int> second;
      int A;
      input >> A;
      int k;
      for (int j = 1; j <= 4; ++j)
        for (int x = 1; x <= 4; ++x) {
          input >> k;
          if (j == A)
            first.push_back(k);
        }
      input >> A;
      for (int j = 1; j <= 4; ++j)
        for (int x = 1; x <= 4; ++x) {
          input >> k;
          if (j == A)
            second.push_back(k);
        }

      sort(first.begin(), first.end());
      sort(second.begin(), second.end());

      vector<int> intersection;

      set_intersection(first.begin(), first.end(), second.begin(), second.end(),
                       back_inserter(intersection));

      if (intersection.size() == 1)
        output << "Case #" << i << ": " << intersection[0] << endl;
      if (intersection.size() == 0)
        output << "Case #" << i << ": Volunteer cheated!" << endl;
      if (intersection.size() > 1 )
        output << "Case #" << i << ": Bad magician!" << endl;
    }
    input.close();
    output.close();
}
