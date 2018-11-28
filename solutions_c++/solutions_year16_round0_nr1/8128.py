#include<iostream>
#include<fstream>

using namespace std;

int main() {
  
  int t, digits[10], n, count = 0, it;
  long long temp;

  ifstream fin;
  fin.open("A-small-attempt0.in");
  ofstream fout;
  fout.open("out1.txt");

  fin >> t;

  for (int k = 0; k < t; k++) {
    
    fin >> n;

    if (n == 0) {
      fout << "Case #" << k+1 << ": " << "INSOMNIA" << endl;
      continue;
    }

    for (int i = 0; i < 10; i++) digits[i] = 0;
    count = 0; it = 1;

    temp = n;
    while (count < 10) {
      
      while(temp > 0) {
        if (digits[temp%10] == 0) {
          digits[temp%10] = 1;
          count++;
        }
        temp /= 10;
      }

      temp = n;
      it += 1;
      temp *= it;
    }

    fout << "Case #" << k+1 << ": " << (temp/it) * (it-1) << endl;
  }

  return 0;
} 


