#include<iostream>
#include<fstream>
#include<string>
#include<unordered_set>
using namespace std;

int find(int num) {
  unsigned long long mul = 0;
  int count = 0, k = 0;
  unordered_set<int> mp1;
  for (unsigned long long i = 1; i < 10000000; i++) {
    mul = i * num;
    while (mul != 0) {
      k = mul % 10;
      if (mp1.find(k) == mp1.end()) {
        mp1.emplace(k);
        count++;
      }
      if (count == 10)
        return i;
      mul = mul / 10;
    }
  }
  return -1;
}
int main() {
    ifstream infile;
    infile.open("/Users/mac/code/c++/A-large.in");
    if (infile.fail()) cout << "open file fail" <<endl;
    ofstream outfile;
    outfile.open("/Users/mac/code/c++/cj1_output2.txt", ios::out | ios::app);
    int num = 0;
    int input = 0;
    infile >> num;
    for (int k = 0; k < num; k++) {
        infile >> input;
        int result = find(input);
        if (result != -1)
          outfile << "Case #"<<k+1<<": "<< result * input <<endl;
        else
          outfile << "Case #"<<k+1<<": "<< "INSOMNIA" <<endl;
    }
    return 0;
}
