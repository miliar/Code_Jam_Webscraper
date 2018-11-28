#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> vown, vken;
int n;

int stoi(const string & s) {
  int n = 0;
  for (int i = 0; i < int(s.size()); ++i) {
    n *= 10;
    n += s[i] - '0';
  }
  for (int i = s.size(); i < 5; ++i)
    n *= 10;
  return n;
}

const int maxn = 1e6;

int firstGame() {
  vector<bool> owndead(n, false), kendead(n, false);
  int score = 0;
  for (int i = 0; i < n; ++i) {
    int firstken = 0;
    while (kendead[firstken]) ++firstken;
    int lastken = n-1;
    while (kendead[lastken]) --lastken;
    
    int firstown = 0;
    while (owndead[firstown]) ++firstown;
    int lastown = firstown;
    while ((owndead[lastown] or vown[lastown] < vken[lastken]) and lastown < n) ++lastown;
    
    if (lastown < n) { // point
      ++score;
      kendead[firstken] = true;
      owndead[lastown] = true;
    }
    else {
      while (kendead[firstken] or  vken[firstken] < vown[firstown]) ++firstken;
      kendead[firstken] = true;
      owndead[firstown] = true;
    }
  }
  return score;
}

int secondGame() {
  vector<bool> owndead(n, false), kendead(n, false);
  
  vector<bool> used(maxn+1, false);
  vector<int> kenrev(maxn, -1);

  for (int i = 0; i < n; ++i) {
    used[vown[i]] = true;
  }
  for (int i = 0; i < n; ++i) {
    used[vken[i]] = true;
    kenrev[vken[i]] = i;
  }

  int score = 0;
  int first = 0, last = n-1;
  for (int i = 0; i < n; ++i) { //for each own piece
    int kenInd = n-1;
    while (kendead[kenInd]) --kenInd;
    
    int ownInd;
    if (vown[last] > vken[kenInd]) {
      ownInd = last;
      --last;
    }
    else {
      ownInd = first;
      ++first;
    }
    
    int lastFree = vken[kenInd]-1;
    while (used[lastFree] and lastFree > vown[ownInd]) {
      if (kenrev[lastFree] != -1 and !kendead[kenrev[lastFree]])
        kenInd = lastFree;
      --lastFree;
    }
    
    lastFree = max(lastFree, vown[ownInd]);
    if (lastFree != vown[ownInd]) {
      used[lastFree] = true;
    }
    
    if (lastFree > vken[kenInd]) ++score;
    owndead[ownInd] = true;
    kendead[kenInd] = true;
  }
  return score;
}

int main() {
  int T; cin >> T;
  int ncase = 0;
  while (T--) {
    cin >> n;
    
    vown.assign(n, 0);
    vken.assign(n, 0);
    for (int i = 0; i < n; ++i) {
      string s; cin >> s;
      vown[i] = stoi(s.substr(2));
    }
    for (int i = 0; i < n; ++i) {
      string s; cin >> s;
      vken[i] = stoi(s.substr(2));
    }
    sort(vown.begin(), vown.end());
    sort(vken.begin(), vken.end());
/*    
    for (int i = 0; i < n; ++i)
      cout << vown[i] << ' ';
    cout << endl;
    for (int i = 0; i < n; ++i)
      cout << vken[i] << ' ';
    cout << endl;*/
    
    cout << "Case #" << ++ncase << ": " << secondGame() << " " << firstGame() << endl;
  }
}