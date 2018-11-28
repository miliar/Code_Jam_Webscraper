#include<cstdio>
#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    int cnt = 0;
    double curr, C, F, X, ans;
    scanf("%d", &T);
    while(T--){
        cin >> C >> F >> X;
        curr = 2.0;
        ans = 0.0;
        while(1){
/*            cout << "tar: " << X << endl;
            cout << "curr: " << curr << endl;
            cout << "next: " << curr+F << endl;
            cout << "not buy: " << (X-C)/curr << "sec left\n";
            cout << "buy: " << X/(curr+F) << "sec left\n";*/
            if((X-C)/curr < X/(curr+F)) break;
            ans += C/curr;
            curr += F;
        }
        ans += X/curr;
        printf("Case #%d: ", ++cnt);
        cout << fixed << setprecision(7) << ans << endl;
    }
    return 0;
}
