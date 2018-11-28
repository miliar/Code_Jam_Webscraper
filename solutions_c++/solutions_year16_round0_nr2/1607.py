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

void flip(char *s, int start, int end) {
  char t;
  int i, j;
  for(i=start, j=end;i<j;i++, j--) {
    t = s[i];
    s[i] = s[j];
    s[j] = t;
  }
  for(i=start;i<=end;i++) {
    if(s[i] == '+') s[i] = '-';
    else if(s[i] == '-') s[i] = '+';
  }
  return;
}

int minFlip(char *s, int start, int end) {
  if(end < start) return 0;
  if(s[end] == '+') return minFlip(s, start, end-1);
  if(s[start] == '-') {
    flip(s, start, end);
    return minFlip(s, start, end-1) + 1;
  }
  int i = end-1;
  for(;i>=start && s[i]=='-';i--);
  assert(i>=start);
  flip(s, start, i);
  assert(s[start] == '-');
  flip(s, start, end);
  return minFlip(s, start, end-1) + 2;
}
    
int main(void) {
  int T, kase, ret;
  char s[200];
  
  _rscanf("%d", &T);
  for(kase=1;kase<=T;kase++) {
    _rscanf("%s", s);
    int m = minFlip(s, 0, strlen(s)-1);
    printf("Case #%d: ", kase);
    printf("%d\n", m);
  }

  return 0;
}
