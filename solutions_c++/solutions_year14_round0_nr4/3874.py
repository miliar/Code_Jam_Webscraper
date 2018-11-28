#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#define MAXN 1001
#define ll long long

using namespace std;

int t, n;
double bn[1001], bk[1001];

int main(void){
    freopen("in.in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &t);
    for(int test = 1; test <= t; test++){
        scanf("%d", &n);
        double great = 0;
        for(int i = 0; i < n; i++){
            scanf("%lf", &bn[i]);
            //cout << bn[i] << endl;
            great = max(great, bn[i]);
        }
        int low = 0;
        for(int i = 0; i < n; i++){
            scanf("%lf", &bk[i]);
        }
        sort(bn, bn+n);
        sort(bk, bk+n);
        int last1 = n-1, last2 = 0;
        int inWar = 0, notWar = 0;
        for(int i = 0; i < n; i ++){
            if(bn[i] > bk[low]){
                notWar ++;
                low++;
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = last2; j < n; j++){
                if(bk[j] > bn[i] && bk[j] != -1.){
                    bk[j] = -1;
                    last2 = j+1;
                    break;
                }
            }
        }
        for(int i = 0; i < n; i++){
            if(bk[i] != -1){
                inWar++;
            }
        }
        printf("Case #%d: %d %d\n", test, notWar, inWar);
    }
    return 0;
}
