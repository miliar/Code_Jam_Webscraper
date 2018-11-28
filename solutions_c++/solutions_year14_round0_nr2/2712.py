#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>

#define START 2

using namespace std;

int main(){
  int n;
  double c, f, x, cookie_per_sec, cookies, time;
  ifstream input;
  ofstream output;
  
  cout << fixed;
  output << fixed;

  string file;
  cin >> file;

  output.open ("output.out");
  input.open (file);

  input >> n;

  for (int k = 1; k < n+1; k++){
    cookie_per_sec = START;
    time = 0;
    cookies = 0;
    input >> c >> f >> x;
    while (x/cookie_per_sec > ((c/cookie_per_sec) + (x/(cookie_per_sec+f)))){
      time += c/cookie_per_sec;
      cookie_per_sec += f;
    }
    time += x/cookie_per_sec;
    
    output << "Case #" << setprecision(7) << k << ": " << time << endl;
    cout << "Case #" << setprecision(7) << k << ": " << time << endl;

  }
  input.close();
  output.close();

  return 0;
}

    
