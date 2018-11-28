//In the name of Allah

#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <bitset>
#include <math.h>
#include <queue>
#include <map>
#include <set>
#include <limits.h>
#include <limits>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
using namespace std;

int T, smax, n;
char s[1005];

int main(){
    freopen("Aout.txt", "w", stdout);
    freopen("A.txt", "r", stdin);
    
    scanf("%d", &T);
    while(T--){
        scanf("%d", &smax);
        scanf("%s", s);

        int c = 0, e = 0;
        for(int i = 0; i <= smax; i++){
            if(c >= i){
                c += s[i] - '0';
                continue;
            }
            e += i - c;
            c = i;
            c += s[i] - '0';
        }
        printf("Case #%d: %d\n", ++n, e);
    }
    return 0;
}