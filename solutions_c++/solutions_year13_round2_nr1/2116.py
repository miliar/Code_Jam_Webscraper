#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int min1 = -1;

void recurse(vector<int> motes, int iter, int moves, int A){
  if (iter == motes.size()){
    if (min1 == -1)
      min1 = moves;
    else if (moves < min1)
      min1 = moves;
    return;
  }
  else if (A > motes[iter]){
    A += motes[iter];
    iter++;
    recurse(motes, iter, moves, A);
  }
  else {
    if (A != 1)
      recurse(motes, iter, moves+1, A + A - 1);
    recurse(motes, iter + 1, moves + 1, A);
  } 
  
}

int main(){
  ifstream in ("A-small-attempt0.in");
  ofstream out ("bar.txt");
  int pee;
  in >> pee;

  for (int ho = 0; ho < pee; ho++){
    int A;
    in >> A;
    int size;
    in >> size;
    vector<int> motes;
    for (int i = 0; i < size; i++){
      int temp;
      in >> temp;
      motes.push_back(temp);
    }
      
    sort(motes.begin(), motes.end());
    
    recurse(motes, 0, 0, A);

    out << "Case #" << ho+1 << ": "<< min1 << endl;
    min1 = -1;
  }


  return 0;
}
