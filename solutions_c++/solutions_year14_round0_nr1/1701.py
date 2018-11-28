
/*
ID: wengsht1
LANG: C++
TASK: test
*/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <sstream>
#include <set>
using namespace std;

#define MX 100005
#define REP(i,n) for(int i=0;i<(n);i++)
#define OREP(i,n) for(int i=1;i<=(n);i++)

typedef long long          LL;
typedef unsigned long long ULL;
typedef unsigned int       UINT;

int n, m, k, t;

bool has1[17], has2[17];

void getx(bool *arr) {
    memset(arr, false, sizeof(bool) * 17);
    
    int r, c;
    scanf("%d", &r);
    OREP(i, 4) {
        OREP(j, 4) {
            scanf("%d", &c);
            if(i == r) 
                arr[c] = true;
        }
    }
}
int main() {
    scanf("%d", &t);
    
    OREP(c, t) {
        getx(has1);
        getx(has2);
        
        int res = -1;
        OREP(i, 16) {
            if(has1[i] && has2[i]) {
                if(res == -1) res = i;
                else res = -2;
            }
        }
        
                
        printf("Case #%d: ", c);
        
        if(res == -1) {
            printf("Volunteer cheated!\n");
        }
        else if(res == -2) {
            printf("Bad magician!\n");
        }
        else {
            printf("%d\n", res);
        }
    }
    return 0;
}

