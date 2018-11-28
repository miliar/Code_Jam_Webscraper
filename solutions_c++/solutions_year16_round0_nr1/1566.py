/*
Problem Name : 
Author       : KZ
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

#define INVALID -1
#define INF  1000000000
#define INFL (long)INF*INF

#define _max(a, b)                 ((a) > (b) ? (a):(b))
#define _min(a, b)                 ((a) < (b) ? (a):(b))
#define _abs(a)                    ((a) > 0 ? (a): -(a))
#define _swap(a, b, t)             do { t=a; a=b; b=t; } while(0)
#define _isEqual(a, b)             (_abs((a) - (b)) < 1e-6)
#define _rscanf                    ret = scanf

typedef std::vector<int> IntVec;
typedef std::vector<long> LongVec;
typedef std::vector<double> DoubleVec;
typedef std::map<std::string, int> StrIntMap;

#define _stl_iter(obj, it) for(typeof(obj.begin()) it = obj.begin(); it != obj.end(); it++) 

int digits[10], count;

void mark(long t) {
  if(digits[t % 10] == 0) {
    digits[t % 10] = 1;
    count++;
  }
  if(t/10)
    mark(t/10);
  return;
}

int main(void) {
  int T, kase, ret;
  long n, i;
  
  _rscanf("%d", &T);
  for(kase=1;kase<=T;kase++) {
    _rscanf("%ld", &n);

    if(n == 0) {
      printf("Case #%d: ", kase);
      printf("INSOMNIA\n");
    }
    else {
      count = 0;
      memset(digits, 0, sizeof(digits));
      i = 1;
      while(1) {
	mark(n * i);
	if(count == 10) break;
	i++;
      }
      printf("Case #%d: %ld\n", kase, n * i);
    }
  }

  return 0;
}
