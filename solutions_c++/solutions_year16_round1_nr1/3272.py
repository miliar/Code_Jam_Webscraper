# include <iostream>
# include <string>
# include <cstdlib>
# include <string.h>
# include <deque>


using namespace std;

int main() {
  int n;
  cin >> n;
  for ( int i = 1 ; i <= n ; i++) {
    string str;
    deque<char> q;
    cin >> str;
    q.push_back(str.at(0));
    for ( int j = 1 ; j < str.size() ; j++ ) {
      char tmp = str.at(j);
      if ( tmp < q.front() ) {
        q.push_back(tmp);
      } // if
      else {
        q.push_front(tmp);
      } // else
    } // for
    cout << "Case #" << i << ": ";
    while ( !q.empty() ) {
      cout << q.front();
      q.pop_front();
    } // while
    cout << endl;
  } // for
  return 0;
} // main()
