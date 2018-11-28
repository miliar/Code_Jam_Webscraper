#include <iostream>

void solve_case(int k)
{
  using namespace std;
  cout << "Case #" << k << ": ";
  int possibilities = 0;

  int A; cin >> A; cin.get();
  int B; cin >> B; cin.get();

  int K; cin >> K; cin.get();
  for (int a = 0; a < A; ++a)
  {
    for (int b = 0; b < B; ++b)
    {
      possibilities += (b & a) < K;
    }
  }

  cout << possibilities << endl;
}

/* ------------------------- main() function ------------------------- */

int main(int argc, char const *argv[])
{
  using namespace std;
  if (argc < 2)
    freopen("test.txt", "r", stdin);
  else
  {
    freopen(argv[1], "r", stdin);
    string output_file(argv[1]);
    output_file.append("-result.txt");
    freopen(output_file.c_str(), "w", stdout);
  }
  int T, case_n = 0;
  cin >> T; cin.get();
  do { solve_case(++case_n); }
  while (--T);
}
