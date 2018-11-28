#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

typedef vector<float> vec;

void getData(ifstream& in, vec& b1, vec& b2);
int playDeceitfulWar(vec b1, vec b2);
int playWar(const vec &b1, vec b2);

int main(int argc, char* argv[]) {
 
  if (argc < 3) {
    cout << "Usage: ./war input output" << endl;
    return -1;
  }

  ifstream in(argv[1]);
  ofstream out(argv[2]);

  int N;
  in >> N;

  for (int i=0; i<N; ++i) {
    vec b1, b2;
    getData(in, b1, b2);

    sort(b1.begin(), b1.end());
    sort(b2.begin(), b2.end());

    int s1 = playWar(b1, b2),
	s0 = playDeceitfulWar(b1, b2);

    out << "Case #" << i + 1 << ": " << s0 << " " << s1 << endl;
  }

  out.close();
  in.close();

  return 0;
}

void getData(ifstream& in, vec& b1, vec& b2) {
  int N;
  in >> N;

  b1.resize(N); b2.resize(N);

  for (int i=0; i<N; ++i) in >> b1[i];
  for (int i=0; i<N; ++i) in >> b2[i];
}

int playDeceitfulWar(vec b1, vec b2) {

  int s = 0;

  while (b1.size() > 0) {
    if (b2.back() > b1.back()) {
      b2.pop_back();
      b1.erase(b1.begin());
    }
    else {
      vec::iterator itr = upper_bound(b1.begin(), b1.end(), b2[0]);
      b1.erase(itr);
      b2.erase(b2.begin());
      ++s;
    }
  }

  return s;
}

int playWar(const vec &b1, vec b2) {
  int s = 0;

  for (int i=0; i<b1.size(); ++i) {
    vec::iterator itr = upper_bound(b2.begin(), b2.end(), b1[i]);
    
    if (itr != b2.end())
      b2.erase(itr);
    else {
      b2.erase(b2.begin());
      ++s;
    }
  }

  return s;
}
