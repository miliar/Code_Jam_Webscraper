#include <iostream>
#include <string.h>
#include <stdio.h>
#include <set>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#define ll long long
#define INF 1e9
#define PI acos(-1.0)
using namespace std;
int main() {
    int T;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int cnt = 1;
    scanf("%d",&T);
    while(T--) {
        int x;
        scanf("%d",&x);
        int a[4][4];
        for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            scanf("%d",&a[i][j]);
        vector<int> v;
        for(int j = 0; j < 4; j++) v.push_back(a[x-1][j]);
        int y;
        scanf("%d",&y);
         int b[4][4];
        for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            scanf("%d",&b[i][j]);
             vector<int> p;
        for(int j = 0; j < 4; j++) p.push_back(b[y-1][j]);
        vector<int> ret;
        for(int i =0; i < 4; i++)
        {
            if(count(p.begin(),p.end(),v[i]) > 0) ret.push_back(v[i]);
        }
            if(ret.size() == 0) {
                printf("Case #%d: Volunteer cheated!\n",cnt++);continue;
            }
            if(ret.size() > 1) {
                printf("Case #%d: Bad magician!\n",cnt++);continue;
            }
            printf("Case #%d: %d\n",cnt++,ret[0]);
    }

return 0;
}

