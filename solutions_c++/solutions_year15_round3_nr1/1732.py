#include <iostream>
#include <cmath>
using namespace std;

int solve(int x);

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.out","w+",stdout);
    int T; cin>>T;
    for (int x = 1;x <= T;x++){

        cout << "Case #"<<x<<": "<<solve(x)<<endl;
    }
}

int solve(int x){
    int R,C,W; cin>>R>>C>>W;

    //if (W == 1){ return R*C; }

    int ciclos = ceil( double(C) / double(W) );

    if (R == 1){ return ciclos + W - 1; }
}