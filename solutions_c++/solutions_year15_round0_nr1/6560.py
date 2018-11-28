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
using namespace std;

class Ovation{
public:
  void strf(string info)
  {
    stringstream ss(info);
    istream_iterator<string> begin(ss);
    istream_iterator<string> end;
    vector<string> vstrings(begin, end);
    //printV(vstrings);
    int numP=atoi( vstrings[0].c_str() );
    string p=vstrings[1];
    int numF=0;
    int preP=p[0]-48;
    for (int i=1; i<numP+1; i++)
    {
      if (preP<i)
      {
        numF+=i-preP;
	preP=i;
       
      }
      preP+=p[i]-48;
    }
    cout<<numF<<endl;
  }
  void printV(vector<string> x)
  {
    for (int i=0; i<x.size(); i++)
    {
      cout<< x[i]<<" ";
    }
    cout<<endl;
  }
};

int main(int argc, char* argv[])
{
  Ovation mystr;
  string line;
  ifstream myfile(argv[1]);
  int numC;
  myfile>>numC;
  getline(myfile,line);
  for (int i=0; i<numC; i++)
  {
    string info;
    getline(myfile,info);
    cout<<"Case #"<<i+1<<": ";
    mystr.strf(info);
  }
}


