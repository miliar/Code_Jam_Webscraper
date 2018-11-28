#include <queue>
#include <map>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <stack>
#include <algorithm>
#include <bitset>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <math.h>
#include <list>
#include <set>
#include <complex>
#include <string.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define squere(x) ((x)*(x))
#define EPS 1e-20

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

double ans(double C, double F, double X)
{
    double res=0;
    double speed=2;
    while(1){
        if((X-C)/speed<=X/(speed+F))
            break;
        res+=C/speed;
        speed+=F;
    }
    return res+X/speed;
    // int n = ceil(((F*X/C)-2)/F-1);
    // double ans=0;

}

int main()
{
    int T;
    double C,F,X;
    cin >> T;
    rep(i,T){
        cin >> C >> F >> X;
        printf("Case #%d: %.9f\n",i+1,ans(C,F,X));
    }

    return 0;
}

