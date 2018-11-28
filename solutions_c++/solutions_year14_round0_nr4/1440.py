#include <bits/stdc++.h>
using namespace std;

pair<int,int> solve(){
    int n; cin >> n;
    vector<double> naomi(n), ken(n);
    for(int i = 0; i < n; i++) cin >> naomi[i];
    for(int i = 0; i < n; i++) cin >> ken[i];


    //War
    int war = n;
    sort(begin(naomi),end(naomi));
    sort(begin(ken),end(ken));

    for(int i = 0, j = 0; j < n; j++){
        if(naomi[i] < ken[j]){
            war--;
            i++;
        }
    }


    //Deceitful War
    int dwar = 0;
    for(int i = 0; i < n; i++){
        int tmp = 0;
        for(int j = 0; j < n-i; j++){
            if(naomi[j+i] > ken[j]){
                tmp++;
            }
        }
        dwar = max(tmp, dwar);
    }

    return {dwar,war};
}

int main(){
    int t; cin >> t;
    for(int tc = 1; tc <= t; tc++){
        auto p = solve();
        printf("Case #%d: %d %d\n", tc, p.first, p.second);
    }
}

