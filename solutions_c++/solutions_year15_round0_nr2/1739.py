
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <algorithm>
#define maxv 1009

using namespace std;

int T;
int F[maxv][maxv];

void input(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
}

void createF() {

    for (int j=1;j<=1000;j++) {
        for (int i=1;i<=1000;i++) {
            if (i<=j){
                F[i][j] = 0;
            } else {
                F[i][j] = maxv;
                for (int k=1; k<=i-1; k++) {
                    F[i][j] = min(F[i][j],F[k][j]+F[i-k][j]+1);
                }
            }

        }
    }
}

void solve(){

    int p[maxv];
    int n,sum,res;
    cin>>T;
    createF();
    for (int t=0;t<T; t++) {
        cin>>n;
        for (int i=1; i<=n ; i++) {
            cin>>p[i];
        }
        res=100000009;
        for (int j=1; j<=1000; j++) {
            sum = 0;
            for (int i=1;i<=n;i++) {
                sum+=F[p[i]][j];
            }

            res=min(res,sum+j);
        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
}

void output(){

}

void process(){
    input();
    solve();
    output();
}

int main() {
    process();
    return 0;
}

