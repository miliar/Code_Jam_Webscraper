#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

std::string str_min(std::string str) {
  if(str.length() == 1) {
    return str;
  }
  std::string ret = "";
  for(int i = 1; i < str.length(); i++) {
    if(str.at(i-1) != str.at(i)) {
      ret += str.at(i-1);
    }    
  }
  std::cerr << "Test" << std::endl;
  if(ret == "" || str.at(str.length()-1) != ret.at(ret.length()-1))
    ret += str.at(str.length()-1);

  std::cerr << ret << std::endl;
  return ret;
}

std::string solve(std::vector<std::string> words ) {
  std::cerr << "Start solving " << std::endl;
  std::string comp = str_min(words[0]);
  for(int i = 1 ; i < words.size();i++) {
    if(str_min(words[i]) != comp) {
      return "Fegla Won";
    }
  }
  //Find min actions required
  int nb_of_words = words.size();
  int field [105][105];
  for(int i = 0; i < 105; i++) {
      for(int j = 0; j < 105; j++) {
        field[i][j] = 0;
      }
  }

  int spalten;
  for(int i = 0; i < nb_of_words; i++) {
    int pos = 0;
    field[i][pos]++;
    for(int j = 0; j < words[i].length()-1;j++) {
        if(words[i].at(j) == words[i].at(j+1)) {
          field[i][pos]++;
        } else {
          pos++;
          field[i][pos]++;
        }
      }
    spalten = pos +1;
  }

  int actions = 0;
  for(int i = 0; i < spalten; i++) {
    float avg;
    int sum = 0;
    int best;
    for(int j = 0; j < nb_of_words; j++) {
        sum += field[j][i];
    }
    avg = (float) sum/nb_of_words;
    best = (avg > 0.0) ? (avg + 0.5) : (avg - 0.5);
    for(int j = 0; j < nb_of_words;j++) {
      actions += abs(field[j][i]-best);
    }
  }

  for(int i = 0; i < 105; i++) {
    bool newline = false;
    for(int j = 0; j < 105 ; j++) {
      if(field[i][j] != 0) {
        std::cerr << field[i][j];
        newline = true;
      }
    }
    if(newline)
      std::cerr << std::endl;
  }
  return std::to_string(actions);
}

int main () 
{
	//read input
	freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  freopen("log", "w", stderr);

  int cases;
  scanf("%d", &cases);
  
  for(int ii = 0; ii < cases; ii++ ) {
    printf("Case #%d: ", ii+1);

    //Read input
    int n;
    scanf("%d",&n);

    std::vector<std::string> words;

    for(int i = 0; i < n ; i++) {
      char temp [100];
      std::string str;
      scanf("%s",&temp);
      str = temp;
      words.push_back(str);
    }

    //Output Solution
    printf("%s\n", solve(words).c_str());
  }
	return 0;
}