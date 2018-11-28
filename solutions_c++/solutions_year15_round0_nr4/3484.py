#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int main() {
    freopen("D. Ominous Omino (small).out","w",stdout);
    int tc;
    cin >> tc;
    for (int a=1; a<=tc; a++) {
        string ans;
        int x,r,c,area;
        cin >> x >> r >> c;
        area = r*c;
        if (x==1)
            ans = "GABRIEL";
        else if (x==2)
            ans = area%2?"RICHARD":"GABRIEL";
        else if (x==3) {
            if (area==3)
                ans = "RICHARD";
            else if (area%3==0 && min(r,c)>1)
                ans = "GABRIEL";
            else
                ans = "RICHARD";
        }
        else if (x==4) {
            if (area==4)
                ans = "RICHARD";
            else if (area%4==0 && min(r,c)>2)
                ans = "GABRIEL";
            else
                ans = "RICHARD";
        }
        cout << "Case #" << a << ": " << ans << "\n";
    }
}
