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

#define MAX 65536

int digitLetter[256];
char buf[MAX];

int main(void) {
  int T, kase, ret;
  
  _rscanf("%d", &T);
  for(kase=1;kase<=T;kase++) {
    _rscanf("%s", buf);
    int i, count[10];
    memset(digitLetter, 0, sizeof(digitLetter));
    for(i=0;buf[i];i++)
      digitLetter[buf[i]]++;
    
    count[0] = digitLetter['Z'];
    count[2] = digitLetter['W'];
    count[4] = digitLetter['U'];
    count[6] = digitLetter['X'];
    count[8] = digitLetter['G'];
    count[3] = digitLetter['H']-digitLetter['G'];
    count[5] = digitLetter['F']-digitLetter['U'];
    count[7] = digitLetter['S']-digitLetter['X'];
    count[1] = digitLetter['O']-digitLetter['Z']-digitLetter['W']-digitLetter['U'];
    count[9] = digitLetter['I']-count[5] - count[6] - count[8];

    printf("Case #%d: ", kase);
    for(int j=0;j<10;j++)
      for(i=0;i<count[j];i++)
	printf("%d", j);
    printf("\n");
  }

  return 0;
}
