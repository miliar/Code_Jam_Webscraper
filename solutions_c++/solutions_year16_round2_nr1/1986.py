#include <iostream>
#include <string>
#include <vector>

using namespace std;

class LetterCounter {
 public:
  LetterCounter() : count(26,0), solution(10,0) {}
  void addLetters(const string S) {
    for (auto c : S) {
      int index = getIndex(c);
      count[index]++;
    }
  }

  void process() {
    handle0();
    handle2();
    handle6();
    handle8();
    handle3();
    handle7();
    handle5();
    handle4();
    handle9();
    handle1();
  }

  void handle0() {
    int nZ = getCount('Z');
    solution[0] = nZ;
    remove('O',nZ);
  }
  void handle2() {
    int nW = getCount('W');
    solution[2] = nW;
    remove('O',nW);
  }
  void handle6() {
    int nX = getCount('X');
    solution[6] = nX;
    remove('S',nX);
    remove('I',nX);
  }
  void handle8() {
    int nG = getCount('G');
    solution[8] = nG;
    remove('I',nG);
    remove('H',nG);
  }
  void handle3() {
    int nH = getCount('H');
    solution[3] = nH;
  }
  void handle7() {
    int nS = getCount('S');
    solution[7] = nS;
    remove('V',nS);
  }
  void handle5() {
    int nV = getCount('V');
    solution[5] = nV;
    remove('I',nV);
    remove('F',nV);
  }
  void handle4() {
    int nF = getCount('F');
    solution[4] = nF;
    remove('O',nF);
  }
  void handle9() {
    int nI = getCount('I');
    solution[9] = nI;
  }
  void handle1() {
    int nO = getCount('O');
    solution[1] = nO;
  }
  string produceNumber() {
    string number = "";
    for(int i = 0; i < 10; ++i) {
      for (int j=0; j < solution[i]; ++j)
        number += to_string(i);
    }
    return number;
  }

 private:
  int getIndex(char c) const {
    return static_cast<int>(c-'A');
  }
  int getCount(char c) const {
    return count[getIndex(c)];
  }
  void remove(char c, int N) {
    count[getIndex(c)] -= N;
  }

  vector<int> count;
  vector<int> solution;
};

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    string S;
    cin >> S;

    LetterCounter lc;
    lc.addLetters(S);
    lc.process();
    string number = lc.produceNumber();

    cout << "Case #" << t << ": " << number << endl;
  }

}