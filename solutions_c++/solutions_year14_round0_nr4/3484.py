#include<stdio.h>
#include<set>
void solve(){
    std::set<double> a, b, b2;
    int n, i;
    double v;
    scanf("%d", &n);
    for(i =0;i<n;i++){
        scanf("%lf",&v);
        a.insert(v);
    }
    for(i =0;i<n;i++){
        scanf("%lf",&v);
        b.insert(v);
        b2.insert(v);
    }
    int war=0, dwar=0;
    for(std::set<double>::iterator it = a.begin(); it != a.end(); ++it){
        std::set<double>::iterator bit = b.lower_bound(*it);
        if(bit == b.end())
            war++, bit--;
        b.erase(bit);
    }
    while(b2.size()){
        std::set<double>::iterator bit = --b2.end();
        std::set<double>::iterator ait = --a.end();
        if(*bit > *ait){
            b2.erase(*bit);
            a.erase(a.begin());
        }
        else {
            dwar++;
            b2.erase(*bit);
            a.erase(ait);
        }
    }
    printf("%d %d\n", dwar, war);
}
int main(void){
#ifdef _DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
