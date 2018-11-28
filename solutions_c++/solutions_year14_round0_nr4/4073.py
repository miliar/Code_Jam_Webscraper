#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <algorithm>
#define forn(i,n) for(int i=0;i<n;i++)
#define clr(a,b) memset(a,b,sizeof(a))
#define ll long long
#define Min(a,b) if(a>b)a=b
#define MP(x,y) make_pair(x,y)
#define sqr(x) ((x)*(x))
using namespace std;

#define RI(a) scanf("%d",&(a))
using namespace std;

int cmpfunc (const void * a, const void * b)
{
if (*(double*)a > *(double*)b) return -1;
else if (*(double*)a < *(double*)b) return 1;
return 0;
}


int main() {

  //freopen("/Users/study/code/codejam/D-sample.in","r",stdin);
  freopen("/Users/study/code/codejam/D-large.in","r",stdin);
  freopen("/Users/study/code/codejam/D-large.out","w",stdout);

  int T, N, cas=0;scanf("%d",&T);

  double naomi[1000] = {0.0f};
  double ken[1000] = {0.0f};

  int wp = 0;
  int dwp = 0;

  while(T--){
  	printf("Case #%d: ", ++cas);
    scanf("%d",&N);

    for(int i = 0; i < N; i++) {
      scanf("%lf", &naomi[i]);
    }

    for(int i = 0; i < N; i++) {
      scanf("%lf", &ken[i]);
    }

      std::qsort(naomi, N, sizeof(double), cmpfunc);
      std::qsort(ken, N, sizeof(double), cmpfunc);
    

    int z = 0;
    int j = 0;
    for(int i = 0; i < N; i++) {
      if(naomi[i] > ken[j]) {
        z++;
      } else {
        j++;
      }
    }


/*
    printf("\n");

    for(int i = 0; i < N; i++) {
      printf("%.3f ", naomi[i]);
    }printf("\n");

    for(int i = 0; i < N; i++) {
      printf("%.3f ", ken[i]);
    }
    printf("\n");

    */

int y = 0;
    int ii = 0, iii= 0;
    for(int i = 0; i < N; i++) {
      //printf("%.3f , %.3f \n",  naomi[i], ken[ii]);

      if(naomi[i] == -1) break;
      if(ken[ii] == -1) break;

      if(naomi[i] < ken[ii]) {
        //printf("i=%d ii=%d %.3f => %.3f \n", i, ii, naomi[N -1 - iii], ken[ii]);
        ken[ii] = naomi[N -1 -iii] = -1;
        ii++;
        iii++;
        i--;
      } else if (naomi[i] > ken[ii]){
		naomi[i] = ken[ii] = -1;
		ii++;
		y++;
      }
      if(ii >= N) break;
    }

/*
       printf("\n");

    for(int i = 0; i < N; i++) {
      printf("%.3f ", naomi[i]);
    }printf("\n");

    for(int i = 0; i < N; i++) {
      printf("%.3f ", ken[i]);
    }
    printf("\n");

*/
    printf("%d %d\n", y, z);
  }



}