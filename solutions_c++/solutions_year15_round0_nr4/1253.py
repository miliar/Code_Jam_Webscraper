#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
int T,N;
int X,R,C;
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin >> T;
    int tt = 0;
    while(T--){
        ++tt;

        cin>>X>>R>>C;
        int mmax = 0;
        if(R*C % X != 0)
            printf("Case #%d: RICHARD\n",tt);
        else {
            if(X <= 2)
            printf("Case #%d: GABRIEL\n",tt);
            else if(X == 3 && min(R,C) >= 2){
                printf("Case #%d: GABRIEL\n",tt);
            } else if(X == 4 && min(R,C) >= 3){
                printf("Case #%d: GABRIEL\n",tt);
            } else printf("Case #%d: RICHARD\n",tt);
        }
    }
    return 0;
}
