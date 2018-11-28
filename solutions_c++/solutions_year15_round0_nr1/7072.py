#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
#include <stack>
#include <bitset>
#include <list>
#include <limits.h>
#include <iomanip>
#include <time.h>

using namespace std;


#define ii pair<int,int>
#define iii pair<int,ii>
#define INF 1000000000
typedef long long int ll;
typedef unsigned long long int ull;
typedef vector <int> vi;
typedef vector <ii> vii;

void testing (string position = "top"){
  // return ;
  
  static clock_t clock_tStart;
  
  if (position=="top"){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
  
    clock_tStart = clock();
  }
  else if(position=="bottom"){
    // printf("\n\nTime taken: %fs\n\n", (double)(clock() - clock_tStart)/CLOCKS_PER_SEC);
  }
}

int main (){
	testing("top");
    
    int t;
    scanf("%d",&t);
    
    int kasus=1;
    while (t--){
        printf("Case #%d: ", kasus++);
        int smax;
        char people[1003];
        scanf("%d %s", &smax, people);
        
        int len = smax+1;
        
        int ans =0;
        int totalStandUp = 0;
        
        for (int snow=0;snow<len;snow++){
            int pnow = people[snow] - '0';
            
            if (snow>totalStandUp){
                ans += snow-totalStandUp;
                totalStandUp = snow;
            }
            
            totalStandUp += pnow;
        }
        
        printf("%d\n",ans);
        
    }
	
    
    
	testing("bottom");
	return 0;
}













