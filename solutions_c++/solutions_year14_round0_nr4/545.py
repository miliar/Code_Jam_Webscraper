#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;


int playWar(vector<double> alice, vector<double> bob) {
  int result = 0;


  for(int i = 0; i < alice.size(); i++) {

    bool canWin = false;
    int minIndex = -1;
    double minWeight = 0;
    int smallest = 0;
    for(int j = 0; j < (int)bob.size(); j++) {
      if(bob[j] > alice[i]) {
	canWin = true;
	if(minIndex == -1 || bob[minIndex] > bob[j]) {
	  minIndex = j;
	}
      }
      if(bob[smallest] > bob[j]) {
	smallest = j;
      }
    }
    if(!canWin) {
      bob.erase(bob.begin()+smallest);
      result++;
    } else {
      bob.erase(bob.begin() + minIndex);
    }
  }

  return result;
}

/*
int playDeceiptfulWar(vector<double> alice, vector<double> bobin) {
  int globalResult = 0;
  sort(alice.begin(), alice.end());
  vector<int> ind;
  for(int i = 0; i < alice.size(); i++) ind.push_back(i);
  do {
    int result = 0;
    vector<double> bob = bobin;
  for(int z = 0; z < alice.size(); z++) {
    int i = ind[z];
    bool canWin = false;
    int maxIndex = -1;
    double maxWeight = 0;
    int smallest = 0;
    for(int j = 0; j < (int)bob.size(); j++) {
      if(bob[j] > alice[i]) {
	canWin = true;
	if(maxIndex == -1 || bob[maxIndex] < bob[j]) {
	  maxIndex = j;
	}
      }
      if(bob[smallest] > bob[j]) {
	smallest = j;
      }
    }
    if(!canWin) {
      bob.erase(bob.begin()+smallest);
      result++;
    } else {
      bob.erase(bob.begin() + maxIndex);
    }
  }
  globalResult = max(result, globalResult);
}
  while(next_permutation(ind.begin(), ind.end()));
  return globalResult;
  }*/

int main() {
  int t;
  cin >> t;
  
  for(int zz = 1; zz <= t; zz++ ){
    int n;
    cin >> n;
    vector<double> alice, bob;

    for(int i = 0; i < n; i++) {
      double cur;
      cin >> cur;
      alice.push_back(cur);
    }

    for(int i = 0; i < n; i++) {
      double cur;
      cin >> cur;
      bob.push_back(cur);
    }

    int resultWar = playWar(alice, bob);
    int resultDeceiptfulWar = n-playWar(bob, alice);

    printf("Case #%d: %d %d\n", zz, resultDeceiptfulWar, resultWar);
  }

  return 0;
}
