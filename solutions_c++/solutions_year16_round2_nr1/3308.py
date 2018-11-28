#include <vector>
#include <string>
#include <iostream>
using namespace std;

int main() {
  int cases;
  cin >> cases;

  for (int i = 0; i < cases; i++) {
    cout << "Case #"<< i + 1 <<": ";
    string a;
    cin >> a;
    int Us = 0;
    int Fs = 0;
    int Os = 0;
    int fives = 0;
    int fours = 0;
    int twos = 0;
    int ones = 0;
    int zeros = 0;
    int eights = 0;
    int threes = 0;
    int sixes = 0;
    int sevens =0;
    int nines = 0;
    int Vs = 0;
    int Ns = 0;
    int Rs = 0;
    int Ss = 0;
    for (int z = 0; z < a.size(); z++) {
     if (a[z] == 'Z') {
       zeros++;
     }
     if (a[z] == 'S') {
       Ss++;
     }
     if (a[z] == 'O') {
       Os++;
     }
     if (a[z] == 'G') {
       eights++;
     }
     if (a[z] == 'W') {
       twos++;
     }
     if (a[z] == 'U') {
       fours++;
     }
     if (a[z] == 'F') {
       Fs++;
     }
     if (a[z] == 'U') {
       Us++;
     }
     if (a[z] == 'V') {
       Vs++;
     }
     if (a[z] == 'X') {
       sixes++;
     }
     if (a[z] == 'N') {
       Ns++;
     }
     if (a[z] == 'R') {
       Rs++;
     }
  }
  fives = Fs - Us;
  ones = Os - twos - fours - zeros; 
  sevens = Ss - sixes;
  nines = (Ns - ones - sevens) / 2;
  threes = Rs - fours - zeros;
  for (int k = 0; k < zeros; k++) 
    cout << "0";

  for (int k = 0; k < ones; k++) 
    cout << "1";
  
  for (int k = 0; k < twos; k++) 
    cout << "2";
  
  for (int k = 0; k < threes; k++) 
    cout << "3";
  
  for (int k = 0; k < fours; k++) 
    cout << "4";
  
  for (int k = 0; k < fives; k++) 
    cout << "5";

  for (int k = 0; k < sixes; k++) 
    cout << "6";
  
  for (int k = 0; k < sevens; k++) 
    cout << "7";
  
  for (int k = 0; k < eights; k++) 
    cout << "8";
  
  for (int k = 0; k < nines; k++) 
    cout << "9";
    
  cout << endl;
  }
  return 0;
}
