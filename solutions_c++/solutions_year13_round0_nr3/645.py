#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <bitset>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <functional>
#include <hash_map>
#include <iostream>
#include <iomanip>
#include <list>
#include <deque>
#include <queue>
#include <math.h>
#include <map>
#include <numeric>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;
#define debug(x) cerr<<#x<<" = "<<(x)<<endl;
bool test = true;
const double pi=acos(-1.0);
const double eps=1e-11;
int breakpoint = 0;

const char rootdir[] = "C:\\CodeJam\\FairAndSquare";
void reopen(char* a) {
	char input[256], output[256];
	sprintf(input, "%s\\%s", rootdir, a);
	sprintf(output, "%s\\%s", rootdir, a);
	char *p = strstr(output, ".in");
	if (p) sprintf(p, ".out"); 
	else sprintf(&p[strlen(output)], ".out");
	debug(input);
	debug(output);
	freopen(input,"r",stdin);
	if (!test) freopen(output,"w",stdout);
}

int T = 0;
__int64 A = 0;
__int64 B = 0;

char SA[200];
char SB[200];

int numDigits(__int64 m) {
  if (m == 0) return 1;
  int v = 0;
  while (m > 0) {
    m = m / 10;
    v++;
  }
  return v;
}

__int64 mirror(__int64 m, int d) {
  int v = 0;
  for (int i = 0; i < d; i++) {
    v = 10 * v + (m % 10);
    m = m / 10;
  }
  return v;
}

// tell whether uppereppu^2 is palindrome
bool isFair(__int64 upper, int d) {
  if (d % 2 == 0) {
    // for example upper = 14, d=4 => p = 1441
    int sum = 0;
    for (int i = 0; i < (d>>1); i++) {
      int v = upper % 10;
      sum += v * v;
      if (sum >= 5) return false;
      upper /= 10;
    }
  } else {
    // for example, upper = 14, d=3 => p = 141
    int v = upper % 10;
    int sum = v * v;
    if (sum >= 10) return false;
    upper = upper / 10;
    d -= 1;
    for (int i = 0; i < (d>>1); i++) {
      int v = upper % 10;
      sum += 2 * v * v;
      if (sum >= 10) return false;
      upper /= 10;
    }
  }
}

int debug = 0;
bool isPalindrome(__int64 q) {
  char a[64];
  int d = 0;
  while (q != 0) {
    a[d] = q % 10 + '0';
    q /= 10;
    d++;
  }
  a[d] = 0;
  for (int i = 0; i < (d>>1); i++) {
    if (a[i] != a[d-1-i]) return false;
  }
  return true;
}

void solveOld(int cn) {
  int total = 0;
  
  __int64 M = (__int64)(sqrt(A * 1.0) + eps);
  __int64 N = (__int64)(sqrt(B * 1.0) + eps);
  // look for palindromes between [M, N]
  // 147 -> 151 161 171 181 191 202 ... 999 (1001)
  // 1447 -> 1551 1661 1771 1881 1991 2002 ... 9999 (10001)
  int d = numDigits(M);
  __int64 upper = M / 10^((d+1)/2) - 1;
  while (true) {
    __int64 p = 0;
    if (d % 2 == 0) {
      p = upper;
      for (int i = 0; i < (d>>1); i++) p *= 10;
      p += mirror(upper, d/2);
    } else {
      p = upper;
      for (int i = 0; i < ((d-1)>>1); i++) p *= 10;
      p += mirror(upper/10, (d-1)/2);
    }
    __int64 q = p * p;
    bool ok = isPalindrome(q);
    if (q > B) break;
    if (ok && test && q >= A)
      printf("%7lld %14lld %s\n", p, q, ok? "true":"");
    int od = numDigits(upper);
    upper++;
    int nd = numDigits(upper);
    if (nd > od) {
      d++;
      // upper:99 p:999  d:3 => upper:10  p:1001  d:4
      // upper:99 p:9999 d:4 => upper:100 p:10001 d:5
      if (d % 2 == 0) upper /= 10;
    }
    if (ok && q >= A) total++;
  }
  printf("Case #%d: %d\n", cn, total);
}

