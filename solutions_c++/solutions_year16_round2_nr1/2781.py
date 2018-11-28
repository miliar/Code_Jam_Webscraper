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

// void UpdateCharCount("TWO", count, &char_count) {
void UpdateCharCount(const string& digstr, int count, map<char, int>* char_count_ptr) {
  for (int i = 0; i < digstr.length(); i++) {
    (*char_count_ptr)[digstr[i]] = (*char_count_ptr)[digstr[i]] - count;
  }
}

string GetAns(string& str) {
  string tstr = "ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE";
  map<char, int> char_count;
  for (int i = 0; i < tstr.length(); i++) {
    // Initializing.
    char_count[tstr[i]] = 0;
  }

  for (int i = 0; i < str.length(); i++) {
    char_count[str[i]] = char_count[str[i]] + 1;
  }

  vector<int> digit_count(10,0);

  // Zeros.
  digit_count[0] = char_count['Z'];
  UpdateCharCount("ZERO", digit_count[0], &char_count);

  // Twos.
  digit_count[2] = char_count['W'];
  UpdateCharCount("TWO", digit_count[2], &char_count);

  // Fours.
  digit_count[4] = char_count['U'];
  UpdateCharCount("FOUR", digit_count[4], &char_count);

  // Sixs.
  digit_count[6] = char_count['X'];
  UpdateCharCount("SIX", digit_count[6], &char_count);

  // Eights.
  digit_count[8] = char_count['G'];
  UpdateCharCount("EIGHT", digit_count[8], &char_count);

  // Ones.
  digit_count[1] = char_count['O'];
  UpdateCharCount("ONE", digit_count[1], &char_count);  

  // Three.
  digit_count[3] = char_count['T'];
  UpdateCharCount("THREE", digit_count[3], &char_count);  

  // Five.
  digit_count[5] = char_count['F'];
  UpdateCharCount("FIVE", digit_count[5], &char_count);  
  
  // seven.
  digit_count[7] = char_count['V'];
  UpdateCharCount("SEVEN", digit_count[7], &char_count);  

  // nine.
  digit_count[9] = char_count['I'];
  UpdateCharCount("NINE", digit_count[9], &char_count);  

  map<int, string> strrep;
  strrep[0] = "0";
  strrep[1] = "1";
  strrep[2] = "2";
  strrep[3] = "3";
  strrep[4] = "4";
  strrep[5] = "5";
  strrep[6] = "6";
  strrep[7] = "7";
  strrep[8] = "8";
  strrep[9] = "9";
  
  // Computing final ans.
  string ans = "";
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < digit_count[i]; j++) {
      ans = ans + strrep[i];
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
    cin >> str;
    cout << "Case #" << tc << ": " << GetAns(str) << std::endl;
  }
}


