#include <iostream>

using namespace std;

void solve(long long K, int C, int S) {
  // cout << "K " << K << " C " << C << " S " << S << endl;
  if (K > C*S) {
    cout << "IMPOSSIBLE";
    return;
  }

  long long tile_to_search = 0;
  long long step = 1;
  for (long long k = 0; k < K; k++) {
    // cout << "k: " << k << endl;
    if (k % C == 0) {
      tile_to_search = 0;
      step = 1;
    }

    tile_to_search += k * step;
    step *= K;
    // cout << "tile_to_search: " << tile_to_search << endl;

    if (k % C == C-1) {
      if (k > C-1) {
        cout << " ";
      }
      cout << tile_to_search+1;
    }
  }

  if (K%C > 0) {
    // cout << "K%C > 0" << endl;
    if (K > C-1) {
      cout << " ";
    }
    cout << tile_to_search+1;
  }
}

int main() {
  int num_cases;
  cin >> num_cases;
  for (int i = 0; i < num_cases; i++) {
    int K; // num tiles in original sequence
    int C; // complexity (C-1 = number of expansions) (C^K = num tiles in new sequence)
    int S; // num tiles allowed to uncover in new sequence
    cin >> K >> C >> S;

    cout << "Case #" << i+1 << ": ";
    solve(K, C, S);
    cout << endl;
  }
}

/*
C^K can fit in an unsigned long long

Each tile you uncover checks to tiles in the original pattern for gold:

*L*GL
LG*L* GGG LGL
LGLGGG*L*GL GGGGGGGGG LGLGGGLGL

pos 6 in seq_3 ->
  6 / 3 = 2 // pos 2 in seq_2
  2 / 3 = 0 // pos 0 in seq_1


seq_0_pos_0
seq_1_pos_1
seq_2_pos_2
-> 5

*L*GL
L*G*L GGG LGL
LGLGG*G*LGL GGGGGGGGG LGLGGGLGL

Can pick a location to search C spaces in original sequence. If any of those spaces are gold, location will be gold.
To search spaces 0, 1, 2, pick location:
 -> 0*(3^2) + 1*(3^1) + 2*(3^0)
 -> 0*(K^2) + 1*(K^1) + 2*(K^0)
 -> 0*(K^(C-1)) + 1*(K^(C-2)) + 2*(K^(C-3))


Can search C*S spaces.
Can only guarantee finding the gold if K <= C*S
*/