#include <iostream>
#include <string>

using namespace std;

int main() {
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    string in;
    cin >> in;
    int res = 1;
    for (int i = 1; i < in.length(); i++) {
      if (in[i] != in[i-1]) res++;
    }
    if (in[in.length() - 1] == '+') res--;
    cout << "Case #" << it << ": " << res << "\n";
  }
  return 0;
}
