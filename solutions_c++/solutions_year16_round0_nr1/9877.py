#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <bitset>

using namespace std;

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout);
    int n; scanf("%d", &n);
    int num, sum;
    int casenum = 1;
    set<int> myset;
    while(n--) {
        scanf("%d", &num);
        int mult = 1;
        int cur = 0;
        myset.clear();
        if(!num) {
            printf("Case #%d: %s\n", casenum++, "INSOMNIA");
            continue;
        }
        bool goOn = true;
        while (goOn) {
            cur = num * mult;
            int temp = cur;
            while(temp) {
                myset.insert(temp%10);
                temp /= 10;
            }
            if (myset.size() == 10) goOn = false;
            mult++;
        }
        printf("Case #%d: %d\n", casenum++, cur);
    }//end while
    return 0;
} //end main
