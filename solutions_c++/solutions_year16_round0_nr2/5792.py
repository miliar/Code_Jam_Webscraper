#include <string>
#include <fstream>
#include <iostream>
#include <vector>


using namespace std;
int flip(string vec);
int main(){
  
  fstream fin, fout;
  fin.open("B-large.bin");
  fout.open("output.out");
  if (!fin.is_open()) {
    cout << "in file was not open" << endl;
  }
  if (!fout.is_open()) {
    cout << "out file was not open" << endl;
  }
  int test_num;
  fin >>  test_num;
 for (int i = 0; i < test_num; i++) {
   string s;
   fin >> s;

   int result = flip(s);
  
   fout << "Case #" << i+1 << ": " << result << endl;
   
 }  
 
  fin.close();
  fout.close();
 
  return 0;
}
int flip(string s){
  int len = s.size();
  int res = 0;
  bool check = false; // + : true; - : false
  if (s[0] == '+') check = true;
  for (int i = 1; i < len; i++) {
    if (check && s[i] == '+'){
      res += 0;
      check = true;
    }
    else if (check &&  s[i] == '-'){
      res += 1;
      check = false;
    }
    else if (!check && s[i] == '-') {
      // - and -
      res += 0;
      check = false;
    }
    else{
      // - and +
      res += 1;
      check = true;
    }
  }
  if (check == false) return res+1;
  return res;
}
