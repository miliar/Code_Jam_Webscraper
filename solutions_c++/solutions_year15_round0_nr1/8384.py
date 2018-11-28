#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int minimumFriendsNumber(vector<int> audience, int maxShyness){
    int standing = 0; // how many audience have stood up
    int friends = 0; // how many friends to invite
    for (int i = 0; i <= maxShyness; ++i) {
      if (i > standing && audience.at(i) != 0) {
        friends += i - standing;
        standing += i - standing;
      }  
      standing += audience.at(i);
    }
    return friends;
  }
};

int main() {
  Solution s;
  int tc_nums = 0; // test case number
  int Smax = 0;
  std::string audienceStr;
  vector<int> result, audience;
  cin >> tc_nums;
  for (int i = 0; i < tc_nums; ++i) {
    cin >> Smax;
    cin >> audienceStr;
    for (int j = 0; j < audienceStr.length(); ++j) {
      audience.push_back(int(audienceStr.at(j) - '0'));
    }
    result.push_back(s.minimumFriendsNumber(audience, Smax));
    audience.clear();
  }
  for (vector<int>::iterator itr = result.begin(); itr != result.end(); ++itr) {
    cout << "Case #" << itr - result.begin() + 1 << ": "<< *itr << endl;
  }
}
