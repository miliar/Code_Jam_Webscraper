#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cassert>
using namespace std;

ostream& operator << (ostream& os, const vector<float> &x) {
  os.precision(3);
  os.setf( std::ios::fixed, std::ios::floatfield );
  for (int i=0; i<x.size(); ++i)
    os << x[i] << " ";
  return os;
}


void getBlocks(ifstream& fin, vector<float>& w1, vector<float>& w2) {
  int N;
  fin >> N;

  w1.resize(N);
  w2.resize(N);

  for (int i=0; i<N; ++i)
    fin >> w1[i];

  for (int i=0; i<N; ++i)
    fin >> w2[i];

  std::sort(w1.begin(), w1.end());
  std::sort(w2.begin(), w2.end());
}

int playDeceitfulWar(vector<float> w1, vector<float> w2) {

  int score = 0;

  while (w1.size() > 0) {
    if (w2.back() > w1.back()) {
      // Lose whatsoever, trade smallest with the largest 
      w2.pop_back();
      w1.erase(w1.begin());
    }
    else {
      // Opponent give up, use the one slightly bigger than it.
      auto just_bigger = std::upper_bound(w1.begin(), w1.end(), w2.front());
      assert(just_bigger != w1.end());
      w1.erase(just_bigger);
      w2.erase(w2.begin());
      ++score;
    }
  }

  return score;
}

int playWar(const vector<float> &w1, vector<float> w2) {
  int score = 0;

  for (int i=0; i<w1.size(); ++i) {
    auto just_bigger = std::upper_bound(w2.begin(), w2.end(), w1[i]);
    
    if (just_bigger != w2.end()) {
      w2.erase(just_bigger);
      // cout << w1[i] << " < " << *just_bigger << endl;
    }
    else {
      w2.erase(w2.begin());
      ++score;
    }
  }

  return score;
}

int main(int argc, char* argv[]) {
 
  if (argc < 3) {
    cout << "Usage: ./war input output" << endl;
    return -1;
  }

  ifstream fin(argv[1]);
  ofstream fout(argv[2]);

  int N;
  fin >> N;

  for (int i=0; i<N; ++i) {
    // printf("\33[34m============= Case #%d =============\33[0m\n", i + 1);
    vector<float> w1, w2;
    getBlocks(fin, w1, w2);
    auto s = playWar(w1, w2);
    auto ds = playDeceitfulWar(w1, w2);
    cout << "Case #" << i + 1 << ": " << ds << " " << s << endl;
    fout << "Case #" << i + 1 << ": " << ds << " " << s << endl;
  }

  fout.close();
  fin.close();

  return 0;
}
