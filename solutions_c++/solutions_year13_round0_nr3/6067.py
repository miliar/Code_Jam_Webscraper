#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;


int main(){
  int times;
  cin >> times;
  int count = 0;
  int a, b;
  ofstream Outfile;
  Outfile.open("Output.out");
  for(int y = 1; y<=times; y++){
    count = 0;
    cin >> a >> b;
    for(int x = a; x <=b; x++){
      int root = round(sqrt(x));
      if(x != root*root){
        continue;
      }
      bool pass = true;
      string A, B;
      stringstream ss, s2;
      ss << x;
      s2 << root;
      A = ss.str();
      B = s2.str();
      pass = true;
      int len = A.length()-1;
      for(int q = 0; q<=len; q++){
        if(A[q] == A[len-q]){
          continue;
        }else{
          pass = false;
          break;
        }
      }
      if(pass){
        len = B.length() -1;
        for(int q = 0; q<=len; q++){
          if(B[q] == B[len-q]){
            continue;
          }else{
            pass = false;
            break;
          }
        }
      }
      if(pass){
        count++;
      }
      
    }
    Outfile << "Case #" << y <<": " << count << endl;

  }
  Outfile.close();
}
