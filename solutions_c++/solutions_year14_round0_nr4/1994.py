#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("D-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t; cin >> t;
    for(int te=1; te<=t; ++te){
        int n, DW=0, W=0; long double in;
        vector<long double> v1, v2;

        cin >> n;
        for(int i=1; i<=n; ++i){
            cin >> in; v1.push_back(in);
        }
        for(int i=1; i<=n; ++i){
            cin >> in; v2.push_back(in);
        }
        sort(v1.begin(), v1.end()); sort(v2.begin(), v2.end());

        int i=0, j=0;
        while(i<v1.size() && j<v2.size()){
            if(v1[i]<v2[j]){i++; j++;}
            else if(v1[i]>v2[i])j++;
        }
        W=v1.size()-i;

        i=v1.size()-1, j=v2.size()-1;
        while(i>-1 && j>-1){
            if(v1[i]>v2[j]){i--; j--; DW++;}
            else if(v1[i]<v2[j])j--;
        }
        printf("Case #%d: %d %d\n", te, DW, W);
    }
    return 0;
}
