#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
  ifstream in("A-small-attempt0.in");
  ofstream out("a1.txt");
  int T;
  in >> T;
  for (int poo = 0; poo < T; poo ++){
    int r, t;
    in >> r >> t;
    
    int guess = 2;
    int prevsum, cursum;
    while(true){
      cursum = 0;
      for (int i = r; i < r+guess; i++){
	if ((i-r)%2 == 0) cursum -= i*i;
	else if ((i-r)%2==1) cursum += i*i;
      }
      if (cursum > t) break;
      else guess += 2;
    }
    guess -= 2;
    out << "Case #" << poo+1 << ": " << guess/2 << endl;
  }
  return 0;
}
