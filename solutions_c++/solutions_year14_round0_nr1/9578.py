#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void Print(const vector<vector<int> >& v) {
  for (int q = 0; q < v.size(); q++) {
    for (int w = 0; w < v[q].size(); w++) {
      cerr << v[q][w] << " ";
    }
    cerr << endl;
  }


}

bool equal(const vector<vector<int> >& v, const vector<vector<int> >& v2) {
  bool Equal = true;
  for (int q = 0; q < 4; q++)
    for (int w = 0; w < 4; w++) {
      if (v[q][w] != v2[q][w])
        Equal = false;
    }
  return Equal;
}

int main() {
  ifstream in;
  in.open("test2.txt");
  int testCases;
  int caseNum = 1;
  in >> testCases;
  //cout << "testCases  "<< testCases<<endl;
  vector< vector<int> > v;
  vector< vector<int> > v2;

  int Dumm;
  while (caseNum <= testCases) {
    bool found = false;
    bool cheated = false;
    bool badMagic = false;
    string result;
    
    int answer, numAnswers;
    numAnswers=0;
    int num1, num2;
    in >> num1;

    v.resize(4, vector<int>(4, 0));
    v2.resize(4, vector<int>(4, 0));

    for (int i = 0; i < 4; i++) {
      for (int d = 0; d < 4; d++) {
        in >> Dumm;
        //cout<< Dumm;
        v[i][d] = (Dumm);
      }
    }
    in >> num2;
    for (int j = 0; j < 4; j++) {
      for (int h = 0; h < 4; h++) {
        in >> Dumm;
        v2[j][h] = (Dumm);
      }
    }

    num1 = num1 - 1;
    num2 = num2 - 1;
    for (int k = 0; k < 4; k++) {
      for (int z = 0; z < 4; z++) {
        if (v[num1][k] == v2[num2][z]) {
          found = true;
          answer = v[num1][k];
          numAnswers++;
          if (found && numAnswers>1) {
            found = false;
            badMagic = true;
            result = "Bad magician!";
          }
        }

      }
    }
    if (!found && !badMagic) {
      cheated = true;
      result = "Volunteer cheated!";
    }
    if (found)
      cout << "Case #" << caseNum << ": " << answer << endl;
    else if (cheated || badMagic)
      cout << "Case #" << caseNum << ": " << result << endl;
    caseNum++;
  }
}