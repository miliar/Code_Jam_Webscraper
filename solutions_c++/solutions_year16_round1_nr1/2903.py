#include <algorithm>
#include <iostream>
#include <deque>
#include <iterator>
using namespace std;

int main()
{
   int t;
   cin >> t;
   cin.ignore(numeric_limits<streamsize>::max(), '\n');
   for (int tt = 1; tt <= t; ++tt) {
      string line;
      getline(cin, line);
      reverse(line.begin(), line.end());

      deque<char> last_word;
      last_word.push_front(line.back());
      line.pop_back();
      while (!line.empty()) {
         if (last_word.front() <= line.back())
            last_word.push_front(line.back());
         else
            last_word.push_back(line.back());
         line.pop_back();
      }

      cout << "Case #" << tt << ": ";
      copy(last_word.begin(), last_word.end(), ostream_iterator<char>(cout, ""));
      cout << '\n';
   }
}
