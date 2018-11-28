#include<iostream>
#include<fstream>

using namespace std;

// There are obviously S invariants to the procedure of taking C - 1 transformations:
// At every step, e.g. the first tile of artwork with complexity X is identical to the one at complexity X + 1.
// The second is identical with 2 -> K * (2 - 1) + 2 -> K * (K + 2 - 1) + 2 -> ...
// More generally, for the original position x, i.e. complexity 1, we have pos(x, 1) = x.
// From this we get the invariant sequence pos(x, X + 1) = K * (pos(x, X) - 1) + x for its position at complexity X + 1.

int main() {
  ifstream fin("D-small-attempt0.in");
  ofstream fout("D-small-attempt0.out");

  int T;
  fin >> T;

  for (int t = 1; t <= T; t++) {
    int K, C, S;
    fin >> K >> C >> S;

    long positions[K + 1];
    for (int x = 0; x <= K; x++)
      positions[x] = x;

    for (int c = 1; c < C; c++)
      for (int x = 1; x <= K; x++) {
	positions[x] *= K;
	positions[x] += x - K;
      }
    
    fout << "Case #" << t << ": ";
    for (int x = 1; x <= K; x++) {
      fout << positions[x];
      if (x != K)
	fout << " ";
    }
    fout << endl;
  }

  return 0;
}
