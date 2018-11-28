#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream in(argv[1]);
    unsigned int N;
    in >> N;
    in.ignore();

    for (unsigned int n = 0; n < N; ++n)
    {
      unsigned int Smax;
      in >> Smax;
      in.get(); // ignore space
      vector<unsigned int> audience(Smax+1);
      for (unsigned int i = 0; i < Smax + 1; ++i)
        audience[i] = in.get() - 48;

      unsigned int A = 0;
      unsigned int xtra = 0;
      for (unsigned int s = 0; s <= Smax; ++s)
      {
        if (A < s)
        {
          ++xtra;
          ++A;
        }
        A += audience[s];
      }

      cout << "Case #"<<n+1<<": "<<xtra << endl;
    }
    return 0;
}
