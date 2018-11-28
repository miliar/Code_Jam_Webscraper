#include <iostream>
#include <iomanip>
#include <set>
#include <algorithm>
#include <iterator>
#include <assert.h>

using namespace std;

int war(multiset<double> Na, multiset<double> Ke, bool deceit){
  int s = 0;
  double chk, chn, ton, max, min;
  auto N = Na.size();
  multiset<double> Naomi(Na), Ken(Ke);
  multiset<double>::iterator ik, in;

  for(int i=0;i<N;i++){
    in = Naomi.begin();
    chn = *in;
    Naomi.erase(in);
    if(deceit){
      max = *Ken.rbegin();
      min = *Ken.begin();
      if(min < chn) // Win
        ton = max + 0.0000001;
      else // Make him waste
        ton = max - 0.0000001;
    }else{
      ton = chn;
    }

    ik = Ken.upper_bound(ton);
    if(ik == Ken.end()) ik = Ken.begin();
    chk = *ik;
    Ken.erase(ik);

    if(chn > chk){
      assert(ton > chk);
      ++s;
    }else{
      if(chn == chk) assert(ton == chk);
      else assert(ton < chk);
    }
  }

  return s;
}

void solveCase(int n){
  int N;
  multiset<double> Naomi, Ken;
  double v;
  int x, y;
  cin >> N;
  for(int i=0; i<N; i++){
    cin >> v;
    Naomi.insert(v);
  }
  for(int i=0; i<N; i++){
    cin >> v;
    Ken.insert(v);
  }

  // PLAY
  x = war(Naomi, Ken, true);
  y = war(Naomi, Ken, false);
  // <<<< PLAY

  cout << "Case #" << n << ": " << x << " " << y << endl;
}

int main(int argc, char** argv){
  int T;
  cin >> T;
  for(int i=0; i < T; i++){
    solveCase(i+1);
  }
  return 0;
}
