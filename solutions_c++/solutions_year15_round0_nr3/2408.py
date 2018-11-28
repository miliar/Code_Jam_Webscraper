#include <iostream>
#include <string>
#include <vector>

using namespace std;


const int p1 = 1;
const int pI = 2;
const int pJ = 3;
const int pK = 4;
const int n1 = -1;
const int nI = -2;
const int nJ = -3;
const int nK = -4;

int multiply(int a, int b) {
  if (a == p1) { return b; }
  if (b == p1) { return a; }
  if (a == n1) { return -b; }
  if (b == n1) { return -a; }
  int sign = 1;
  if ((a < 0 && b > 0) || (a > 0 && b < 0)) {
    sign = -1;
  }  
  a = abs(a); b = abs(b);
  if (a == b) { return sign*n1; }
  if (a == pI && b == pJ) { return sign*pK; }
  if (a == pI && b == pK) { return sign*nJ; }
  if (a == pJ && b == pI) { return sign*nK; }
  if (a == pJ && b == pK) { return sign*pI; }
  if (a == pK && b == pI) { return sign*pJ; }
  if (a == pK && b == pJ) { return sign*nI; }
  return 100;
}

int invert(int a) {
  if (a == p1) { return p1; }
  if (a == n1) { return n1; }
  if (a == pI) { return nI; }
  if (a == pJ) { return nJ; }
  if (a == pK) { return nK; }
  if (a == pK) { return nK; }
  if (a == nI) { return pI; }
  if (a == nJ) { return pJ; }
  if (a == nK) { return pK; }
  return 100000;
}

int convertToQuarternion(char c) {
  if (c == 'i') { return pI; }
  if (c == 'j') { return pJ; }
  if (c == 'k') { return pK; }
  return 1000;
}

bool isPossible(string s) {
  int current = p1;
  bool iFound = false;
  bool jFound = false;
  for (int i = 0; i < s.length(); ++i) {    
    int q = convertToQuarternion(s[i]);
    if (!iFound) {
      current = multiply(current, q);
      if (current == pI) { iFound = true; current = p1; }      
    } else if (iFound && !jFound) { 
      current = multiply(current, q);
      if (current == pJ) { jFound = true; current = p1; }
    } else if (iFound && jFound) { 
      current = multiply(current, q); 
    }    
  } 
  cout << current << endl;
  return current == pK && iFound && jFound ? true : false;
}

bool isPossibleDp(string s, long long X) {
  long long LX = X*((long long) s.length());
  vector<int> A(s.length() + 1);
  A[0] = p1;
  for (int i = 1; i <= s.length(); ++i) {
    int q = convertToQuarternion(s[i-1]);
    A[i] = multiply(A[i-1], q);
  }
  // A[0] = p1, A[i] = multiplication by s[0]...s[i-1]
  // find multiplication by s[i],...,s[s.length()-1] by multiply(invert(A[i]), A[s.length()])
  // find multiplication by s[i],...,s[i+j] by multiply(invert(A[i]), A[i+j+1])
  vector<int> B; // B contains full length cycles
  B.push_back(p1); 
  for (int i = 0; i < 3; ++i) { B.push_back(multiply(B.back(), A.back())); }
  // find I
  long long minIIdx = LX;
  for (int i = 1; i < A.size(); ++i) {
    if (A[i] == pI) { 
      minIIdx = i;
      break;
    }
    // use cycles and continuation
    for (int c = 1; c < B.size(); ++c) {
      int current = multiply(B[c], A[i]);
      if (current == pI && (i-1) + c*s.length() < minIIdx) {
        minIIdx = (long long) (i + c*s.length());
      }
    }
  }
  // I was obtained by multiplication by s[0],...,s[minIIdx-1]
  if (minIIdx >= LX) { return false; }
  // now find J
  long long minJIdx = LX;  
  int jOffset = minIIdx % s.length();
  for (int i = jOffset + 1; i < A.size(); ++i)  {
    int current = multiply(invert(A[jOffset]), A[i]);
    if (current == pJ) {
      minJIdx = minIIdx + i - jOffset;
      break;
    }
    // now add cycles and loop arounds
    if (i == A.size() - 1) {
      for (int j = 0; j < A.size(); ++j) {
        for (int c = 0; c < B.size(); ++c) {
          int next = multiply(multiply(current, B[c]), A[j]);
          int nextIdx = minIIdx + i - jOffset + c*s.length() + j;
          if (next == pJ && nextIdx < minJIdx) {
            minJIdx = nextIdx;
          }
        }
      }
    }
  }
  // J was obtained by multiplication by s[minIIdx],...,s[minJIdx-1]
  if (minJIdx >= LX) { return false; }
  // multiply everything else out
  int kOffset = minJIdx % s.length();
  int k = multiply(invert(A[kOffset]), A.back());
  long long cyclesLeft = (LX-minJIdx-1)/s.length();
  k = multiply(k, B[(int) (cyclesLeft % 4)]);
  return k == pK ? true : false;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int L;
    long long X;
    cin >> L >> X;
    string s;
    cin >> s;
    // string ss(s);
    // for (int j = 1; j < X; ++j) {
    //   ss += s;
    // }
    // isPossible(ss);
    bool yes = isPossibleDp(s, X);
    cout << "Case #" << i+1 << ": " << (yes ? "YES" : "NO") << endl;
  }
  return 0;
}
