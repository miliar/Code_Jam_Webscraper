/*
Author : Md Kamruzzaman
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

#define INVALID -1

#define _max(a, b)                 ((a) > (b) ? (a):(b))
#define _min(a, b)                 ((a) < (b) ? (a):(b))
#define _abs(a)                    ((a) > 0 ? (a): -(a))
#define _swap(a, b, t)             do { t=a; a=b; b=t; } while(0)
#define _isEqual(a, b)             (_abs((a) - (b)) < 1e-6)
#define _rscanf                    ret = scanf

using namespace std;

typedef vector<int> IntVec;
typedef vector<long> LongVec;
typedef vector<double> DoubleVec;
typedef map<string, int> StrIntMap;

#define _stl_iter(obj, it) for(typeof(obj.begin()) it = obj.begin(); it != obj.end(); it++) 

long m[1001];
long N;

int main(void) {
  int T, kase, ret;
  
  _rscanf("%d", &T);
  for(kase=1;kase<=T;kase++) {
    long i, j, mx = 0;

    _rscanf("%ld", &N);
    for(i=0;i<N;i++) {
      _rscanf("%ld", &m[i]);
      mx = _max(mx, m[i]);
    }

    long x=0, y, s, r, mg = 0;
    double mr = 0;

    s = m[0];
    for(i=1;i<N;i++) {
      if(s > m[i])
	x += s - m[i];
      s = m[i];
      if(((double)m[i-1] - m[i])/10.0 > mr) {
	mr = ((double)m[i-1] - m[i])/10.0;
	mg = m[i-1] - m[i];
      }
    }

    //    printf("%lf %ld\n", mr, mg);
    long k = 0;
    y = 0;
    s = m[0];
    for(i=1;i<N;i++) {
      if(mg >= m[i-1])
	k += m[i-1];
      else {
	if(m[i] >= m[i-1] - mg)
	  k += mg;
	else
	  k += (m[i] - m[i-1]);
      }
    }
    y = k;
    printf("Case #%d: %ld %ld", kase, x, y);
    printf("\n");
  }

  return 0;
}
