#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<vector<int> > VII;
typedef vector<PII> VPII;

typedef vector<double> VD;
typedef vector<string> VS;

typedef long long LL;

int A[4][4];
int B[4][4];
bool possibleA[17];
bool possibleB[17];

int main(){ 	
	int cases;
	scanf("%d\n", &cases);
	
	for(int caseNr = 1; caseNr <= cases; caseNr++){
	  // INIT
	  memset(A, 0, sizeof(A));
	  memset(B, 0, sizeof(B));
	  memset(possibleA, false, sizeof(possibleA));
	  memset(possibleB, false, sizeof(possibleB));
	  
	  // READ
	  int c1, c2;
	  scanf("%d\n", &c1);
	  for(int i=0; i<4; i++) for(int j=0; j<4; j++) scanf("%d", &A[i][j]);
	  scanf("%d\n", &c2);
	  for(int i=0; i<4; i++) for(int j=0; j<4; j++) scanf("%d", &B[i][j]);
	  
	  --c1;
	  --c2;
	  
	  // PROCESS
	  for(int i=0; i<4; i++)
	    possibleA[A[c1][i]]=true;
	  for(int i=0; i<4; i++)
	    possibleB[B[c2][i]]=true;
	  
	  int matches = 0;
	  int lastMatch = -1;
	  for(int i=1; i<=16; i++){
	    if(possibleA[i] && possibleB[i]){
	      ++matches;
  	    lastMatch = i;
	    }
	  }
	
		// OUTPUT
		printf("Case #%d: ", caseNr);
    if(matches == 0){
      printf("Volunteer cheated!");
    }else if(matches == 1){
      printf("%d", lastMatch);
    }else{
      printf("Bad magician!");
    }
		
		printf("\n");
		fflush(stdout);
	}
	
	return 0;
}
