#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
  int T;
  cin >> T;
  int A; int B; int K;


  for (int ii = 1; ii <= T; ++ii)
  {
    cin >> A >> B >> K;
    
    int cnt = 0;
    for (int aa = 0; aa < A; ++aa)
    {
      for (int bb = 0; bb < B; ++bb)
      {
	if ((aa & bb) < K)
        {
	  ++cnt;
	}
      }
    }

    cout << "Case #" << ii << ": " << cnt << endl;
  }

  return 0;
}
