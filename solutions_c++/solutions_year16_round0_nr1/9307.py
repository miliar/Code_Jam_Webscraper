#include <stdio.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

vector<int> parseNumberInArray(int N) {
  vector<int> result;
  int size;
  while (N > 0) {
    result.push_back(N % 10);
    N = N / 10;
  }
  return result;
}

int atOrZero(vector<int> a, int position) {
  if (position < a.size()) {
    return a.at(position);
  } else {
    return 0;
  }
}

vector<int> addUp(vector<int> a, vector<int> b) {
  int resultSize = max(a.size(), b.size()) + 1;
  vector<int> result(resultSize);
  int extra = 0;
  int i = 0;
  while ((i < a.size()) || (i < b.size())) {
    int digitSum = atOrZero(a,i) + atOrZero(b,i) + extra;
    result[i] = digitSum % 10;
    extra = digitSum / 10;

    i++;
  }
  if (extra > 0) {
    result[i] = extra;
  } else {
    result.pop_back();
  }
  return result;
}

int updateDigits(vector<int> a, int digits) {
  int i = 0;
  while (i<a.size()) {
    digits = digits | (1 << a.at(i));
    i++;
  }
  return digits;
}

int backToNumber(vector<int> a) {
  int i = 0, n = 0, p = 1;
  while (i<a.size()) {
    n += p * a.at(i);
    p = p * 10;
    i++;
  }
  return n;
}

int countSheep(int N) {
  if (N == 0) return -1;
  else {
    vector<int> digitArray = parseNumberInArray(N);
    vector<int> sum;
    sum.push_back(0);
    int digits = 0;

    do{
       sum = addUp(sum, digitArray);
       digits = updateDigits(sum, digits);
    }while (digits < 1023);

    return backToNumber(sum);
  }
}

string prettifyResult(int result) {
  if (result == -1)
    return "INSOMNIA";
  else
    return to_string(result);
}

int main(int argc, char const *argv[]) {
  string line;
  ifstream myfile ("CountingSheep1.in");
  ofstream outfile ("CountingSheepB.out");
  if (myfile.is_open() && outfile.is_open()){
    int T, N;
    int c = 1;
    getline(myfile, line);
    stringstream(line) >> T;
    while ( getline(myfile,line) ){
      stringstream(line) >> N;
      outfile << "Case #" << c << ": "<< prettifyResult(countSheep(N)) << "\n";
      c++;
    }
    myfile.close();
    outfile.close();
  } else cout << "Unable to open file";

  return 0;
}