int highestDigit(__int64 p) {
  while (p > 10) p /= 10;
  return p;
}

bool anyDigit3Plus(__int64 p) {
  int v = 0;
  while (p > 0) {
    if (p % 10 >= 3) return true;
    p /= 10;
  }
}

void runTest() {
  A = 1L;
  B = 10000000000000000L;
  int total = 0;
  for (__int64 p = 1; p < 10000000000; p++) {
    if (!isPalindrome(p)) continue;
    if (p > 1000 && highestDigit(p) == 3) {
      int d = numDigits(p);
      p = 1;
      for (int i = 0; i < d; i++) p *= 10;
    }
    if (anyDigit3Plus(p)) continue;
    __int64 q = p * p;
    if (!isPalindrome(q)) continue;
    printf("%2d %10lld %20lld\n", ++total, p, q);
  }
}

const int MN = 100000;
const int D = 50;
char* buf = NULL;
char** nums = NULL;
int total = 0;
char* buf2 = NULL;
char** sqs = NULL;

char* nextNum(int d, char leading) {
  char * num = nums[total++];
  num[0] = leading;
  num[d-1] = leading;
  // initialize all other digit as '0'
  for (int l = 1; l < d-1; l++) {
    num[l] = '0';
  }
  return num;
}

int compareNum(const void* a, const void* b) {
  char * num1 = (char *)a;
  char * num2 = (char *)b;
  int len1 = strlen(num1);
  int len2 = strlen(num2);
  if (len1 < len2) return -1;
  else if (len1 > len2) return 1;
  else return strcmp(num1, num2);
}

void computeSquare(int index) {
  char * num = nums[index];
  char * s = sqs[index];
  int d = strlen(num);
  // sum should be 2 * d -1 digit
  for (int i = 0; i < 2*d - 1; i++) s[i] = '0';
  for (int i = 0; i < d; i++) {
    int k = num[i] - '0';
    if (k == 0) continue;
    for (int j = 0; j < d; j++) {
      int l = num[j] - '0';
      if (l == 0) continue;
      s[i+j] += k * l;
    }
  }
  // assert it is parlindrome
  for (int i = 0; i < d; i++) assert(s[i] = s[2*d-2-i]);
}

