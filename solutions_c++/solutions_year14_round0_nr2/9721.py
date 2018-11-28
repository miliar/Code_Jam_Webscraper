/*Santiago Zubieta*/
#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <iterator>
#include <algorithm>  

using namespace std;

const double EPS = 1e-7;
int cmp (double x, double y = 0, double tol = EPS){
    return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
    // x < y : -1
    // x = y :  0
    // x > y :  1
}

double C, F, X;
// C: cost for buying a factory >:O
// F: production rate that each factory increases :D
// X: final amount of cookies we want :3
double calculate(double rate){
    double t1 = X / rate; // Wait until the end
    double t2 = C / rate; // Wait until factory
    double res = t2 + (X / (rate + F)); // What if waiting
    // until the end at the next step...
    if(cmp(t1, res) == -1) return t1;
    else return t2 + calculate(rate + F);
}

int main(){
    int T;
    scanf("%d", &T);
    for(int z = 0; z < T; z++){
        scanf("%lf %lf %lf", &C, &F, &X);
        double result = calculate(2);
        printf("Case #%d: ", z + 1);
        printf("%.7lf", result);
        if(z + 1 < T){
            printf("\n");
        }
    }
}