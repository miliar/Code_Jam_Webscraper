#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const char IN_FILE[] = "input.txt";
const char OUT_FILE[] = "output.txt";

int main() {
  ifstream cin(IN_FILE);
  ofstream cout(OUT_FILE);

  int testCount;
  cin >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    int K, C, S;
    cin >> K >> C >> S;
    cout << "Case #" << test << ": ";
    for (int i = 1; i <= S; ++i)
      cout << i << " ";
    cout << "\n";
  }

  cin.close();
  cout.close();
  return 0;
}
