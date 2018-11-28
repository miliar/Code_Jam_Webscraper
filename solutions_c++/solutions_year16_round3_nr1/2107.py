#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Evacuator {
 public:
  Evacuator(int totalMembers, std::vector<int> members) : remainingMembers_(members), totalMembers_(totalMembers), addedInParties_(members.size(),0) {}

  void process() {
    remainingMembers_[0]--;
    remainingMembers_[1]--;
    addedInParties_[0]++;
    addedInParties_[1]++;
    solution.push_back("AB");
    totalAdded_ += 2;

    while(totalAdded_ < totalMembers_) {
      addMember();
    }
  }

  void printSolution(ostream& out) {
    for(int i = solution.size()-1; i > 0; --i) {
      out << solution[i] << " ";
    }
    out << solution[0];
  }

 private:
  void addMember() {
    bool found = false;
    int nParties = remainingMembers_.size();
    for (int i = 0; i < nParties; ++i) {
      if (remainingMembers_[i] > 0) {
        int newMajority = (totalAdded_+1) / 2 + 1;
        if (addedInParties_[i] + 1 < newMajority) {
          remainingMembers_[i]--;
          addedInParties_[i]++;
          char c = 'A' + i;
          string sol;
          sol.push_back(c);
          solution.push_back(sol);
          found = true;
          break;
        }
      }
    }
    if (!found) {
      int a, b;
      for (int i = 0; i < nParties; ++i) {
        if (remainingMembers_[i] > 0) {
          a = i;
          remainingMembers_[i]--;
          addedInParties_[i]++;
          break;
        }
      }
      for (int i = 0; i < nParties; ++i) {
        if (remainingMembers_[i] > 0 && i != a) {
          b = i;
          remainingMembers_[i]--;
          addedInParties_[i]++;
          break;
        }
      }
      char cA = 'A' + a;
      char cB = 'A' + b;
      string sol;
      sol.push_back(cA);
      sol.push_back(cB);
      solution.push_back(sol);
      totalAdded_++;
    }
    totalAdded_++;
  }

  vector<int> remainingMembers_;
  vector<int> addedInParties_;
  vector<string> solution;
  int totalMembers_;
  int totalAdded_ = 0;
};

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;

    std::vector<int> membersInParties(N);
    int totalMembers = 0;
    for(int i = 0; i < N; ++i) {
      cin >> membersInParties[i];
      totalMembers += membersInParties[i];
    }

    Evacuator ev(totalMembers, membersInParties);
    ev.process();

    cout << "Case #" << t << ": ";
    ev.printSolution(cout);
    cout << std::endl;
  }
}
