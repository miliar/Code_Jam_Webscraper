/*
ID: Plagapong
LANG: C++
TASK: B
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#define INF 999999999
#define SWAP(u,v,w) {temp=u[v];u[v]=u[w];u[w]=temp;}

using namespace std;
int n, a[2000], b[2000];
int maxI = 0, maxA = 0, temp;

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  for (int i = 0; i < n; i++) a[i] = 0;
  maxI = maxA = 0;
}

void process() {
  // Code here!
  cin >> n;
  for (int i = 0; i < n; i++) cin >> a[i];
  int m = n, answer = 0;
  for (int i = 0; i < n; i++) {
    // Find min
    int minI = 0, minA = INF;
    for (int j = 0; j < m; j++) {
      if (a[j] < minA) {
        minA = a[j];
        minI = j;
      }
    }
    // Swap to front or back
    int frontCost = minI;
    int backCost = m - 1 - minI;
    answer += min(frontCost, backCost);
    // For efficiency, swap to back anyway
    for (int j = minI; j < m - 1; j++) {
      SWAP(a, j, j+1);
    }
    m--;
  }
  cout << answer;
}

int main() {
  preprocess();
  int times;
  cin >> times;
  for (int i = 1; i <= times; i++) {
	cout << "Case #" << i << ": ";
	clearVars();
	process();
	cout << endl;
  }
  return 0;
}
