#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

static bool isPalindrome(int n) {
  stringstream ss;
  ss << n;
  string str = ss.str();
  int front = 0;
  int back = str.length() - 1;
  while (front < back) {
    if (str[front] != str[back]) {
      return false;
    }
    front++;
    back--;
  }
  return true;
}

int main(int argc, char** argv) {

  int debug = false;
  int T = 0;
  cin >> T;
  for (int t = 0; t < T; t++) {
 
    int A = 0, B = 0;
    int count = 0;
    cin >> A;
    cin >> B;
    queue<queue<int>*> processed;
    int rootB = ceil(sqrt(B));
    int rootA = ceil(sqrt(A));
    for (int i = rootA; i <= rootB; i++) {
      int n = i;
      if (debug) {
        cout << "n: " << n << endl;
        cout << "processed.size(): " << processed.size() << endl;
      }
      if (processed.size() == 0 || (processed.front())->front() != n) {
        int cn = -1;
        queue<int>* squares = new queue<int>();
        // special case: n = 1
        if (n == 1) {
          cn = 1;
        } else {
          while (n <= B && isPalindrome(n)) {
            if (debug) {
              if ((n*n) <= B) {
                cout << "found palindrome " << n << ", checking " << (n*n) << " now." << endl;
              } else {
                cout << "found palindrome " << n << endl;
              }
            }
            n = n * n;
            squares->push(n);
            cn++;
          }
          processed.push(squares);
        }
        if (cn > 0) {
          count += cn;
        }
      } else {
        if (debug) {
          cout << "Skipping " << n << endl;
        }
        // front of squares == current number n
        queue<int>* squares = processed.front();
        processed.pop();
        squares->pop();
        processed.push(squares);
      }
    }    

    cout << "Case #" << (t+1) << ": " << count << endl;
  }
}
