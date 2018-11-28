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


int main() {
	double c, f, x;

	freopen("/Users/study/code/codejam/B-large.in","r",stdin);
  freopen("/Users/study/code/codejam/B-large.out","w",stdout);

    int T,cas=0;scanf("%d",&T);

    while(T--){
    	printf("Case #%d: ", ++cas);

   	  scanf("%lf",&c);
      scanf("%lf",&f);
      scanf("%lf",&x);

      double totalTime = 0;
      double ff = 2;

      double buyFarmCostSecs;
      double buyFarmCostToXSecs;
      double notBuyFarmCostToXSecs;
      do {

         buyFarmCostSecs = c / ff;
         buyFarmCostToXSecs = x / (ff + f) + buyFarmCostSecs;
         notBuyFarmCostToXSecs = x / ff;

        if(notBuyFarmCostToXSecs > buyFarmCostToXSecs) {
          ff += f;
          totalTime += buyFarmCostSecs;
        } else {
          totalTime += notBuyFarmCostToXSecs;
        }

      } while(notBuyFarmCostToXSecs > buyFarmCostToXSecs);

      char str[15];
      sprintf(str, "%.7lf", totalTime);
      puts(str);

      //return 0;

/*
      c *= 100.;
      f *= 0.001;
      x *= 100.;

      double cookiePerSec = 0.002f;
      double cc = 0;
      double sec = 0;
      do {

        double xFarmCostSec = x / (cookiePerSec + f) + (c / cookiePerSec);
        double xCostSec = x / cookiePerSec;

        if(xCostSec > xFarmCostSec && cc >= c) {
          cc -= c;
          cookiePerSec += f;
        }

        sec += 0.001f;
        cc+=cookiePerSec;
      } while(cc < x);

      char str[15];
      sprintf(str, "%.7lf", sec / 100.f);
      puts(str);
*/
/*

   	    for(int i = 0; i < 4; i++){
   	    	 for(int j = 0; j < 4; j++){
   	    		scanf("%d",&a[i][j]);
   	    	}
   	    }

   	    scanf("%d",&rb);
   	    rb =rb -1;

  	    for(int i = 0; i < 4; i++){
   	    	 for(int j = 0; j < 4; j++){
   	    		scanf("%d",&b[i][j]);
   	    	}
   	    }

   	    bool flag=true;
 

   	    if(equal_arrays(a[ra], b[rb], 4) == 1 || equal_arrays2(a[ra], b[rb], 4) == 1 ) {
			flag = false;
    		puts("Bad magician!");
   	    }
   	    

		if(flag)
	  	    for(int i = 0; i < 4; i++){
	  	    	for(int j = 0; j < 4; j++) {
	  	    		if(a[ra][i] == b[rb][j]) {
	   	    			flag = false;
						char str[15];
						sprintf(str, "%d", a[ra][i]);
	   	    			puts(str);
	   	    			break;
	  	    		}
	   			}
	   	    }

	   	if(flag) {
    		puts("Volunteer cheated!");
	   	}

  */
    }

}