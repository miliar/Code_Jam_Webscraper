#include <iostream>
#include <set>
#include <queue>

using namespace std;

class Party {
  public:
    int P;
    char l;

    bool operator<(const Party&) const;
};

bool Party::operator<(const Party& right) const {
    return P < right.P;
}

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for(int ca=0; ca<T; ++ca) {
    long N;
    cin >> N;

    int total = 0;
    std::priority_queue<Party> P;
    char c = 'A';
    for(int i=0; i<N; i++, c++) {
      Party party;
      cin >> party.P;
      party.l = c;
      total += party.P;
      P.push(party);
    }

    vector<string> res;
    // Take party with most members. Take second most if condition not violated.
    while(P.size()) {
      Party most = P.top();
      P.pop();
      total--;
      most.P--;
      if(most.P > 0) {
        P.push(most);
      }

      string r = "";
      r+= most.l;

      Party second = P.top();
      P.pop();
      second.P--;
      total--;
      if(second.P > 0) {
        P.push(second);
      }

      // don't take second if it would cause the next party to have more than half of the total.
      if(P.size() && P.top().P > total/2) {
        P.push(second);
        total ++;
      } else {
        r += second.l;
      }

      res.push_back(r);
    }

    cout << "Case #" << (ca+1) << ":";
    for(auto it=res.begin(); it != res.end(); ++it) {
      cout << " " << *it;
    }
    cout << "\n";
  }

  return 0;
}
