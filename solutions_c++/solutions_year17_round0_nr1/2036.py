#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define rep(i, from, to) for(int i = from; i < to; i++)

int main(){
  int T, K, counter; cin >> T;
  string input;
  rep(t, 0, T){
    counter = 0;
    cin >> input >> K;
    vector<int> I;
    rep(i, 0, input.size()) I.push_back(input[i] == '+' ? 1 : 0);
    rep(i, 0, input.size()-K+1){
      if (!I[i]) { counter++; rep(j, i, i+K) { I[j] = 1-I[j]; } }
    }
    cout << "Case #" << t+1 << ": ";
    rep(i, 0, input.size()) {
      if (!I[i]) {
        cout << "IMPOSSIBLE" << endl; break;

      } else if (i == input.size()-1) cout << counter << endl;
    }
    I.clear();
  }
}
