#include <iostream>
#include <cassert>
using namespace std;

// Quaternion functions

typedef int quaternion;

int productTable[5][5] = 
{
  { 0, 0, 0, 0, 0},
  { 0, 1, 2, 3, 4},
  { 0, 2,-1, 4,-3},
  { 0, 3,-4,-1, 2},
  { 0, 4, 3,-2,-1}
};

quaternion sign (quaternion x) {
  return x < 0 ? -1 : 1;
}

// Warning: not commutative
quaternion product (quaternion a, quaternion b) {
  quaternion signA = sign(a);
  quaternion signB = sign(b);
  return signA * signB * productTable[a/signA][b/signB];
}

quaternion fromChar (char x) {
  switch(x) {
    case 'i': return 2;
    case 'j': return 3;
    case 'k': return 4;
    default: assert(false);
  }
}

void quaternionTests () {
  assert(product(1, -1) == -1);
  assert(product(2, -3) == -4);
  assert(product(-2, -2) == -1);
  assert(product(-4, -1) == 4);
  assert(product(-4, 3) == 2);
}

// Main algorithm

#define MAXSIZE 1500000
quaternion array[MAXSIZE];
quaternion cumProds[MAXSIZE+1]; // cumProds[i] stores the cumulative product to the ith element (inclusive)

int reduce(long long x) {
  if (x < 12) return x;
  else return 12 + (x%4);
}

bool solvable (string s, long long reps) {
  int newReps = reduce(reps); // If reps is big, reduce reps to a suitable size
  // Generate the data array
  int dataSize = s.size() * newReps;
  for (int i = 0; i < dataSize; i++) {
    array[i] = fromChar(s[i % s.size()]);
  }
  // Compute cumProds
  cumProds[0] = array[0];
  for (int i = 1; i < dataSize; i++) {
    cumProds[i] = product(cumProds[i-1], array[i]);
    // cout << cumProds[i] << endl;
  }
  // Check that the total product is -1, else false
  if (cumProds[dataSize-1] != -1) return false;
  // Find the first i (if none, return false)
  int firsti = -1;
  for (int i = 0; i < dataSize; i++) {
    if (cumProds[i] == 2) {
      firsti = i;
      break;
    }
  }
  if (firsti == -1) return false;
  // Find the last k (if none, return false)
  int lastk = -1;
  for (int i = 0; i < dataSize; i++) {
    if (cumProds[i] == 4) {
      lastk = i;
    }
  }
  if (lastk == -1) return false;
  // If first i before last k, return true, else false
  if (firsti < lastk) return true;
  return false;
}

int main () {
  int T;
  cin >> T;
  //For test case
  for (int tc = 1; tc <= T; tc++) {
    long long L, X;
    string s;
    cin >> L;
    cin >> X;
    cin >> s;
    if (solvable(s, X)) {
      cout << "Case #" << tc << ": YES" << endl;
    } else {
      cout << "Case #" << tc << ": NO" << endl;
    }
  }
  return 0;
}