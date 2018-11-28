#include <bits/stdc++.h>
using namespace std;


#define endl '\n'

int count(string str){
  int res=0;
  int ptr=0;
  if(str[0]=='-'){
    while(str[ptr]=='-'){
      str[ptr] = '+';
      ptr++;
    }
    res++;
  }
  while(ptr<str.length()){
    if(str[ptr]=='-'){
      while(str[ptr]=='-'){
        str[ptr] = '+';
        ptr++;
      }
      res+=2;
    }
    ptr++;
  }
  return res;
}

int main() {
  ios_base::sync_with_stdio(false);cin.tie(0);
  ifstream fin("input.in");
  ofstream fout("output.out");
  
  if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
  if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
  
  int numCase;
  fin >> numCase;
  //Write your code here
  string s;
  for(int i=0; i<numCase; i++) {
    fin >> s;
    fout << "Case #" << i+1 << ": "<< count(s) << endl;
  }
  
  fin.close();
  fout.close();
  return 0;
}
