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

int cur_count = 0, mx_scm = 0;
int N;

int perm[1000], mark[1000];
int bff[1000];

int isFeasible(int p) {
  int i;

  for(i=1;i<p-1;i++) {
    if((bff[perm[i]] == perm[i-1]) || (bff[perm[i]] == perm[i+1]))
      continue;
    return 0;
  }
  if(((bff[perm[0]] == perm[1]) || (bff[perm[0]] == perm[p-1])) &&
     ((bff[perm[p-1]] == perm[p-2]) || (bff[perm[p-1]] == perm[0])))
    return p;
  return 0;
}

void gen_npr(int pos, int p) {
  if(pos == p) {
    int t = isFeasible(p);
    mx_scm = _max(mx_scm, t);
    return;
  }
  int i;
  for(i=0;i<N;i++) {
    if(mark[i]) continue;
    perm[pos] = i;
    mark[i] = 1;
    gen_npr(pos+1, p);
    mark[i] = 0;
    if(mx_scm > 0) return;
  }
  return;
}
    
int main(void) {
  int T, kase, ret;
  
  _rscanf("%d", &T);
  for(kase=1;kase<=T;kase++) {
    _rscanf("%d", &N);
    memset(bff, 0, sizeof(bff));
    int i;
    for(i=0;i<N;i++) {
      int v;
      _rscanf("%d", &v);
      bff[i] = v-1;
    }

    mx_scm = 0;
    if(N < 4)
      mx_scm = N;
    else {
      int p = N;
      for(p=N;p >= 2; p--) {
	memset(perm, 0, sizeof(perm));
	memset(mark, 0, sizeof(mark));
	gen_npr(0, p);
      }
    }
	
    printf("Case #%d: %d", kase, mx_scm);
    printf("\n");
  }

  return 0;
}
