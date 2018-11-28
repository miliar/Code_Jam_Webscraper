#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  int N;
  cin >> N; cin.ignore();
  for (int C = 1; C <= N; ++C)
  {
    cout << "Case #" << C << ": ";
    string d;
    getline(cin, d);
    bool H = d[0] == '+';
    int F = 0;
    for (int i = 0; i < d.size(); ++i)
    {
      bool H2 = d[i] == '+';
      if (H == H2)
        continue;
      H = H2;
      ++F;
    }
    if (d[d.size() - 1] == '-') ++F;
    cout << F << endl;
  }
}
