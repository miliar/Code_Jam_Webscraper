#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cfloat>
#include <climits>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <utility>
#include <sys/time.h>

#define INF 1000000007
#define EPS (1e-8)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define mp make_pair
#define FOR(i,k) for(i=0;i<k;i++)
#define RFOR(i,k) for(i=k-1;i>=0;i--)
const long double PI = 3.1415926535897932384626433832795;
typedef long long LL;

using namespace std;

// Expects a string of the form '+-+-..'
// or '-+-+..'. '++--..' is not allowed.
int GetAns(const string& str) {
  if (str.length() == 0)
    return 0;

  vector<int> ansplus(str.length(), 0);
  vector<int> ansminus(str.length(), 0);

  // Setting the answers for 0th position.
  if (str[0] == '+') {
    ansplus[0] = 0;
    ansminus[0] = 1;
  }
  else if (str[0] == '-') {
    ansplus[0] = 1;
    ansminus[0] = 0;
  }

  for (int i = 1 ;i < str.length(); i++) {
    // A plus always combines with plus and 
    // viceversa.
    if (str[i] == '+') {
      ansplus[i] = ansplus[i-1];
      ansminus[i] = ansplus[i-1] + 1;
    }
    else if (str[i] == '-') {
      ansplus[i] = ansminus[i-1] + 1;
      ansminus[i] = ansminus[i-1];
    }
  }

  return ansplus[str.length() - 1];
}

// if input is '++--+-' output is '+-+-'
string GetDedupedString(const string& str) {
  string outstr = "";

  if (str.length() == 0)
    return outstr;

  // Setting the 0th pos.
  outstr.push_back(str[0]);

  for (int i = 1 ;i < str.length(); i++) {
    if (str[i] != outstr[outstr.length() - 1]) {
      outstr.push_back(str[i]);
    }
  }

  return outstr;
}

main()
{
  int testcases;
  std::cin >> testcases;

  for (int tc = 1; tc <= testcases; tc++) {
    string inputstr;
    std::cin >> inputstr;
    string deduped = GetDedupedString(inputstr);
    std::cout << "Case #" << tc << ": " << GetAns(deduped) << std::endl;
  }
}


