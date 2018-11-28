// codejam.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <bitset>
#include <vector>

using namespace std;

#define LOOPI(N) for(int i = 0; i < N; ++i)
#define LOOPJ(N) for(int j = 0; j < N; ++j)

bool inStr(char c, string& str)
{
  int n = str.size();
  for(int i = 0; i < n; ++i){
    if(c == str[i]){
      return true;
    }
  }
  return false;
}

void removeStr(string key, string& str)
{
  int n = key.size();
  int m = str.size();
  for(int i = 0; i < n; ++i){
    for(int j = 0; j < str.size(); ++j){
      if(key[i] == str[j]){
        str.replace(j, 1, 1, ' ');
        break;
      }
  
    }
  }
}

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
  string input;
  iFile >> input;

  vector<int> result;
  while(inStr('Z', input)){
    removeStr("ZERO", input);
    result.push_back(0);
  };
  while(inStr('W', input)){
    removeStr("TWO", input);
    result.push_back(2);
  };
  while(inStr('G', input)){
    removeStr("EIGHT", input);
    result.push_back(8);
  };
  while(inStr('X', input)){
    removeStr("SIX", input);
    result.push_back(6);
  };
  while(inStr('H', input)){
    removeStr("THREE", input);
    result.push_back(3);
  };
   while(inStr('R', input)){
    removeStr("FOUR", input);
    result.push_back(4);
  };
   while(inStr('F', input)){
    removeStr("FIVE", input);
    result.push_back(5);
  };
   while(inStr('V', input)){
    removeStr("SEVEN", input);
    result.push_back(7);
  };
   while(inStr('O', input)){
    removeStr("ONE", input);
    result.push_back(1);
  };
   while(inStr('N', input)){
    removeStr("NINE", input);
    result.push_back(9);
  };

  for(int i = 0 ;i < result.size(); ++i){
    for(int j = i + 1; j < result.size(); ++j){
      if(result[i] > result[j]){
        int tmp = result[i];
        result[i] = result[j];
        result[j] = tmp;
      }
    }
  }
 
  cout << "Case #"<<n<<": ";
  int m = result.size();
  for(int j = 0; j < m; ++j){
    cout << result[j];
  }
  cout << endl;
}



