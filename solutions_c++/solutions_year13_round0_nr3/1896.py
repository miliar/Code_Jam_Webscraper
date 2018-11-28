#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef unsigned long long ulld;

bool is_palindrome (ulld X) {
  ulld original = X;
  ulld reversed = 0LL;
  while (X) {
    ulld dig = X%10;
    reversed *= 10;
    reversed += dig;
    X /= 10;
  }
  return (original == reversed) ? true : false;
}

int main ()
{
  int T;
  cin >> T;
  vector<ulld> fair_square;
  for (ulld x = 1LL; x <= 10000000LL; x++) {
    if (is_palindrome(x)) {
      ulld square = x * x;
      if (is_palindrome(square)) {
        fair_square.push_back(square);
      }
    }
  }
  for (int t = 0; t < T; t++) {
    ulld A, B;
    cin >> A >> B;
    int counter = 0;
    for(vector<ulld>::iterator it = fair_square.begin();
        it != fair_square.end();
        it++) {
      if (*it >= A && *it <= B)
        counter++;
    }
    cout << "Case #" << t+1 << ": " << counter << endl;
  }
}
