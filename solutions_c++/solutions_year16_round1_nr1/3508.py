//Joe Snider
//4/16
//
//q1, last word

#include <algorithm>
#include <vector>
#include <deque>
#include <iostream>
#include <string>
#include <iterator>
#include <math.h>

using namespace std;

void dfs(deque<char> board, deque<char>& cur, deque<char>& best) {
    if(board.size() == 0) {
        if (lexicographical_compare(best.begin(), best.end(), cur.begin(), cur.end())) {
            best.assign(cur.begin(), cur.end());
        }
    } else {
        char l = board[0];
        board.pop_front();
        deque<char> c1(cur.begin(), cur.end());
        c1.push_front(l);
        deque<char> c2(cur.begin(), cur.end());
        c2.push_back(l);
        if(lexicographical_compare(c2.begin(), c2.end(), c1.begin(), c1.end())) {
           dfs(board, c1, best);
        } else {
           dfs(board, c2, best);
        }
    }
}

int main() {
   int T;
   cin >> T;
   string line;
   for(int i = 0; i < T; ++i) {
      cin >> line;
      deque<char> board;
      deque<char> cur;
      deque<char> best;
      board.assign(line.begin(), line.end());
      cur.push_back(board[0]);
      board.pop_front();
      best.assign(line.begin(), line.end());
      dfs(board, cur, best);
      cout << "Case #" << i+1 << ": ";
      for(int j = 0; j < best.size(); ++j) {
         cout << best[j];
      }
      cout << "\n" << flush;
   }
   return 0;
}
