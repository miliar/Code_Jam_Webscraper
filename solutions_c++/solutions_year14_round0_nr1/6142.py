#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
  int totalTc; cin >> totalTc;
  for (int tc = 1; tc <= totalTc; ++tc) {

    map<int,int> chosen;

    for (int i=0; i<2; i++) {
      int rowNum; cin >> rowNum;

      for (int j=0; j<4; j++) {
	for (int k=0; k<4; k++) {
	  int tmpCard; cin >> tmpCard;

	  if (j + 1 != rowNum) continue;
	  if (chosen.find(tmpCard) != chosen.end()) chosen[tmpCard]++;
	  else chosen[tmpCard] = 1;
	}
      }
    }

    int ans = 0;
    for(map<int,int>::iterator it = chosen.begin();
	it != chosen.end(); it++) {
      if (it->second != 2) continue;
      if (ans != 0) ans = -1;
      else ans = it->first;
    }
	
    cout << "Case #" << tc << ": ";
    if ( ans == 0 ) cout << "Volunteer cheated!" << endl;
    else if ( ans == -1 ) cout << "Bad magician!" << endl;
    else cout << ans << endl;
  }
  return 0;
}
