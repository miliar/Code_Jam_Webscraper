#include <iostream>
#include <fstream>
using namespace std;

int main() {
  ifstream in("A-large.in");
  streambuf *cinbuf = cin.rdbuf();
  cin.rdbuf(in.rdbuf());
  ofstream out("out.txt");
  streambuf *coutbuf = std::cout.rdbuf();
  cout.rdbuf(out.rdbuf());
  int t, n, num, c, needed;
  char tmp;
  cin >> t;

  for(int i = 1; i <= t; i++)
  {
    cin >> n;
    c = 0;
    needed = 0;
    for(int j = 0; j < n + 1; j++)
    {
      cin >> tmp;
      num = tmp - '0';
      if(c >= j)
      {
        c += num;
      }
      else
      {
        needed += j - c;
        c += j - c;
        c += num;
      }
    }

    cout << "Case #" << i << ": " << needed << endl;
  }
  return 0;
}