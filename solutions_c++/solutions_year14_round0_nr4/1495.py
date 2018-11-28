#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <memory.h>
#include <stack>
#include <iomanip>
#include <sstream>
#include <cmath>
using namespace std;

typedef long long int ll;

int a_score_by_game(double a[], double b[], int len){
    int idx_a = 0;
    int idx_b = 0;
    int score = 0;
    while(idx_a < len && idx_b < len){
        if(a[idx_a] > b[idx_b]) {
            score++;
            idx_a++; idx_b++;
        }else idx_b++;
    }
    return score;
}

int main (int argc, char * const argv[]){
    #ifdef LOCAL
        freopen("D-large.in", "r", stdin);
        freopen("D-large.out", "w", stdout);
    #endif // LOCAL

    int ntest;
    while(cin>>ntest){
        for(int tt=0; tt<ntest; tt++){
            int nboxs;
            cin >> nboxs;
            double a[nboxs + 1];
            double b[nboxs + 1];

            for(int i=0; i<nboxs; i++){
                cin >> a[i];
            }
            for(int i=0; i<nboxs; i++){
                cin >> b[i];
            }
            sort(a, a+nboxs, greater<double>());
            sort(b, b+nboxs, greater<double>());

            int ans[2] = {};
            if(nboxs == 1) {
                if(a[0] > b[0]){
                    ans[0] = ans[1] = 1;
                }else ans[0] = ans[1] = 0;
            }else {
                ans[0] = a_score_by_game(a, b, nboxs);
                ans[1] = nboxs - a_score_by_game(b, a, nboxs);
            }

            printf("Case #%d: %d %d\n", tt+1, ans[0], ans[1]);
        }
    }

    return 0;
}
