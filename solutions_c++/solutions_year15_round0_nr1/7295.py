#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  int T;
  cin >> T;
  string line;
  getline(cin, line);
  int pos;
  int Smax;
  vector<int> S;
  string digits;
  int allFriends;
  int friends;
  int stand;
  for (int i = 1; i <= T; i++)
  {
    getline(cin, line);
    pos = line.find(" ");
    Smax = atoi(line.substr(0, pos).c_str());
    digits = line.substr(pos + 1);
    S.clear();
    for (int j = 0; j <= Smax; j++)
      S.push_back(atoi(digits.substr(j, 1).c_str()));
    allFriends = 0;
    stand = 0;
    cout << "Case #" << i << ": ";
    for (int j = 0; j <= Smax; j++)
    {
      friends = 0;
      if ((S[j] > 0) && (stand < j))
      {
        friends = j - stand;
        allFriends += friends;
        stand += friends;
      }
      stand += S[j];
    }
    cout << allFriends << endl;
  }
}