#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>

//#define VERBOSE

using namespace std;

void solve(int size, const vector<int> &s, int c);

int main(int argc, char **argv){
  if(argc<2){ cerr << "no input file" << endl; exit(0);}

  ifstream in;
  in.open(argv[1]);
  int num_cases=0;
  if(in.good()){
    in >> num_cases;
  }
  int c=0;
  int s_size;
  string digits;
  while(in >> s_size >> digits){
    c++;   
    vector<int> s;
    for(const auto d:digits){
      s.push_back(atoi(&d));
    }
    
    
    solve(s_size,s,c);
    
#ifdef VERBOSE    
    cout << s_size << "\t:\t";
    for(const auto v:s){
      cout << " " << v;
    }
    cout << endl;
#endif
    
  }
  
  
}

void solve(int size, const vector<int> &s, int c){
  if(size+1!=s.size()){
    cerr << "line size and vector size don't match." << endl;
    exit(1);
  }

  long invited=0;
  long sum=0;
  for(unsigned int i=0;i<s.size();++i){
    if(sum<i){
      invited+=i-sum;
      sum+=i-sum;
    }
    sum+=s[i];
  }
  cout << "Case #" << c << ": " << invited << endl;
  
}
