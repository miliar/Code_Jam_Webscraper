#include<iostream>
#include<fstream>
#include<string>
#include<queue>
using namespace std;

int DP(string &S) {
  vector<int> list(S.length() + 1, 0);
  for (int i = 1; i < list.size(); i++) {
    if (S[i-1] == '+') {
      list[i] = list[i-1];
    } else {
      if (i > 1 && S[i-1] != S[i-2])
        list[i] = list[i-1] + 2;
      else if (i > 1 && S[i-1] == S[i-2])
        list[i] = list[i-1];
      else
        list[i] = 1;
    }
  }
  return list[S.length()];
}

int main() {
    ifstream infile;
    infile.open("/Users/mac/code/c++/B-large.in");
    if (infile.fail()) cout << "open file fail" <<endl;
    ofstream outfile;
    outfile.open("/Users/mac/code/c++/cj2_output4.txt", ios::out | ios::app);
    int num = 0;
    string S;
    infile >> num;
    for (int k = 0; k < num; k++) {
        infile >> S;
        int result = DP(S);
        cout << "Case #"<<k+1<<": "<< result <<endl;
        outfile << "Case #"<<k+1<<": "<< result <<endl;
    }
    return 0;
}
