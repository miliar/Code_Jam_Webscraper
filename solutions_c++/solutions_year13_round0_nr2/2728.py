#include "stdio.h"
#include "string.h"
using namespace std;
int main() {
  int t;
  scanf("%d", &t);
  for(int x=1; x<=t; x++) {
    int n,m;
    scanf("%d %d", &n, &m);
    int A[n][m];
    for (int i=0; i<n; i++)
      for (int j=0; j<m; j++)
	scanf("%d", &A[i][j]);
    bool isOK=true;
    for (int i=0; i<n; i++)
      for (int j=0; j<m; j++)
	if(A[i][j] > 100) isOK=false;
    if (!isOK) { printf("Case #%d: NO\n", x); continue;}
    else {
      for (int i=0; i<n; i++) {
	int rowmin = A[i][0];
	bool allequal = true;
	for (int j=1; j<m; j++) {
	  if (rowmin > A[i][j]) {
	    allequal=false;
	    rowmin = A[i][j];
	  }
	  if (rowmin < A[i][j]) allequal = false;
	}
	if (!allequal) {
	  for (int j=0; j<m; j++) {
	    if (A[i][j] == rowmin) {
	      //printf("Case #%d : n = %d, m = %d"
	      //"Checking column for %d\n", x, n, m, rowmin); 
	      for(int y=0; y<n; y++) {
		if (A[i][j] < A[y][j]) {
		  isOK = false;
		  break;
		}
	      }
	      if (!isOK) break;
	    }
	    if (!isOK) break;
	  }
	}
	if (!isOK) break;
      }
      if (isOK) {
	printf("Case #%d: YES\n", x);
      } else {
	printf("Case #%d: NO\n", x);
      }
    }
  }
}