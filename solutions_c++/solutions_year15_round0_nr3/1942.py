#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <iomanip>
#include <set>

#define INF 2000000000
#define MOD 1000000007

using namespace std;

int mult[4][4] = {{1, 2, 3, 4}, 
		  {2, -1, 4, -3},
                  {3, -4, -1, 2},
		  {4, 3, -2, -1}};

int toInt(char c) {
  return (c - 'i' + 2);
}

int multiply(int a, int b) {
  return a / abs(a) * b / abs (b) * mult[abs(a) - 1][abs(b) - 1];
}

int main() {
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int testCount;
  cin >> testCount;
  for (int testNum = 1; testNum <= testCount; testNum++) {\
    cout << "Case #" << testNum << ": ";
    set<int> used;
    int l, x;
    cin >> l >> x;
    string s;
    cin >> s;
    int cur = 1;
    int index = 0;
    bool found = false;
    for (; index < l * x; index++) {
      cur = multiply(cur, toInt(s[index % l]));
      if (cur == 2) {
	found = true;
	break;
      }
    }
    if (!found) {
      cout << "NO" << endl;
      continue;
    }
    found = false;
    index++;
    cur = 1;
    for (; index < l * x; index++) {
      cur = multiply(cur, toInt(s[index % l]));
      if (cur == 3) {
	found = true;
	break;
      }
    }
    if (!found) {
      cout << "NO" << endl;
      continue;
    }
    index++;
    cur = 1;
    for (; index < l * x; index++) {
      cur = multiply(cur, toInt(s[index % l]));
    }
    if (cur == 4)
      cout << "YES";
    else
      cout << "NO";
    cout << endl;
    /*    int leftIndex, rightIndex;
    int cur = 1;
    bool isGood  = true;
    for (leftIndex = 0; true; leftIndex++) {
      if (leftIndex % l == 0) {
	if (used.find(cur) != used.end()) {
	  cout << "NO" << endl;
	  isGood = false;
	  break;
	}
	else
	  used.insert(cur);
      }
      cur = multiply(cur, toInt(s[leftIndex % l]));
      if (cur == 2)
	break;
    }
    used.clear();
    cur = 1;
    for (rightIndex = 0; true; rightIndex++) {
      if (rightIndex % l == 0) {
	if (used.find(cur) != used.end()) {
	  cout << "NO" << endl;
	  isGood = false;
	  break;
	}
	else
	  used.insert(cur);
      }
      cur = multiply(cur, toInt(s[l - 1 - (rightIndex % l)]));
      if (cur == 4)
	break;
    }
    int whole = 1;
    for (int i = 0; i < s.length(); i++)
      whole = multiply(whole, toInt(s[i]));
    if (!isGood)
      continue;
    x -= leftIndex / l + rightIndex / l;
    if (leftIndex % l + 1 + rightIndex % l + 1 >= x)
      x--;
    x -= 2;
    if (x < 0) {
      cout << "NO" << endl;
      continue;
    }
    cur = 1;
    leftIndex++;
    rightIndex++;
    while (leftIndex % l != 0) {
      cur = multiply(cur, toInt(s[leftIndex % l]));
      leftIndex++;
    }
    while (rightIndex % l != l - 1) {
      cur = multiply(cur, toInt(s[l - 1 - (rightIndex % l)]));
      rightIndex++;
    }
    */
  }
  return 0;
}
