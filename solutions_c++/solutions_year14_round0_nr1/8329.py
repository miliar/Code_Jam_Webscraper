#include <string.h>
#include <stdio.h>
#include <math.h>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <limits>

using namespace std;


int main(){
    int c;
    int tmp;
    scanf("%d",&c);
    int set1[4][4];
    int set2[4][4];
    int casenum = 0;
    while(c--){
    	casenum++;
    	int hint1, hint2;
    	scanf("%d", &hint1);
    	for(int i=0;i<4;i++){
    		scanf("%d %d %d %d", &set1[i][0], &set1[i][1], &set1[i][2], &set1[i][3]);
    	}
    	scanf("%d", &hint2);
    	for(int i=0;i<4;i++){
    		scanf("%d %d %d %d", &set2[i][0], &set2[i][1], &set2[i][2], &set2[i][3]);
    	}
    	int chkcnt = 0;
    	int found;
    	for(int i=0;i<4;i++){
    		if(set1[hint1-1][i] == set2[hint2-1][0] ||
    		set1[hint1-1][i] == set2[hint2-1][1] ||
    		set1[hint1-1][i] == set2[hint2-1][2] ||
    		set1[hint1-1][i] == set2[hint2-1][3]
    		){
    			chkcnt++;
    			found = set1[hint1-1][i];
    		}
    	}
    	if (chkcnt == 1) printf("Case #%d: %d\n", casenum, found);
    	else if (chkcnt > 1) printf("Case #%d: Bad magician!\n", casenum);
    	else printf("Case #%d: Volunteer cheated!\n", casenum);
    }

    return 0;

}
