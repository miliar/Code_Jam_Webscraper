#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>

#include <cassert>

using namespace std;

int cmp(string a, string b){
    if(a == b) return 0;
    int x1 = 0,x2 = 0;
    int la = a.size(),lb = b.size();

    for(int i = 0;i < la - 5;++i)
        x1 = x1 * 10 + a[i] - '0';
    for(int i = 0;i < lb - 5;++i)
        x2 = x2 * 10 + b[i] - '0';

    if(x1 < x2) return -1;
    if(x1 > x2) return 1;

    x1 = 0,x2 = 0;

    for(int i = 0;i < 4;++i)
        x1 = x1 * 10 + a[la - (4 - i)] - '0';
    for(int i = 0;i < 4;++i)
        x2 = x2 * 10 + b[lb - (4 - i)] - '0';

    if(x1 < x2) return -1;
    if(x1 > x2) return 1;
    return 0;
}

void toDouble(string &s, double &x){
    istringstream is(s);
    is >> x;
}

int main(){
    //ios::sync_with_stdio(0);

    int T,N;
    string sX;
    double V,X;
    string sC[100];
    double R[100],C[100];

    cin >> T;

    for(int tc = 1;tc <= T;++tc){
        cin >> N;

        cin >> V >> sX;
        toDouble(sX,X);

        for(int i = 0;i < N;++i){
            cin >> R[i] >> sC[i];
            toDouble(sC[i],C[i]);
        }

        bool ok = true;
        double ans;

        if(N == 1 && sC[0] == sX){
            ans = V / R[0];
        }else if(N == 2 && sC[0] == sC[1]){
            if(sC[0] == sX){
                ans = V / (R[0] + R[1]);
            }else ok = false;
        }else if(N == 2){
            int c1 = cmp(sC[0],sX),c2 = cmp(sC[1],sX);

            if((c1 <= 0 && c2 >= 0) || (c1 >= 0 && c2 <= 0)){
                double r = (X - C[1]) / (C[0] - C[1]);
                ans = V * max(r / R[0],(1 - r) / R[1]);
            }else ok = false;
        }else{
            ok = false;
        }

        printf("Case #%d: ",tc);

        if(!ok) printf("IMPOSSIBLE\n");
        else printf("%.10f\n",ans);
    }

    return 0;
}