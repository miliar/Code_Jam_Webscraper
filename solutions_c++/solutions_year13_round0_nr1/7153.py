#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <deque>
#include <stack>
#include <bitset>
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

using namespace std;

long solve(long t){ 
    long i,j;
    long full = 1;
    string a[4];
    long d = 1;
    for (i = 0; i < 4; i ++) 
        cin >> a[i];
    for (i = 0; i < 4; i ++) 
        for (j = 0; j < 4; j ++) if (a[i][j] == '.') full = 0;
    if (t == 5) {
        t = 5;
    }
    char ch = 'X';
    for (i = 0; i < 4; i ++) {
        d = 1;
        for (j = 0; j < 4; j ++) 
            if (!(a[i][j] == ch || a[i][j] == 'T')) d = 0;
        if (d) {
            printf("Case #%d: %c won\n",t+1,ch);
            return 0;
        }
    }
    for (i = 0; i < 4; i ++) {
        d = 1;
        for (j = 0; j < 4; j ++) 
            if (!(a[j][i] == ch || a[j][i] == 'T')) d = 0;
        if (d) {
            printf("Case #%d: %c won\n",t+1,ch);
            return 0;
        }
    }
    d = 1;
    for (i =0; i < 4; i ++) if (!(a[i][i] == ch || a[i][i] == 'T')) d = 0;
        if (d) {
            printf("Case #%d: %c won\n",t+1,ch);
            return 0;
        }
    d = 1;
    for (i =0; i < 4; i ++) if (!(a[3-i][i] == ch || a[3-i][i] == 'T')) d = 0;
        if (d) {
            printf("Case #%d: %c won\n",t+1,ch);
            return 0;
        }
    
    
    
    ch = 'O';
    for (i = 0; i < 4; i ++) {
        long d = 1;
        for (j = 0; j < 4; j ++) 
            if (!(a[i][j] == ch || a[i][j] == 'T')) d = 0;
        if (d) {
            printf("Case #%d: %c won\n",t+1,ch);
            return 0;
        }
    }
    for (i = 0; i < 4; i ++) {
        long d = 1;
        for (j = 0; j < 4; j ++) 
            if (!(a[j][i] == ch || a[j][i] == 'T')) d = 0;
        if (d) {
            printf("Case #%d: %c won\n",t+1,ch);
            return 0;
        }
    }
    d = 1;
    for (i =0; i < 4; i ++) if (!(a[i][i] == ch || a[i][i] == 'T')) d = 0;
        if (d) {
            printf("Case #%d: %c won\n",t+1,ch);
            return 0;
        }
    d = 1;
    for (i =0; i < 4; i ++) if (!(a[3-i][i] == ch || a[3-i][i] == 'T')) d = 0;
        if (d) {
            printf("Case #%d: %c won\n",t+1,ch);
            return 0;
        }
    if (full == 0) {        
        printf("Case #%d: Game has not completed\n",t+1,ch);
        return 0;
    }
    printf("Case #%d: Draw\n",t+1);
}

int main () {
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    long T,i,j;
    cin >> T;
    for (i = 0; i < T; i ++) {
        solve(i);
    }
    return 0;
}

