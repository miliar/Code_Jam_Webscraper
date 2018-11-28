#include <iostream>
#include <vector>
using namespace std;

void SleepResult(long input);
void ArrayAdd(vector<int>& seen, int toadd);

int main(int argc, char* argv[]) {
  int trials;
  cin >> trials;
  long temp;
  for (int i = 0; i < trials; i++) {
    cin >> temp;
    cout << "Case #" << i+1 << ": ";
    SleepResult(temp);
    cout << endl;
  }
  return 0;
}


void SleepResult(long input) {
  if (input == 0)
    cout << "INSOMNIA";
  else {
    vector<int> seen;
    long n = 1;
    long currentInput;
    long output;
    while(seen.size() != 10) {
      currentInput = n * input;
      output = n*input;
      while(currentInput) {
        ArrayAdd(seen, currentInput%10);
        currentInput /= 10;
      }
      n++;
    }
    cout << output;
  }
}

void ArrayAdd(vector<int>& seen, int toadd) {
  bool addflag = true;
  for (int i = 0; i < seen.size(); i++) {
    if (seen.at(i) == toadd)
      addflag = false;
  }
  if (addflag)
    seen.push_back(toadd);
}
