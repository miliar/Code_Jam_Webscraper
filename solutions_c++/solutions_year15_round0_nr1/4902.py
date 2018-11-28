#include<bits/stdc++.h>

using namespace std;

char lol[5000];

void solve() {

    int n;

    scanf("%d%s",&n, lol);


    int jml_sblm = 0;
    int o =0 ;
    for(int i =0 ; i <= n; i++) {
        int v = lol[i] - '0';
        int t = 0;
        if(jml_sblm < i) {
            t = i-jml_sblm;
            o+=t;
        }
        jml_sblm+=v+t;

    }
    //printf("%s ", lol);
    printf("%d\n", o);
}

int main() {
    int tc;
    scanf("%d", &tc);
    for(int i = 1; i<=tc; i++) {
        printf("Case #%d: ",i);
        solve();
    }
}