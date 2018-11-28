#include <iostream>
#include <cstdio>
using namespace std;


int grid[60][60];

int main() {
  int t;

  cin >> t;

  for(int zz = 1; zz <= t; zz++) {
    int r,c,m;
    cin >> r >> c >> m;
    int left = r*c-m;


    printf("Case #%d:\n", zz);

    if(r==1) { // always possible

      printf("c");
      for(int i = 1; i < left; i++) printf(".");
      for(int i = left; i < c; i++) printf("*");
      printf("\n");

    } else if (c == 1) { // always possible

      printf("c\n");
      for(int i = 1; i < left; i++) printf(".\n");
      for(int i = left; i < r; i++) printf("*\n");

    } else if (left==1) { // always possible

      for(int i = 0; i < r; i++) {
	for(int j = 0; j < c; j++) {
	  if(i==0 && j==0)printf("c");
	  else printf("*");
	}
	printf("\n");
      }

    } else {

      bool isGood = false;
      for(int l = 0; l+2 <= r; l++) {
	for(int k = 0; k+2 <= c; k++) {
	  int taken = 4 + l*2 + k*2;
	  if(left >= taken && (left-taken) <= l*k) {
	    isGood = true;
	    
	    for(int i = 0; i < r; i++)
	      for(int j = 0; j < c; j++)
		grid[i][j] = 0;

	    for(int i = 0; i < l+2; i++) {
	      for(int j = 0; j < 2; j++) {
		grid[i][j] = 1;
	      }
	    }

	    for(int i = 0; i < 2; i++) {
	      for(int j = 0; j < k+2; j++) {
		grid[i][j] = 1;
	      }
	    }

	    int nowleft = left-taken;
	    int ci = 2, cj = 2;
	    while(nowleft > 0) {
	      grid[ci][cj] = 1;
	      ci++;
	      if(ci >= l+2) {
		cj++;
		ci = 2;
	      }
	      nowleft--;
	    }

	    printf("c");
	    for(int i = 0; i < r; i++) {
	      for(int j = 0; j < c; j++) {
		if(i != 0 || j != 0) {
		  if(grid[i][j]) {
		    printf(".");
		  } else {
		    printf("*");
		  }
		}
	      }
	      printf("\n");
	    }


	    break;
	  }
	}
	if(isGood) break;
      }
      
      if(!isGood) {

	printf("Impossible\n");
      }
    }
  }


  return 0;
}
