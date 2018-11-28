#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int main(int argc, char *argv[]) {

  if (argc != 3) {
    cout << "Useage: a.out file_in file_out" << endl;
    return -1;
  }


  ifstream file_in;
  ofstream file_out;
  file_in.open(argv[1]);
  file_out.open(argv[2]);

  int T;
  string word;
  int length;
  char max;
  int max_i;
  vector<char> fronts;
  list<char> ordered;

  file_in >> T;

  for (int t = 1; t <= T; t++) {
    file_in >> word;
    length = word.length();
    fronts.clear();
    ordered.clear();
    while (length > 0) {
      max = word[0];
      max_i = 0;
      for (int i = 1; i < length; i++) {
        if (word[i] >= max) {
          max = word[i];
          max_i = i;
        }
      }
      fronts.push_back(max);
      //cout << max << endl;
      length = max_i;
    }
    for (int i = 0; i < word.length(); i++) {
      if (word[i] == fronts.back()) {
        ordered.push_front(word[i]);
        fronts.pop_back();
      }
      else {
        ordered.push_back(word[i]);
      }
    }

    file_out << "Case #" << t << ": ";
    for (auto itr = ordered.begin(); itr != ordered.end(); ++itr) {
      //cout << *itr;
      file_out << *itr;
    }
    //cout << endl;
    file_out << endl;

  }

  file_in.close();
  file_out.close();
  return 0;
}
