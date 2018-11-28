
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int main() {
	int T;	
	cin >> T;

  for(int t = 1; t <= T; t++) {

    int N, X;
    cin >> N >> X;
    vector<int> S(N);
    for(int i = 0; i < N; i++) cin >> S[i];
    sort(S.rbegin(), S.rend());

    int nb = 0;
    for(int i = 0; i < S.size(); i++) {
      int j = S.size()-1;
      for(; j > i; j--) if(S[j] + S[i] <= X) break;
      if(j > i && S[j] + S[i] <= X) S.erase(S.begin() + j);
      nb++;
    }
    cout << "Case #" << t << ": " << nb << endl;
  }


}
