// codejam.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

void solve(int n, ifstream& iFile);

string flip(int i, string in);

int main(int argv, char **argc)
{
  if(argv < 2) return 1;
  string s(argc[1]);

  //ofstream oFile(argc[1]);
  //oFile.close();
  //return 1;

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
  string s;
  iFile >> s;

  int count = 0;


  while(true){
    int last_n = -1;
    int first_n = -1;
    for(int i = 0;i < s.size(); ++i){
      if(s[i] == '-' && first_n == -1) first_n = i;
      if(s[i] == '-') last_n = i;
    }
    if(last_n == -1){  //done
      cout << "Case #"<<n<<": "<<count<<std::endl;
      return;
    }
    else{
      if( first_n == 0 ){
        s = flip(last_n, s);
        count++;
      }
      else{
        s = flip(first_n -1, s);
        count++;
      }
    }
  }

  //int N;
  //iFile >> N;
  //if(N == 0 ){
  //  cout <<"Case #"<<n<<": INSOMNIA"<<std::endl;
  //  return;
  //}
  //set<char> digitSet;
  //int count = 1;
  //while(true){
  //  unsigned long long int S = N * count;
  //  string str;
  //  stringstream ss;
  //  ss << S;
  //  ss >> str;

  //  for(int i = 0; i < str.size(); ++i){
  //    digitSet.insert(str[i]);
  //  }
  //  if(digitSet.size() == 10){
  //    cout << "Case #"<<n<<": "<<str<<std::endl;
  //    return;
  //  }
  //  ++count;
  //}
}


string flip(int n, string in)
{
  string end;
  for(int i = n; i >= 0; --i){
    if(in[i] == '+') end.push_back('-');
    else end.push_back('+');
  }
  for(int i = n + 1; i < in.size(); ++i){
    end.push_back(in[i]);
  }
  return end;
}
