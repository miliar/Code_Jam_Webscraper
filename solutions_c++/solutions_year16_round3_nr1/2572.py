#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int t;
  cin>>t;

  for (int i = 0; i < t; i++) {
    int n;
    cin >> n;

    vector<int> parties;

    int people = 0;

    for (int j = 0; j < n; j++) {
      int p;
      cin >> p;
      parties.push_back(p);
      people += p;
    }

    string outputs = "";

    while (people > 0) {

      // Find party to evacuate
      int partyPos1 = -1;
      float partyMajority1 = 0.0;
      for (int j = 0; j < n; j++) {
        int currParty = parties[j];
        float currMajority = currParty / (float) people;
        if (currMajority > partyMajority1) {
          partyPos1 = j;
          partyMajority1 = currMajority;
        }
      }

      // Find party to evacuate
      int partyPos2 = -1;
      float partyMajority2 = 0.0;
      for (int j = 0; j < n; j++) {
        int currParty = parties[j];
        if (j == partyPos1) currParty--;
        float currMajority = currParty / (float) (people - 1);
        if (currMajority > partyMajority2) {
          partyPos2 = j;
          partyMajority2 = currMajority;
        }
      }

      char party1 = (char) 65 + partyPos1;
      char party2 = (char) 65 + partyPos2;

      outputs += party1;
      if (partyPos2 != -1 && people != 3) outputs += party2;
      outputs += " ";

      parties[partyPos1]--;
      if (partyPos2 != -1 && people != 3) parties[partyPos2]--;

      people -= 2;
    }
    outputs = outputs.substr(0, outputs.size()-1);
    cout<<"Case #"<<(i+1)<<": "<<outputs<<endl;
  }
  return 0;
}
