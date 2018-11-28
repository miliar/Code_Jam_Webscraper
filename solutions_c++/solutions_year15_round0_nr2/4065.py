#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <assert.h>
#include <queue>
#include <sstream>
#include <iomanip>

using namespace std;

bool officialprint=true;

int D=-1;

std::vector<int> pancakes;

class State {
private:
  std::vector<int> pancakes_;
  int time_;
  
  int totalPancakes_;

  void computeTotalPancakes_();

public:
  State(const std::vector<int>& pancakes, int t=0): pancakes_(pancakes), time_(t) { computeTotalPancakes_(); }

  int time() const { return time_; }

  bool allDone() const { return totalPancakes_ == 0; }

  bool pushNeighbors(queue<State>& q) const;

  void eat();
};


void State::computeTotalPancakes_()
{
  totalPancakes_ = 0;
  for (int i=0; i<pancakes_.size(); ++i) totalPancakes_ += pancakes_[i];
}

void State::eat()
{
  totalPancakes_ = 0;
  for (int i=0; i<pancakes_.size(); ++i) {
    if (pancakes_[i] > 0) {
      pancakes_[i]--;
      totalPancakes_ += pancakes_[i];
    }
  }
}

bool State::pushNeighbors(queue<State>& q) const
{
  assert(!allDone());
  
  //find the diner with most pancakes
  int d=-1;
  int nump=-1;
  for (int i=0; i<pancakes_.size(); ++i) {
    if (nump < pancakes_[i]) {
      d = i;
      nump = pancakes_[i];
    }
  }

  assert(d!=-1);
  assert(nump > 0);
  assert(nump == pancakes_[d]);

  //let the time pass
  State newState(pancakes_, time_+1);
  newState.eat();
  q.push(newState);

  if (newState.allDone()) return true;

  //split the stack anywhere from 1 to n/2 with a new client
  for (int i=1; i<=pancakes_[d]/2; ++i) {
    State newState2(pancakes_, time_+1);
    newState2.pancakes_[d] -= i;
    newState2.pancakes_.push_back(i);
    q.push(newState2);
  }

  return false;
}


int solve()
{
  int time=0;

  queue<State> q;

  q.push(State(pancakes));

  while (!q.empty()) {
    State b = q.front();
    q.pop();
    
    assert(time <= b.time());

    if (b.allDone()) {
      return b.time();
    }

    if (b.pushNeighbors(q))
      return b.time()+1;
  }

  assert(false);
  return 0;
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;
  
  //  if (!officialprint)  cout << "Number of cases: " << numCases << endl;

  for (int c=0; c<numCases; ++c) {
    i >> D;

    pancakes.resize(D, 0);
    
    for (int r=0; r<D; ++r) {
      i >> pancakes[r];
    }

    int answer = solve();
    cout << "Case #" << c+1 << ": " << answer << endl;
  }

  return true;
}


int main(int argv, char* argc[])
{
  if (argv < 2) {
    cout << "Usage " << argc[0] << " <inputFile>" << endl;
    exit(1);
  }

  ifstream filei(argc[1]);

  if (!readFile(filei)) {
    cout << "Couldn't parse file " << argc[1] << endl;
    exit(1);
  }

  //    for (long int d=0; d<100; ++d) {
  //      for (long int b=0; b<100; ++b) {
  //        cout << "d: " << d << " b: " << b << endl;
  //
  //        long int ff = f(d,b);
  //        long int hh = h(d,b);
  //        
  //        cout << "f: " << ff << " h: " << hh << endl;
  //
  //        assert(ff == hh);
  //
  //
  //        cout << setw(4) << h(d,b) << " ";
  //      }
  //      cout << endl;
  //    }

  //  cout << "********************" << endl;
  //
  //  cout << "h(5,2) = " << h(5,2) << endl;
  //
  //  cout << "********************" << endl;
  //
  //  cout << "h(5,3) = " << h(5,3) << endl;

  return 0;
}
