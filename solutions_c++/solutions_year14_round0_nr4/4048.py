#include <algorithm>
#include <iterator>
#include <vector>
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

  ofstream out("output.txt");

void solve(vector<double> arr1, vector<double> arr2){
  vector<double>::iterator n1, n2, d1, d2;
  int y, z;
  bool c1, c2;
  
  n1 = arr1.begin(); n2 = arr2.begin(); 
  d1 = arr1.begin(); d2 = arr2.begin();

  sort(arr1.begin(), arr1.end());
  sort(arr2.begin(), arr2.end());

  while (true){
    c1 = (n2 == arr2.end());
    c2 = (d1 == arr1.end());

    if(c1 && c2) break;

    if(!c1){
      if(*n1 < *n2){
        n1++;
        n2++;
      }

      else {
        n2++;
      }
    }

    if(!c2){
      if(*d2 < *d1){
        d1++;
        d2++;
      }

      else {
        d1++;
      }
    }
  }

  y = static_cast<int> (d2 - arr2.begin());
  z = static_cast<int> (arr1.end() - n1);

  out << y << " " << z << endl;
}



int main(int argc, char** argv){
  if(argc < 2){
    cout <<"Enter input file name" << endl;
    exit(1);
  }

  vector<double> arr1;
  vector<double> arr2;

  ifstream in(argv[1]);

  int T, N;
  in >> T;

  for(int i=1; i<=T; i++){
    in >> N;
    double num;

    arr1.clear(); arr2.clear();
    arr1.resize(N); arr2.resize(N);

    for(int j=0; j< N; j++){in >> num; arr1[j] = num;}
    for(int j=0; j< N; j++){in >> num; arr2[j] = num;}

    out << "case #" << i << ": ";
    solve(arr1, arr2);
  }

  

  return 0;
}
