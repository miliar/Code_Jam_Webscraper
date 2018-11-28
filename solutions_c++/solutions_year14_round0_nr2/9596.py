//In the name of Allah

#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <bitset>
#include <math.h>
#include <queue>
#include <map>
#include <set>
#include <limits.h>
#include <limits>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
using namespace std;

int T;
double C, F, X, eps = 1e-7;

double solve(double current_rate){
    double direct = (X / current_rate);
    double buy_a_farm = (C / current_rate) + X / (current_rate + F);
    
    if(direct > buy_a_farm + eps)return (C / current_rate) + solve(current_rate + F);
    else return (X / current_rate);
}
int main(){
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        cin >> C >> F >> X;
        printf("Case #%d: %.7f\n", t, solve(2.0));
    }
    return 0;
}