// codejam.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

void solve(int n, ifstream& iFile);

int main(int argv, char **argc)
{
  if(argv < 2) return 1;
  string s(argc[1]);

  ifstream iFile(argc[1]);
  
  int n = 0;

  if(iFile.good()) {
    iFile >> n;
  }
  else return 1;

  for(int i = 1; i <= n; i++){
    solve(i, iFile);
  }
  return 0;
}

void solve(int n, ifstream& iFile)
{
  int N;
  iFile >> N;
  if(N == 0 ){
    cout <<"Case #"<<n<<": INSOMNIA"<<std::endl;
    return;
  }
  set<char> digitSet;
  int count = 1;
  while(true){
    unsigned long long int S = N * count;
    string str;
    stringstream ss;
    ss << S;
    ss >> str;

    for(int i = 0; i < str.size(); ++i){
      digitSet.insert(str[i]);
    }
    if(digitSet.size() == 10){
      cout << "Case #"<<n<<": "<<str<<std::endl;
      return;
    }
    ++count;
  }
}

