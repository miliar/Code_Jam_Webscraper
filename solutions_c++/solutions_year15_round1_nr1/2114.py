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

class Solution{
public:
  vector<int> minNum(int n, vector<int> numM)
  {
    int res1=0;
    int res2=0;
    vector<int> res;
    double max=0.0;
    for (int i=1; i<n; i++)
    {
      if (numM[i-1]-numM[i]>=0)
      {
         res1+=numM[i-1]-numM[i];
         if (max<numM[i-1]-numM[i])
	 {
	   max=double(numM[i-1]-numM[i]);
	 }
      }
    }
    double rate=max/10;
    for (int j=0; j<n-1; j++)
    {
      if (numM[j]<max)
      {
	res2+=numM[j];
      }
      else
      {
        res2+=max;
      }
    }
    res.push_back(res1);
    res.push_back(res2);
    return res;
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
    string Dstring;
    string Pstring;
    getline(myfile,Dstring);
    getline(myfile,Pstring);
    int numD=atoi(Dstring.c_str());
    stringstream ss(Pstring);
    istream_iterator<string> begin(ss);
    istream_iterator<string> end;
    vector<string> vstrings(begin, end);
    vector<int> numPs;
    for (int j=0; j<vstrings.size(); j++)
    {
      numPs.push_back(atoi(vstrings[j].c_str()));
    }
   
    Solution myS;
    vector<int> res=myS.minNum(numD,numPs);
    cout<<"Case #"<<i+1<<": "<<res[0]<<" "<<res[1]<<endl;
    
  }
}
