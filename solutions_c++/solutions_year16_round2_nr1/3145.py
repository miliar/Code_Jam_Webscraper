#include <iostream>
#include <string>
#include <map>
#include <vector>
typedef unsigned int ui;
using namespace std;

vector<string> words = {
  "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

void check(map<char, ui> &char_counts, map<unsigned, ui> &num_counts, char c, ui number){
  ui count = char_counts[c];
  if(count > 0){
    num_counts[number] = count;
    for(auto d : words[number]){
      char_counts[d] -= count;
    }
  }
}

int main(){
  ui t;
  cin >> t;
  for(ui c = 0; c < t; c++){
    string s;
    cin >> s;
    map<char, ui> char_counts;
    for(auto c : s){
      char_counts[c]++;
    }
    map<ui, ui> num_counts;
    check(char_counts, num_counts, 'Z', 0);
    check(char_counts, num_counts, 'W', 2);
    check(char_counts, num_counts, 'X', 6);
    check(char_counts, num_counts, 'S', 7);
    check(char_counts, num_counts, 'V', 5);
    check(char_counts, num_counts, 'F', 4);
    check(char_counts, num_counts, 'O', 1);
    check(char_counts, num_counts, 'G', 8);
    check(char_counts, num_counts, 'I', 9);
    check(char_counts, num_counts, 'T', 3);
    string answer;
    for(auto i : num_counts){
      for(ui j = 0; j < i.second; j++){
        answer += to_string(i.first);
      }
    }
    cout << "Case #" << c + 1 << ": " << answer << endl;
  }
  return 0;
}
