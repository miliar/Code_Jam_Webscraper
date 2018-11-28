/go down until there is a different pancake
//flip all first pancakes
//repeat

#include<iostream>
#include<string>
#include<fstream>
#include<cstdlib>
using namespace std;

int main(){
  string sin;
  int numIn;
  ifstream ifs;
  ifs.open("p.txt");
  getline(ifs,sin);
  numIn = atoi(sin.c_str());

  for(int i = 0; i < numIn; i++){
    string s;
    getline(ifs, s);
    int diff = 0;
    char curr = s[0];
    for(int j = 0; j < s.length(); j++){
      if (s[j] != curr){
        curr = s[j];
        diff++;
      }
    }
    //cout << "last char: " << s[s.length() -1] << endl;
    if (s[s.length() -1] == '-'){
      diff++;
    }
    cout << "Case #" << i+1 << ": " << diff << endl;
  }

}

