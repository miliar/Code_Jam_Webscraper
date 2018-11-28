// codejam.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <bitset>
#include <vector>
#include <cmath>
#include <algorithm>

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

int sum(vector<int> a)
{
  int sum_ = 0;
  LOOPI(a.size()){
    sum_ += a[i];
  }
  return sum_;
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
  int sz;
  iFile >> sz;

  vector<int> a(sz);

  for(int i = 0; i < sz; ++i){
    iFile >> a[i];
  }

  string s;

  while(sum(a)!= 0 ){
    //check
    int sum_ = sum(a);
    LOOPI(a.size()){
      if(a[i] > sum_/2.0){
        return;
      }
    }

    if(sum(a) == 2){
      LOOPI(a.size()){
        if(a[i] == 1){
          a[i]--;
          s+='A' + i;
        }
      }
      s+= " ";
      continue;
    }

    int max  = 0;
    LOOPI(a.size()){
      if(a[i] > max) max = a[i];
    }
    LOOPI(a.size()){
      if(a[i] == max){
        a[i]--; 
        s += string(1, char('A' + i));
        break;
      }
    }
    if(sum(a) % 2== 1){
      LOOPI(a.size()){
        if(a[i] == max){
          a[i]--; 
          s += string(1, char('A' + i));
          break;
        }
      }
    }
    s+= " ";
  }


  cout << "Case #"<<n<<": ";
  cout << s;
  cout << endl;
}



