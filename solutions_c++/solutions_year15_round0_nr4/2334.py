#include<iostream>
#include<queue>
using namespace std;
long long T, X, R, C, ret;

int main(){
  cin >> T;
  for (long long t = 0;t < T;++t) {
    cin >> X >> R >> C;
    bool possible = true;
    if (X>R && X>C) possible = false;
    if (X>2 && (R==1 || C==1)) possible = false;
    if (R*C % X > 0) possible = false;
    if (X==4 && (R<3||C<3)) possible = false;
    
    //if (X==3 && R==3 && C==3) possible = false;
    //if (X==4 && R==4 && C==4) possible = false;
    //f (X==4 && (R==4 && C==3)) possible = false;
    //if (X==4 && (R==3 && C==4)) possible = false;
    
    if (possible)
      cout << "Case #" << t+1 << ": GABRIEL" << endl;
    else
      cout << "Case #" << t+1 << ": RICHARD" << endl;
  };

}
