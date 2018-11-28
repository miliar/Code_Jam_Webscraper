#include <cstdlib>
#include <fstream>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main () {


  ifstream ifile("input.in");
  ofstream ofile("output.txt");

  int cases;
  ifile>>cases;

  for(int i=0; i<cases; i++) {
    int firstrow, secondrow;
    ifile>>firstrow;
    vector<int> firstcards, rowone, secondcards, rowtwo;
    for(int j=0; j<16; j++) {
      int a;
      ifile>>a;
      firstcards.push_back(a);
      if(j<firstrow*4&&j>=(firstrow-1)*4) {
        rowone.push_back(a);
      }
    }
    ifile>>secondrow;
    for(int j=0; j<16; j++) {
      int a;
      ifile>>a;
      secondcards.push_back(a);
      if(j<secondrow*4&&j>=(secondrow-1)*4) {
        rowtwo.push_back(a);
      }
    }
    int check=0;
    int ans;
    for(int j=0; j<4; j++) {
      for(int k=0; k<4; k++) {
        if(rowtwo.at(k)==rowone.at(j))
        {
          check++;
          ans = rowone.at(j);
        }
      }
    }
    cout<<"Case #"<<i+1<<": ";
    if(check==1) {
      cout<<ans<<endl;
    }
    if(check==0) {
      cout<<"Volunteer cheated!"<<endl;
    }
    if(check>1) {
        cout<<"Bad magician!"<<endl;
    }
  }

}