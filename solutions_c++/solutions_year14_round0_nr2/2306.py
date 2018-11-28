#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define LL long long
using namespace std;

int main(){
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);
    int t;
    int tt = 0;
    scanf("%d", &t);
    while(t--){
        double C, F, X, ans = 0., V = 2.;
        cin >> C >> F >> X;
        while(1){
            double tmp1 = X / V;
            double tmp2 = C / V + X / (V + F);
            //cout<<"  =====  "<<tmp1<<"  "<<tmp2<<endl;
            if(tmp1 <= tmp2){
                ans += tmp1;
                break;
            }
            else{
                ans += C / V;
                V += F;
            }
        }
        printf("Case #%d: %.7f\n", ++tt, ans);
    }
	return 0;
}
