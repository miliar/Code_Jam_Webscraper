#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[]) {
  if (argc != 2)
    return -1;

  ifstream fin(argv[1]);

  int nCases;
  fin >> nCases;
 
  for (int i=0; i<nCases; ++i) {
    int smax;
    fin >> smax;

    string s;
    fin >> s;

    int nStoodUp = 0, nAudiance = 0;

    for (int j=0; j<s.size(); ++j) {
      int n = s[j] - '0';
      nAudiance += n;

      if (nStoodUp < j)
	nStoodUp += (j - nStoodUp);

      nStoodUp += n;
    }

    int nFriends = nStoodUp - nAudiance;
    printf("Case #%d: %d\n", i + 1, nFriends);
  }
}

