#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <queue>
#include <iostream>
#include <string>

using namespace std;

struct Pos {
  char ch;
  int count;

  Pos(char ch,int count) : ch(ch),count(count) { }
};

int N;
vector< vector< Pos > > words;


void readData() {
  cin >> N;
  words.resize(N);
  for (int i = 0;i < N;i++) {
    string st;
    cin >> st;
    words[i].clear();
    char last = '-';
    for (int j = 0;j < (int)st.size();j++) {
      if (st[j] != last) {
        words[i].push_back(Pos(st[j],1));
        last = st[j];
      } else {
        words[i].back().count++;
      }
    }
  }

  //debug
/*   for (auto &x : words) {
 *     for (auto &a : x) {
 *       for (int i = 0;i < a.count;i++) cout << a.ch;
 *     }
 *     cout << endl;
 *   }
 */
}

int result;

int process() {
  //check impossible
  int length = -1;
  for (auto &w : words) {
    if (length == -1) length = (int)w.size();
    else if (length != (int)w.size()) {
        return -1;
    }
  }
  int result = 0;
  for (int i = 0;i < length;i++) {
    for (int j = 1;j < (int)words.size();j++) {
      if (words[j][i].ch != words[0][i].ch) return -1;
    }
    int sum = 0;
    for (auto &w : words) {
      sum += w[i].count;
    }
    int avg = sum / N;

    int a = 0;
    for (auto &w : words) {
      a += fabs(avg - w[i].count);
    }
    int b = 0;
    for (auto &w : words) {
      b += fabs((avg+1) - w[i].count);
    }
    //printf("at pos %d (char = %c), a = %d, b = %d\n",i,words[0][i].ch,a,b);
    if (a < b) result += a; else result += b;
  }
  return result;
}


int main() {
  freopen("A-small-attempt0.in","r",stdin);
  int T;
  cin >> T;
  int case_id = 0;
  while (T--) {
    case_id++;
    readData();
    int result = process();
    if (result == -1) 
      cout << "Case #" << case_id << ": Fegla Won" << endl; 
    else
      cout << "Case #" << case_id << ": " << result << endl; 
  }
}
