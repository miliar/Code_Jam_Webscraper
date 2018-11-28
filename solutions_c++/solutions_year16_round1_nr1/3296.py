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

string GetAns(string& input) {
  string ans = "";
  ans.push_back(input[0]);

  for (int i = 1; i < input.length(); i++) {
    // char is greater, push it in front.
    if (input[i] >= ans[0]) {
      string tmp = "";
      tmp.push_back(input[i]);
      ans = tmp + ans;
    }
    else {
      ans.push_back(input[i]);
    }
  }

  return ans;
}

main()
{
  int tests;
  scanf("%d", &tests);

  for (int tc = 1; tc <= tests; tc++) {
    string str;
    std::cin >> str;
    string ans = GetAns(str);
    std::cout << "Case #" << tc << ": " << ans << std::endl;
  }
}


