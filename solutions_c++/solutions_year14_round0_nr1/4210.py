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


int equal_arrays(int a1[], int a2 [], int n)
{
    int i, result;
        for (i=0; i<n; ++i)
            if (a1[i] != a2[i])
                                return 0;
    return (1);
}


int equal_arrays2(int a1[], int a2 [], int n)
{
	int hitcnt = 0;
    int i, j, result;
    for (i=0; i<n; ++i)
    	for (j=0; j<n; ++j)
			if(a1[i]==a2[j])
    			hitcnt++;

    
    if(hitcnt>1) 
        return 1;

    return (0);
}

int main() {
	int ra, rb;

	int a[4][4];
	int b[4][4];

	freopen("/Users/study/code/codejam/A-small-attempt2.in","r",stdin);
    freopen("/Users/study/code/codejam/A-small-attempt2.out","w",stdout);

    int T,cas=0;scanf("%d",&T);

    while(T--){
    	printf("Case #%d: ", ++cas);
   	    scanf("%d",&ra);
   	       	    ra =ra -1;


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
    }

}