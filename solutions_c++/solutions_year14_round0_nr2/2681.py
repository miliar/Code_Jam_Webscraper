#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

const int N = 210;
const int M = 1000000;
const int inf = 0x3f3f3f3f;
const int mod = 1e9 + 7;

typedef long long ll;

double C, F, X;

int main(){
    int _, cases = 1;
    for(cin >> _; _--; ){
        printf("Case #%d: ", cases++);
        scanf("%lf %lf %lf", &C, &F, &X);
        double rate = 2, ans = 0;
        while(1){
            if(X / rate < C / rate + X / (rate + F)){
                ans += X / rate;
                break;
            }
            else{
                ans += C / rate;
                rate += F;
            }
        }
        printf("%.7f\n", ans);
    }
}