#include <iostream>
#include <string>

using namespace std;

void solutionOut(int caseNo, int res) {
  cout << "Case #" << caseNo << ": " << res << endl;
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  cin >> T;

  int incCaseNo = 0;
  while (T--) {
    incCaseNo++;

    int sMax;
    string audience;

    cin >> sMax >> audience;
    int sumAudi = 0;
    int needNFriends = 0;
    for (int i = 0; i < audience.length(); ++i) {
      if (sumAudi < i) {
        int thisRoundNeedNFriends = i - sumAudi;
        needNFriends += thisRoundNeedNFriends;
        sumAudi += thisRoundNeedNFriends;
      }
      sumAudi += audience[i] - '0';
    }

    solutionOut(incCaseNo, needNFriends);
  }

  return 0;
}