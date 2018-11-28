#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int findMinInvitees(const vector<int> &sCount) {
  int invitees = 0;
  int clappers = 0;
  for (int i = 0; i < sCount.size(); ++i) {
    if (clappers < i) {
      invitees += i - clappers;
      clappers = i;
    }
    clappers += sCount[i];
  } 
  return invitees;
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;
  
  for (int i = 0; i < T; ++i) {
    int Smax = 0;
    cin >> Smax;
    char c;
    cin.get(c);
    vector<int> sCount;
    for (int j = 0; j <= Smax; ++j) {
      cin.get(c);
      sCount.push_back(atoi(&c));
    }
    cout << "Case #" << i+1 << ": " << findMinInvitees(sCount) << endl;
  }

  return 0;
}




