#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define inf 1000000000
#define MAXN 100000

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    
    for (int qwertz = 0; qwertz < t; ++qwertz) {
        int n;
        scanf("%d", &n);
        
        char number[1001];
        scanf("%s", number);
        
        int cur = 0;
        int i = 0;
        int sol = 0;
        while (number[i] != '\0') {
            if (cur < i) {
                sol++;
                cur++;
            }
            cur += number[i]-'0';
            i++;
        }

        printf("Case #%d: %d\n", qwertz+1, sol);
    }
    
    return 0;
}
