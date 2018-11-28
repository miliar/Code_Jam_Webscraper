#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>

using namespace std;

#define ll long long
#define pii pair<int,int>

int N,T;

ifstream fin("A.in");
ofstream fout("A.out");

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    string input;
    fin >> input;
    N = input.length();
    stack<int> todo;
    ll ans=0;
    for (int i = 0; i < N; i++) {
      int next;
      if (input[i] == 'C') next = 0;
      else next = 1;
      if ((!todo.empty() && todo.top() == next) || todo.size() == N-i) {
        //cout << "Removed " << next << "\n";
        if (todo.top() == next) ans += 10;
        else ans += 5;
        todo.pop();
      }
      else {
        //cout << "Added " << next << "\n";
        todo.push(next);
      }
    }
    fout << "Case #" << tt << ": " << ans << "\n";
  }
  return 0;

}