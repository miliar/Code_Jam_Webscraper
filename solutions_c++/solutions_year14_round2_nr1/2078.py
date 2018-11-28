#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <string>
#include <iostream>
using namespace std;

int calcAns(vector< vector<int> > &vn) {
    int ans = 0;
    for (int i = 0; i < vn.size(); i++) {
        int s = 0;
        for (int j = 0; j < vn[i].size(); j++)
            s += vn[i][j];
        int m = (int)round(s / vn[i].size());
        for (int j = 0; j < vn[0].size(); j++)
            ans += (int)abs(vn[i][j] - m);
    }
    return ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testsCnt;
    scanf("%d", &testsCnt);
    for (int testN = 1; testN <= testsCnt; testN++) {
        int n;
        scanf("%d", &n);
        vector<char> vc;
        vector< vector<int> > vn;
        bool badString = false;
        for (int i = 0; i < n; i++) {
            char s[110];
            scanf(" %s", s);            
            if (vc.empty()) {
                vc.push_back(s[0]);
                for (int j = 1; s[j]; j++) {
                    if (s[j] == s[j - 1])
                        continue;
                    vc.push_back(s[j]);
                }
                vn.resize(vc.size());
            }
            int startPos = 0, endPos = 0;
            for (int j = 0; j < vc.size(); j++) {
                if (s[startPos] != vc[j]) {
                    badString = true;
                    break;
                }
                while (s[endPos] == s[startPos])
                    endPos++;
                vn[j].push_back(endPos - startPos);
                startPos = endPos;
            }
            if (s[startPos])
                badString = true;
            if (badString)
                break;
        }
        if (badString)
            printf("Case #%d: Fegla Won\n", testN);
        else
            printf("Case #%d: %d\n", testN, calcAns(vn));
    }

}