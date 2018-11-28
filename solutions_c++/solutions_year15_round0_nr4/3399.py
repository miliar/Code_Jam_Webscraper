#include <iostream>
#include <stdio.h>
#include <stdlib.h>  
#include <math.h>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

class Solution{
public:
  string omino(vector<int> info)
  {
    int X=info[0];
    int R=info[1];
    int C=info[2];
    if (X>=7) return "RICHARD";
    else if((R*C)%X!=0) return "RICHARD";
    else if (X-1>R || X-1>C) return "RICHARD";
    else return "GABRIEL"; 
      
  }
  
};


int main(int argc, char* argv[])
{
 
  string line;
  ifstream myfile(argv[1]);
  int numC;
  myfile>>numC;
  getline(myfile,line);
  for (int i=0; i<numC; i++)
  {
    Solution s;
    string info;
    getline(myfile,info);
    stringstream ss(info);
    istream_iterator<string> begin(ss);
    istream_iterator<string> end;
    vector<string> vstrings(begin, end);
    vector<int> myinfo;
    for (int j=0; j<vstrings.size();j++)
    {
      myinfo.push_back(atoi( vstrings[j].c_str() ));
    }
    cout<<"Case #"<<i+1<<": "<<s.omino(myinfo)<<endl;
  }
    
}
