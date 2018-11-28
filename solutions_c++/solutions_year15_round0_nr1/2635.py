#include<bits/stdc++.h>

using namespace std;

const int MAX_SHYNESS = 1000 + 111;

const char INPUT[] = "HelloWorld.inp";
const char OUTPUT[] = "HelloWorld.out";

int main(void){
  freopen(INPUT, "r", stdin);
  freopen(OUTPUT, "w", stdout);

  int shyness[MAX_SHYNESS];

  int numTest;
  cin >> numTest;

  for (int idTest = 0; idTest < numTest; ++ idTest){
    int numShy;
    cin >> numShy;

    int result = 0; int count = 0;
    for (int idShy = 0; idShy <= numShy; ++ idShy){
      char temp;
      cin >> temp;
      //cerr << "\'" << temp << "\' ";
      if (temp - '0' != 0 && idShy > count){
        result += idShy - count;
        count = idShy;
      }
      count += temp - '0';
    }

    cout << "Case #" << (idTest + 1) << ": " << result << endl;
  }

  return 0;
}
