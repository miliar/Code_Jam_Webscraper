#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#define _USE_MATH_DEFINES
#include <math.h>
#include <assert.h>
#include <cstdlib>
#include <algorithm>
#include <list>

#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define LL long long
#define S(n) scanf("%d", &n)
#define Sa(n,i) scanf("%d", n+i)
#define N 2001
#define MOD 1000000007
#define EPS 0.00000001

using namespace std;

bool can(double C, double F, double X, double t){
    
    return false;
}


int main(){
#ifndef ONLINE_JUDGE
    //freopen("input.txt","rt",stdin);
    freopen("/Users/ramis/Downloads/B-large.in","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
    
    int T;
    S(T);
    
    for(int _t=1; _t <= T; ++_t){
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double speed = 2.0, t = 0;
        while(1){
            double t1 = c/speed + x/(speed + f);
            double t2 = x/speed;
            if(t1 < t2){
                t += c/speed;
                speed += f;
            }else{
                t += t2;
                break;
            }
        }
        
        
        /*double t_min=0, t_max=x/2 + 1;
        while(t_max - t_min > EPS){
            double mid = (t_min + t_max) / 2;
            if(can(c, f, x, mid)){
                t_max = mid;
            }else{
                t_min = mid;
            }
        }*/
        printf("Case #%d: %.9f\n", _t, t);
    }
    
    
    return 0;
}

