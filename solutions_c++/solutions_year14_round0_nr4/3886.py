#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int determineScore(vector<float> weights[2], int N, bool who) {
  int score0 = 0;
  int score1 = 0;
  int lowIndex = 0;
  int highIndex = N-1;
  for ( int i = N; --i >=0; ) {
    if (weights[1].at(highIndex) > weights[0].at(i)) {
      score0++;
      highIndex -= 1;
    }
    else {
      score1++;
      lowIndex += 1;
    }
  }
  if ( who )
    return score0;
  return score1;
}

int main() {
  int numProb;
  cin >> numProb;
  int N;

  for (int i = 0; i < numProb; i++) {
    cin >> N;
    vector<float> weights[2];
    for ( int j = 0; j < 2; j++) {
      for ( int k = 0; k < N; k++) {
        float temp;
        cin >> temp;
        weights[j].push_back(temp);
      }
    }

    sort (weights[0].begin(), weights[0].end());
    sort (weights[1].begin(), weights[1].end());
    
    int warOpt = 0 , warDec = 0;
    
    warOpt = determineScore(weights, N, false);
    vector<float> revWeights[2];
    revWeights[0] = weights[1];
    revWeights[1] = weights[0];
    warDec = determineScore(revWeights, N, true);
    /*
    for ( int j = 0; j < N; j++ ) {
      cout << "w0: " << weights[0].at(j) << " w1: " << weights[1].at(j) << endl;
      if ( weights[0].at(j) > weights[1].at(j) ) {
        warOpt++;
      }
      cout << "w0Dec: " << weights[0].at(j) << " w1: " << weights[1].at(N-1-j) << endl;
      if ( weights[0].at(j) > weights[1].at(N-1-j) ) {
        warDec++;
      }
    }
    */

    cout << "Case #" << i + 1 << ": " << warDec << " " << warOpt << endl;
  }
}
