/*
 * Author: fatboy_cw
 * Created Time:  2014/4/12 11:12:02
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
const double eps = 1e-9;

int sgn(double x) {
    return (x > eps) - (x < -eps);
}

int t, ca;
double c, f, x;

double solve() {
    double tnow = 0.0;
    double per = 2.0;
    while(1) {
        double t1 = x / per;
        double t2 = c / per + x / (per + f);
        if(sgn(t1 - t2) > 0) {
            tnow += c / per;
            per += f;
        }
        else {
            tnow += x / per;
            return tnow;
        }
    }
}

int main() {
    freopen("B2.in", "r", stdin);
    freopen("B2.out", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        scanf("%lf%lf%lf", &c, &f, &x);
        printf("Case #%d: %.7lf\n", ++ca, solve());
    }
    return 0;
}

