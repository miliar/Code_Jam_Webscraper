#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <climits>
#include <algorithm>
using namespace std;

int lengthRepetition(int n, const string& str) {
  int retVal = 1;
  char first = str[n];
  while (str[++n] == first) ++retVal;
  return retVal;
}

string extractCharacters(const string& str) {
  string retVal = "";
  int i1 = 0;
  while (i1 < str.length()) {
    retVal += str[i1];
    i1 += lengthRepetition(i1,str);
  }
  return retVal;
}

int dist(const string& str1, const string& str2) {
  int distance = 0;
  int i1 = 0;
  int i2 = 0;
  while (i1 < str1.length() and i2 < str2.length() and str1[i1] == str2[i2]) {
    int inc1 = lengthRepetition(i1,str1);
    int inc2 = lengthRepetition(i2,str2);
    i1 += inc1;
    i2 += inc2;
    distance += abs(inc1-inc2);
  }
  if (i1 != str1.length() or i2 != str2.length()) distance = INT_MAX;
  return distance;
}

int distanceSum(const vector<string>& vstr, const string& str) {
  int retVal = 0;
  for (int i = 0; i < vstr.size(); ++i) {
    int inc = dist(vstr[i],str);
    if (inc == INT_MAX) return INT_MAX;
    else retVal += inc;
  }
  return retVal;
}

int minDistance(const vector<string>& vstr) {
  int m = INT_MAX;
  for (int i = 0; i < vstr.size(); ++i) {
    int distsum = distanceSum(vstr,vstr[i]);
    m = distsum < m? distsum : m;
  }
  return m;
}

vector<string> successors(const string& str) {
  vector<string> retVal;
  int i = 0;
  while (i < str.length()) {
    string stri = str;
    stri.insert(i,1,str[i]);
    retVal.push_back(stri);
    i += lengthRepetition(i,str);
  }
  return retVal;
}

int minDistance2(const vector<string>& vstr) {
  string str = extractCharacters(vstr[0]);
  int d = distanceSum(vstr,str);
  string strnext;
  int dnext = INT_MAX;
  vector<string> suc = successors(str);
  for (int i = 0; i < suc.size(); ++i) {
    int dtmp = distanceSum(vstr,suc[i]);
    if (dtmp < dnext) {
      strnext = suc[i];
      dnext = dtmp;
    }
  }
  while (dnext < d) {
    d = dnext;
    str = strnext;
    
    dnext = INT_MAX;
    suc = successors(str);
    for (int i = 0; i < suc.size(); ++i) {
      int dtmp = distanceSum(vstr,suc[i]);
      if (dtmp < dnext) {
        str = suc[i];
        dnext = dtmp;
      }
    }
  }
  //cout << str << endl;
  return d;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;
    vector<string> vstr(N);
    for (int n = 0; n < N; ++n) cin >> vstr[n];
    cout << "Case #" << t << ": ";
    int mindist = minDistance(vstr);
    if (mindist == INT_MAX) cout << "Fegla Won" << endl;
    else cout << mindist << endl;
  }
  
  //vector<string> v = successors("maw");
  //for (int i = 0; i < v.size(); ++i) {
  //  cout << v[i] << endl;
  //}
  
  //cout << extractCharacters("mmaaaaw") << endl; 
}
