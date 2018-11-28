#include <cstdio>
#include <algorithm>
#include <deque>

using namespace std;

void solve(){
    int n;
    scanf("%d", &n);
    deque<double> Dme, Dop;
    int normal = 0, opt = 0;
    double val;
    for(int i = 0; i < n; ++i){
        scanf("%lf", &val);
        Dme.push_back(val);
    }
    for(int i = 0; i < n; ++i){
        scanf("%lf", &val);
        Dop.push_back(val);
    }
    sort(Dme.begin(), Dme.end());
    sort(Dop.begin(), Dop.end());
    int l = 0;
    int r = 0;
    while(l < n and r < n){
        if(Dme[l] < Dop[r]) l++;
        else normal++;
        r++;
    }
    for(int i = 0; i < n; ++i){
        if(Dme.back() > Dop.back()){
            Dme.pop_back();
            opt++;
        }else{
            Dme.pop_front();
        }
        Dop.pop_back();
    }
    printf("%d %d\n", opt, normal);
}

int main(){
    int allt;
    scanf("%d", &allt);
    for(int t = 1; t <= allt; ++t){
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}