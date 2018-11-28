#include <algorithm>
#include <iterator>
#include <vector>
#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <set>
using namespace std;

ofstream out("output.txt");

void solve(set<int> set1, set<int> set2){
  set<int> res;
  res.clear();

  set_intersection(set1.begin(), set1.end(),
                   set2.begin(), set2.end(),
                   inserter(res, res.begin()));
  
  if(res.size() == 1) out << *(res.begin()) << endl;
  else if(res.size() > 1) out << "Bad magician!" << endl;
  else out << "Volunteer cheated!" << endl;
}



int main(int argc, char** argv){
  if(argc < 2){
    cout <<"Enter input file name" << endl;
    exit(1);
  }

  set<int> set1;
  set<int> set2;
  string dummy;

  ifstream in(argv[1]);

  int ans1, ans2, num, T;
  in >> T;

  for(int i=1; i<=T; i++){
    set1.clear(); set2.clear();
    in >> ans1;
    getline(in, dummy);
    for(int j=1; j<=4; j++){
      if(j==ans1){
        for(int k=0; k<4; k++){
          in >> num;
          //cout << num << "\n" ;
          set1.insert(num);
        }
      }
      else
        for(int k=0; k<4; k++){
          in >> num;
        }
    }

    in >> ans2;
    for(int j=1; j<=4; j++){
      if(j==ans2){
        for(int k=0; k<4; k++){
          in >> num;
          //cout << num << "\n" ;
          set2.insert(num);
        }
      }
      else
        for(int k=0; k<4; k++){
          in >> num;
        }
    }

    out << "case #" << i << ": ";
    solve(set1, set2);
  }

  
  return 0;
}
