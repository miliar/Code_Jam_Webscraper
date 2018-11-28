#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
  int T;
  int c = 1;
  cin >> T;
  while (T--) {
    int Smax;
    string Sstring;

    cin >> Smax >> Sstring;
    
    int people_standing = 0;
    int people_needed = 0;
    for (size_t s = 0; s <= Smax; s++)
    {
      int potential = Sstring[s] - '0';
      if (people_standing < s) {
        int extra_people = s - people_standing;
        people_needed += extra_people;
        people_standing += extra_people;
      }
      people_standing += potential;
    }

    cout << "Case #" << c++ << ": " << people_needed << endl;


    

  }

  return 0;
}