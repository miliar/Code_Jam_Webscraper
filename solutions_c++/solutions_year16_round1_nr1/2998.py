#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv){

  int numTestCases = 0;

  cin >> numTestCases;

  for (int t = 0; t < numTestCases; t++){
    string s;
    cin >> s;

    string output;
    output += s[0];

    for (int i = 1; i < s.length(); i++){
      char c = s[i];
      if (c >= output[0]){
        output.insert(0, 1, c);
      } else {
        output = output += c;
      }
    }

    cout << "Case #" << (t+1) << ": " << output << endl;
  }


  return 0;
}
