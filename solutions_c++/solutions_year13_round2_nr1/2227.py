#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

class State {
 public:
  int my_size_;
  multiset<int> motes_;

  void Reduce();
  void Dump() {
    for (multiset<int>::iterator it = motes_.begin(); it != motes_.end(); ++it)
      cerr << *it << " ";
    cerr << endl;
  }

  int GetOperationCount();
};

void State::Reduce() {
  multiset<int>::iterator it = motes_.begin();
  multiset<int>::iterator beginner = motes_.begin();
  
  while ((it != motes_.end()) && (*it < my_size_)) {
    my_size_ += *it;
    it++;
  }
  motes_.erase(beginner, it);
  //cerr << "After reduction "; Dump();
};

int State::GetOperationCount() {
  //Dump();
  Reduce();
  //cerr << motes_.size() << " is size " << endl;
  if (motes_.size() == 0)
    return 0;

  int branch1 = 100000000;
  if (my_size_ > 1) {
    //cerr << "Trying addition of " << my_size_ - 1 << " to "; Dump();
    multiset<int> backup_motes(motes_);
    int backup_my_size = my_size_;

    motes_.insert(my_size_ - 1);
    Reduce();
    branch1 = 1 + GetOperationCount();

    motes_ = backup_motes;
    my_size_ = backup_my_size;
  }
  //cerr << "Trying removal "; Dump();
  motes_.erase(motes_.begin());
  int branch2 = 1 + GetOperationCount();

  if (branch1 < branch2)
    return branch1;
  else
    return branch2;
}

int main() {

  int t;
  string line;
  getline(cin, line);
  istringstream iss1(line);
  iss1 >> t;

  //cerr << t << " cases to deal with \n" << endl;
  for (int i = 0; i < t; ++i) {
    getline(cin, line);
    istringstream iss2(line);
    int my_size;
    int nmotes;
    iss2 >> my_size >> nmotes;
    State state;
    state.my_size_ = my_size;
    //cerr << my_size << " " << nmotes << endl;

    getline(cin, line);
    istringstream iss3(line);
    for (int j = 0; j < nmotes; ++j) {
      int sz;
      iss3 >> sz;
      state.motes_.insert(sz);
      //cerr << sz << " ";
    }
    //cerr << endl;

    cout << "Case #" << i + 1 << ": " << state.GetOperationCount() << endl;
  }
  return 0;
}

