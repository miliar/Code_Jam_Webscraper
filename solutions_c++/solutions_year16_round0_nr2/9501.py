#include <iostream>
using namespace std;

void pancake(string P) {
    int flip = 0;
    char c = P[0];
    for (int i = 0; i < P.size(); i++)
    {
        if (c!=P[i])
        {
            c=P[i];
            flip++;
        }
    }
    if(c=='-'){
        flip++;
    }
    cout << flip;
}

int main() {
  int t;
  string P;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> P;
    cout << "Case #" << i << ": ";
    pancake(P);
    cout << endl;
  }
}
