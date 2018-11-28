#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define min(X,Y) (X<Y?X:Y)
#define max(X,Y) (X<Y?Y:X)

using namespace std;


int main() {
    int totalTests;
    scanf("%d", &totalTests);
    for (int test=1; test<=totalTests; test++) {
        printf("Case #%d:", test);
        int sMax;
        scanf("%d",&sMax);

        int numOfFriends = 0;
        int numOfMembers = 0;
        for (int i=0; i<(sMax+1); i++) {
            char c;
            scanf(" %c",&c);
            int curSLevelMembers = c-'0';
            //printf(" i=%d curSLevelMembers = %d numOfMem=%d\n", i, curSLevelMembers, numOfMembers);
            if(curSLevelMembers==0) continue;
            if(i==0) {
                numOfMembers = curSLevelMembers;
                continue;
            }
            if(i<=(numOfMembers+numOfFriends)) {
                numOfMembers += curSLevelMembers;
            } else {
                numOfFriends = max(numOfFriends,i-numOfMembers);
                numOfMembers += curSLevelMembers;
            }
            
            //printf(" numFriends=%d\n", numOfFriends);
        }
        printf(" %d\n",numOfFriends);
    }
}