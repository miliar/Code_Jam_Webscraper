#include <bits/stdc++.h>

using namespace std;

double C , F , X;
double solve(int step){
    double res = X / (2 + step*F);
    for(int i = 0; i < step;++i)
        res += C / (2 + i*F);
return res;
}

int main(){
    freopen("in.c","r",stdin);
    freopen("on.c","w",stdout);

    int tc , nc = 1;
    cin >> tc;

    while(tc--){

        cin >> C >> F >> X;

        int step = ceil((X*F - 2*C - F*C)/F/C);
        if(step < 0) step = 0;
    printf("Case #%d: %.15f\n",nc++,solve(step));
    }


return 0;
}
