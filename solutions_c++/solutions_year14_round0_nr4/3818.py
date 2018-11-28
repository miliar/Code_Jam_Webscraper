#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int play_deceitful_war(const vector<double>& blocks_naomi,
                       const vector<double>& blocks_ken)
{
  const int N = blocks_naomi.size();
  int naomi_wins = 0;

  // Naomi's deceitful strategy:
  // 
  // - If Ken's lightest block is heavier than Naomi's lightest block,
  //   use the lightest block to kill Ken's heaviest block.
  //
  // - Otherwise, Naomi's lightest block is heavier than Ken's
  //   lightest block. In this case, Naomi can lie and say that her
  //   lightest block is heavier than Ken's heaviest block. This
  //   trick's Ken into playing his lightest block and thus Naomi
  //   wins.
  //

  int naomi_first = 0;
  int ken_first = 0;
  int ken_last = N-1;
  while ( naomi_first < N ) {
    while ( naomi_first < N && blocks_ken[ken_first] > blocks_naomi[naomi_first] ) {
      ++naomi_first;
      --ken_last;
    }
    while ( naomi_first < N && blocks_ken[ken_first] < blocks_naomi[naomi_first] ) {
      ++naomi_wins;
      ++naomi_first;
      ++ken_first;
    }
  }

  return naomi_wins;
}
  
int play_war(const vector<double>& blocks_naomi,
             const vector<double>& blocks_ken)
{
  const int N = blocks_naomi.size();
  
  int naomi_last = N-1;
  int ken_first = 0;
  int ken_last = N-1;

  int naomi_wins = 0;
  while ( naomi_last >= 0 ) {
    while ( ( naomi_last >= 0 ) && ( blocks_naomi[naomi_last] > blocks_ken[ken_last] ) ) {
      ++naomi_wins;
      --naomi_last;
      ++ken_first;
    }
    while ( ( naomi_last >= 0 ) && ( blocks_naomi[naomi_last] < blocks_ken[ken_last] ) ) {
      --naomi_last;
      --ken_last;
    }
  }
  return naomi_wins;
}

int main() {

  int num_tests;
  cin >> num_tests;
  for ( int t = 1; t <= num_tests; ++t ) {
    int N;
    cin >> N;
    
    vector<double> blocks_naomi (N);
    for ( int i = 0; i < N; ++i ) {
      cin >> blocks_naomi[i];
    }
    sort(blocks_naomi.begin(), blocks_naomi.end());
    
    vector<double> blocks_ken (N);
    for ( int i = 0; i < N; ++i ) {
      cin >> blocks_ken[i];
    }
    sort(blocks_ken.begin(), blocks_ken.end());

    cout << "Case #" << t << ": "
         << play_deceitful_war(blocks_naomi, blocks_ken)
         << " "
         << play_war(blocks_naomi, blocks_ken)
         << "\n";
    
  }
  return 0;
}