void buildParlindromeTable() {
  buf = (char *)malloc(MN * (D+1));
  memset(buf, 0, MN * (D+1));
  nums = (char **)malloc(MN * sizeof(char *));
  char *p = buf;
  for (int i = 0; i < MN; i++) {
    nums[i] = p;
    p += D+1;
  }

  buf2 = (char *)malloc(MN * (2*D+1));
  memset(buf2, 0, MN * (2*D+1));
  sqs = (char **)malloc(MN * sizeof(char *));
  char *q = buf2;
  for (int i = 0; i < MN; i++) {
    sqs[i] = q;
    q += 2*D+1;
  }

  // Add special 3 which is the only with with digit 3
  nextNum(1, '3');
  
  // No digit 2
  for (int d = 1; d <= D; d++) {
    int m = (d-1) >> 1; // index of the middle digit
    // The leading/tailing digit is always 1. Other than that,
    // we can afford 0, 1, 2, or 3 1's in either upper or lower half.
    {
      char * num = nextNum(d, '1');
      // printf("  %s\n", num);
    }

    for (int i = 1; i <= m; i++) {
      char * num = nextNum(d, '1');
      num[i] = '1';
      num[d-1-i] = num[i];
      // printf("  %s\n", num);
    }

    for (int i = 1; i <= m; i++) {
      for (int j = i+1; j <= m; j++) {
        char * num = nextNum(d, '1');
        num[i] = '1';
        num[d-1-i] = num[i];
        num[j] = '1';
        num[d-1-j] = num[j];
        // printf("  %s\n", num);
      }
    }

    for (int i = 1; i <= m; i++) {
      for (int j = i+1; j <= m; j++) {
        for (int k = j+1; k <= m; k++) {
          char * num = nextNum(d, '1');
          num[i] = '1';
          num[d-1-i] = num[i];
          num[j] = '1';
          num[d-1-j] = num[j];
          num[k] = '1';
          num[d-1-k] = num[k];
          // printf("  %s\n", num);
        }
      }
    }

    // we can afford 4th one if it is the middle digit when d is odd.
    if (d % 2 == 1) {
      for (int i = 1; i < m; i++) {
        for (int j = i+1; j < m; j++) {
          for (int k = j+1; k < m; k++) {
            char * num = nextNum(d, '1');
            num[m] = '1';
            num[i] = '1';
            num[d-1-i] = num[i];
            num[j] = '1';
            num[d-1-j] = num[j];
            num[k] = '1';
            num[d-1-k] = num[k];
            // printf("  %s\n", num);
          }
        }
      }
    }
  }

  for (int d = 2; d <= D; d += 2) {
    // leading digit 2: 200002
    char * num = nextNum(d, '2');
    // printf("  %s\n", num);
  }
  for (int d = 1; d <= D; d += 2) {
    char * num;
    int m = (d - 1) >> 1;  // index of the middle digit

    // leading digit 2: 20002 20102
    num = nextNum(d, '2');
    // printf("  %s\n", num);

    if (d <= 2) continue;

    num = nextNum(d, '2');
    num[m] = '1';
    // printf("  %s\n", num);

    // middle digit 2: 1002001
    num = nextNum(d, '1');
    num[m] = '2';
    // printf("  %s\n", num);

    // middle digit 2 with one extra 1: 1012101 1102011
    if (d <= 3) continue;
    for (int i = 1; i < m; i++) {
      num = nextNum(d, '1');
      assert(m != i);
      num[m] = '2';
      num[i] = '1';
      num[d-1-i] = num[i];
      // printf("  %s\n", num);
    }
  }

  qsort(buf, total, D+1, compareNum);
  for (int i = 0; i < total; i++) computeSquare(i);
  for (int i = 0; i < total; i++) {
    // printf("%4d %s\n", i+1, nums[i]);
    if (test && (i < 100 || i > total - 1000))
      printf("%4d %s %s\n", i, nums[i], sqs[i]);
  }
}

// search first item in the table >= num
int binarySearch(char* num, int min, int max) {
  if (test) printf("search %s in range [%d,%d] %s %s\n", 
    num, min, max, sqs[min], sqs[max]);
  if (min >= max) return min;
  int mid = (min+max) >> 1;
  if (min == mid) {
    if (compareNum(sqs[min], num) >= 0) return min;
    return max;
  }
  if (compareNum(sqs[mid], num) < 0) {
    return binarySearch(num, mid, max);
  } else if (compareNum(sqs[mid], num) > 0) {
    return binarySearch(num, min, mid);
  }
  return mid;
}

int binarySearch(char* num, int min) {
  return binarySearch(num, 0, total-1);
}

void solve(int cn) {
  int indexa = binarySearch(SA, 0);
  int indexb = binarySearch(SB, 0);
  // we need nums[indexb] <= SB, not bigger
  if (compareNum(sqs[indexb], SB) > 0) indexb--;
  assert(compareNum(sqs[indexb], SB) <= 0);
  assert(compareNum(sqs[indexa], SA) >= 0);
  if (indexa > 0) {
    assert(compareNum(sqs[indexa-1], SA) < 0);
  }
  if (test) printf("indexa:%d indexb:%d\n", indexa, indexb);
  printf("Case #%d: %d\n", cn, indexb - indexa + 1);
}

int main(int argc, char* argv[]) {
  test = false;
	// reopen("sample.in");
  // reopen("C-small-attempt0.in");
  // reopen("C-large-1.in");
  reopen("C-large-2.in");
  buildParlindromeTable();
  
	scanf("%d", &T);
	for(int t=1; t<=T; t++) {
    scanf("%s %s", SA, SB);
    int len = strlen(SA);
    if (SA[len-1] == ' ' || SA[len-1] == '\n') SA[len-1] = 0;
    len = strlen(SB);
    if (SB[len-1] == ' ' || SB[len-1] == '\n') SB[len-1] = 0;
    if (test) {
      printf("%s %s\n", SA, SB);
    }
    // showin();
    solve(t);
  }
 	return 0;
}