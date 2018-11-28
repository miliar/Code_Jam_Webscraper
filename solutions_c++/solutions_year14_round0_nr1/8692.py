#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void compare(const vector<int>& left, const vector<int>& right, ofstream& out);

int main ()
{  
  ifstream infile("A-small-attempt1.in");
  ofstream outfile("hi.txt");
  
  int numtestcases;
  infile >> numtestcases;
  
  //test cases
  for(int i = 0; i < numtestcases; i++) {
      vector<vector<vector<int> > > arrange;
      arrange.resize(2);
      
      vector<int> choice;
      
    //each round
    for(int j = 0; j < 2; j++) {
      arrange[j].resize(4);
      int userchoice;
      infile >> userchoice;
      choice.push_back(userchoice);
      
      //rows
      for(int k = 0; k < 4; k++) {
        //column
        for(int l = 0; l < 4; l++) {
          int num;
          infile >> num;
          arrange[j][k].push_back(num);
        }
      }
    }
    outfile << "Case #" << (i+1) << ": "; 
    compare(arrange[0][choice[0]-1], arrange[1][choice[1]-1], outfile);
    outfile << endl;
  } 
  return 0;
}

void compare(const vector<int>& left, const vector<int>& right, ofstream& outfile) {
  bool found = false;
  int ret = 0;
  for(int i = 0; i < left.size(); i++) {
    for(int j = 0; j < right.size(); j++) {
      if(left[i] == right[j]) {
        if(found) {
          outfile << "Bad magician!";
          return;
        }
        
        ret = left[i];
        found = true;
      }
    }
  }
  
  if(found) {
    outfile << ret;
  } else {
    outfile << "Volunteer cheated!";
  }
}
 
