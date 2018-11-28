#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
  ifstream myfile("A-small-attempt2.in");
  ofstream of("output");
  int testcases;
  myfile >> testcases;
  int smax;
  string temp;
  int casenum = 1;
  while(myfile >> smax >> temp) {
    int people = temp[0] - '0';
    int count = 0;
    for (int i = 1; i < smax+1; i++) {
      if (temp[i] > '0' && i > people) {
	count += i - people;
	people += count;
      }
      people += temp[i] - '0';
    }
    of <<"Case #"<<casenum <<": "<<count<<std::endl; 
    casenum++;
  }
  return 0;
}
