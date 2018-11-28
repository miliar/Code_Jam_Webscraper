#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <utility>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int t,x=1, a, i, j, b, c, d, a1[4], b1[4], ans1, ans2;
    scanf("%d", &t);
    while (x<=t) {
        scanf("%d", &ans1);
        for (i = 1; i <= 4; i++) {
            if (i == ans1)
                scanf("%d%d%d%d", &a1[0], &a1[1], &a1[2], &a1[3]);
            else
                scanf("%d%d%d%d", &a, &b, &c, &d);
        }
        scanf("%d", &ans2);
        for (i = 1; i <= 4; i++) {
            if (i == ans2)
                scanf("%d%d%d%d", &b1[0], &b1[1], &b1[2], &b1[3]);
            else
                scanf("%d%d%d%d", &a, &b, &c, &d);
        }
        int count = 0, card;
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                if (a1[i] == b1[j]) {
                    count++;
                    card=a1[i];
                }
            }
        }
        printf("Case #%d: ",x);
        if(count==1)
            printf("%d\n",card);
        else if(count>1)
            printf("Bad magician!\n");
        else if(count==0)
            printf("Volunteer cheated!\n");
        x++;
    }
    return 0;
}

