#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#define exp 1e-6
#define maxn 100002
using namespace std;

double f, c, x;
double p[maxn];

void pre(){
    int i;
    p[0] = 0.0;
    p[1] = c + 2.0*c/f;
    for(i = 2;i < maxn && p[i] < maxn;i++){
        p[i] = c + p[i-1];
    }
}

void solve(int num){
    int i;
    for(i = 1;i < maxn;i++){
        if(p[i] >= x){
            break;
        }
    }
    int j;
    double speed = 2.0;
    double time = (x-p[i-1])/(speed + (i-1)*f);
    for(j = i - 2;j >= 1;j--){
        time += c/(speed + (j)*f);
    }
    if(i > 1)
    time += p[1]/2.0;
    printf("Case #%d: %.7f\n", num, time);
}

int main()
{
    int t;
    int tt = 0;
    cin >> t;

    while(t--){
        cin >> c >> f >> x;
memset(p, 0.0, sizeof(p));
        pre();
        solve(++tt);
    }
    return 0;
}
