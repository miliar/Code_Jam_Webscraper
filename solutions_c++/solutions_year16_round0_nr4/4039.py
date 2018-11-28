#include<iostream>
#include<fstream>

using namespace std;

int main() {
  int T;

  ifstream input;
  ofstream output;
  input.open("input.in");
  output.open("output.out");
  input>>T;
  for(int i=0;i<T;i++) {
    int K,C,S;
    input>>K;
    input>>C;
    input>>S;
    output<<"Case #"<<i+1<<":";
    for(int j=0;j<K;j++) {
      output<<" "<<j+1;
    }
    output<<endl;
  }
  input.close();
  output.close();

  return 0;
}
