//
//  main.cpp
//  word
//
//  Created by Estelle :) on 16/4/16.
//  Copyright © 2016 Estelle :). All rights reserved.
//

#include <iostream>
#include <cstdio>
using namespace std;
char w[1005];
string ans;

void rec(int l, int r) {
    if (r<l) return;
    int x=0, y;
    for (int i=l; i<=r; i++) {
        if ((int)w[i]>=x) {
            x=(int)w[i];
            y=i;
        }
    }
    ans+=(char)x;
    rec(l,y-1);
    for (int i=y+1; i<=r; i++) ans+=w[i];
}

int main() {
    int tc;
    scanf("%d", &tc);
    for (int i=1; i<=tc; i++) {
        ans="";
        scanf("%s", w);
        rec(0,(int)strlen(w)-1);
        printf("Case #%d: %s\n", i, ans.c_str());
    }
}
