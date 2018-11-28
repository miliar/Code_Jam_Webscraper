#include<iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAXN 1009
char s[MAXN];
int sMax;

void Read() {
    scanf("%d",&sMax);
    scanf("%s",s);
}

void Solve(int testcase) {
    int counter = 0;
    int ans = 0;

    for (int i=0;i<=sMax;i++) {
        int spectator = s[i] - '0';

        if (counter < i) {
            ans += i-counter;
            counter = i;
        }

        counter += spectator;
    }

    printf("Case #%d: %d\n",testcase,ans);
}

int main () {
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);

    for (int i=1;i<=t;i++) {
        Read();
        Solve(i);
    }
}
