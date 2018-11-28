#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <limits>
#include <cassert>

using namespace std;

int main(int argc, char** argv)
{
	ifstream input(argv[1]);
  unsigned long long T;
  input >> T;

  for (unsigned long long i = 1; i <= T; i++)
	{
		size_t K, C, S;
		input >> K >> C >> S;

		cout << "Case #" << i << ":"; 
		for (size_t j = 1; j <= K; j++)
			cout << " " << j;
		cout << endl;
	}

  return 0;
}
