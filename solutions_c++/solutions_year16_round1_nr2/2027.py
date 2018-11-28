#include <algorithm>
#include <climits>
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

vector<int> getMissingList(vector<vector<int>> &listsOfHeights) {
  int N = (listsOfHeights.size()+1)/2;
  vector<vector<int>> sortedListsOfHeights; sortedListsOfHeights.reserve(2*N);
  int missingIdx = -1;
  int lastDiagonal = 0;
  vector<bool> visited(listsOfHeights.size(), false);
  // sort by diagonals
  for (int i = 0; i < N; ++i) {
    int smallestDiagonal = INT_MAX;
    int idxA, idxB;
    bool twoFound = false;
    for (int j = 0; j < listsOfHeights.size(); ++j) {
      if (!visited[j]) {
        if (listsOfHeights[j][i] < smallestDiagonal) {
          smallestDiagonal = listsOfHeights[j][i];
          idxA = j;
          twoFound = false;
        } else if (listsOfHeights[j][i] == smallestDiagonal) {
          idxB = j;
          twoFound = true;
        }
      }
    }    
    sortedListsOfHeights.push_back(listsOfHeights[idxA]);
    visited[idxA] = true;
    if (twoFound) {
      sortedListsOfHeights.push_back(listsOfHeights[idxB]);
      visited[idxB] = true;
    } else {
      missingIdx = sortedListsOfHeights.size();
      sortedListsOfHeights.emplace_back();
      sortedListsOfHeights.back().reserve(N);
    }
  }
  // now pick height not in corresponding filled list
  int filledIdx = missingIdx - 1;
  int k = filledIdx/2;
  for (int i = 0; i < N; ++i) {
    if (i == k) {
      sortedListsOfHeights[missingIdx].push_back(sortedListsOfHeights[filledIdx][i]);
    } else {
      int a = sortedListsOfHeights[filledIdx][i];
      int b = sortedListsOfHeights[2*i][k] == a ? sortedListsOfHeights[2*i + 1][k] : sortedListsOfHeights[2*i][k];
      sortedListsOfHeights[missingIdx].push_back(b);
    } 
  }
  return sortedListsOfHeights[missingIdx];
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);  
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;
    vector<vector<int>> listsOfHeights;
    listsOfHeights.reserve(2*N - 1);
    for (int n = 0; n < 2*N - 1; ++n) {
      listsOfHeights.emplace_back();
      listsOfHeights.back().reserve(N);
      for (int m = 0; m < N; ++m) {
        int h; cin >> h;
        listsOfHeights.back().push_back(h);
      }
    }
    vector<int> missingList = getMissingList(listsOfHeights);
    cout << "Case #" << t << ": ";
    copy(missingList.begin(), missingList.end() - 1,
         ostream_iterator<int>(cout, " "));    
    cout << missingList.back() << '\n';
  }  
  cout << flush;
  return 0;
}
