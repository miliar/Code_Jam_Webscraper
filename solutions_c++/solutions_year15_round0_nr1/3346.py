#include <iostream>
#include <string>
#include <sstream>
using namespace std;

string doCase() {
   string line;
   getline(cin, line);
   stringstream ss(line);
   string m, levels;
   ss >> m >> levels;
   int standing = 0;
   int friends = 0;
   for (int i = 0; i < levels.size(); ++i) {
      int next = levels[i] - '0';
      if (standing < i) {
         friends += i - standing;
         standing = i;
      }
      standing += next;
   }
   stringstream ss2; ss2 << friends;
   return ss2.str();
}
int main() {
   int cases;
   cin >> cases;
   cin.ignore();
   for (int c = 0; c < cases; ++c) {
      cout << "Case #" << c + 1 << ": " << doCase() << '\n';
   }
   return 0;
}