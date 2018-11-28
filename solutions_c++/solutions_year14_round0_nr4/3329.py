
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int playFair(vector<double> &blocksNaomi, vector<double> &blocksKen)
{
  int kenWins = 0;
  int blockCount = blocksNaomi.size() - 1;

  int i=0, j=0;
  // each time this loop run, Ken wins
  while(i<=blockCount && j<=blockCount) {
    while(blocksNaomi[i] > blocksKen[j] && j<=blockCount)
      j++;
    if(j>blockCount)
      break;
    i++;
    j++;
    kenWins++;
  }
  
  return blocksNaomi.size() - kenWins;
}


int playDeceitful(vector<double> &blocksNaomi, vector<double> &blocksKen)
{
  int naomiWins = 0;
  int blockCount = blocksNaomi.size() - 1;

  int i=0, j=0;
  // each time this loop runs, Naomi wins
  while(j<=blockCount && i<=blockCount) {
    while(blocksNaomi[i] < blocksKen[j] && i<=blockCount)
      i++;
    if(i>blockCount)
      break;
    i++;
    j++;
    naomiWins++;
  }
  
  return naomiWins;
}


int main(int argc, char **)
{
  int testCount = 0;
  cin >> testCount;

  int blockCount;
  
  for(int testCounter=0; testCounter<testCount; testCounter++) {
  
    cin >> blockCount;
    vector<double> blocksNaomi(blockCount),
      blocksKen(blockCount);

    // read naomis's blocks
    for(int i=0; i<blockCount; i++)
      cin >> blocksNaomi[i];
    // read ken's blocks
    for(int i=0; i<blockCount; i++)
      cin >> blocksKen[i];

    sort(blocksNaomi.begin(), blocksNaomi.end());
    sort(blocksKen.begin(), blocksKen.end());

    cout << "Case #" << (testCounter+1) << ":"
	 << " " << playDeceitful(blocksNaomi, blocksKen)
	 << " " << playFair(blocksNaomi, blocksKen)
	 << endl;
  }
  return 0;
}

