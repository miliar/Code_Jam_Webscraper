#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
typedef ulong ulong;

void movesTillBiggerThan(ulong mySize, ulong desiredSize, ulong &outSize, ulong& moves) {
  moves = 0;
  outSize = mySize;
  while(outSize<= desiredSize) {
    outSize += outSize - 1;
    moves += 1;
  }
  return;
}

ulong getMinMoves(ulong initMote, vector<ulong>& motes) {
  ulong moves = 0;
  ulong eaten = 0;
  ulong total = motes.size();
  ulong me = initMote;
  
  std::sort(motes.begin(), motes.end());
  
  for(auto currentMote : motes) {
    if(me <= currentMote) {
      if(me == 1) { //can't eat anything, delete everything
        return moves + total - eaten;
      }
      
      ulong movesToGrow;
      ulong sizeAfterGrowth;
      
      movesTillBiggerThan(me, currentMote, sizeAfterGrowth, movesToGrow);
      if(movesToGrow > total-eaten) {
        return moves + total-eaten; //delete total-eaten last moths
      } else {
        me = sizeAfterGrowth;
        moves += movesToGrow;
      }
    }
    
    me += currentMote;
    eaten++;
  }
  return moves;
}

void printVector(vector<ulong> v) {
  cout << "[";
  for(ulong a:v)
    cout << a << ", ";
  cout << "]";
}

int main() {
  uint testCases;
  cin >> testCases;
  
  for(uint i=0; i<testCases; i++) {
    ulong initialMote, noOfMotes;
    vector<ulong> motes;
    cin >> initialMote;
    cin >> noOfMotes;
    
    for(ulong mote = 0; mote < noOfMotes; mote++) {
      ulong newMote;
      cin >> newMote;
      motes.push_back(newMote);
    }
    
    /*
    cout << "getMinMoves(" << initialMote<< ", ";
    printVector(motes);
    cout << ");" << endl;
    */
    ulong moves = getMinMoves(initialMote, motes);
    std::cout << "Case #" << i+1 <<": "<< moves << endl;
  }
  

}